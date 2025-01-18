import pandas as pd
import numpy as np
import sys
import os

def read_input_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")

    if os.stat(file_path).st_size == 0:
        raise ValueError(f"Error: The file '{file_path}' is empty.")

    data = pd.read_csv(file_path)

    if data.shape[1] < 3:
        raise ValueError("Error: Input file must contain at least three columns.")

    if data.iloc[:, 0].isnull().any():
        raise ValueError("Error: The first column (object/variable names) contains empty values.")

    return data

def validate_weights_and_impacts(weights, impacts, num_criteria):
    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != num_criteria:
        raise ValueError("Error: The number of weights must match the number of criteria columns.")

    try:
        weights = [float(w) for w in weights]
    except ValueError:
        raise ValueError("Error: All weights must be numeric.")

    if len(impacts) != num_criteria:
        raise ValueError("Error: The number of impacts must match the number of criteria columns.")

    if not all(i in ['+', '-'] for i in impacts):
        raise ValueError("Error: Impacts must be either '+' or '-'.")

    return weights, impacts

def normalize_decision_matrix(matrix):
    return matrix / np.sqrt((matrix**2).sum(axis=0))

def calculate_ideal_values(weighted_matrix, impacts):
    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    return np.array(ideal_best), np.array(ideal_worst)

def calculate_distances(weighted_matrix, ideal_best, ideal_worst):
    distance_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))
    return distance_best, distance_worst

def topsis(input_file, weights, impacts, output_file):
    try:
        data = read_input_file(input_file)

        fund_names = data.iloc[:, 0]
        matrix = data.iloc[:, 1:]

        if not all(np.issubdtype(matrix[col].dtype, np.number) for col in matrix.columns):
            raise ValueError("Error: All columns from 2nd to last must contain numeric values.")

        weights, impacts = validate_weights_and_impacts(weights, impacts, matrix.shape[1])

        norm_matrix = normalize_decision_matrix(matrix)
        weighted_matrix = norm_matrix * weights

        ideal_best, ideal_worst = calculate_ideal_values(weighted_matrix, impacts)

        distance_best, distance_worst = calculate_distances(weighted_matrix, ideal_best, ideal_worst)

        topsis_score = distance_worst / (distance_best + distance_worst)

        data['Topsis Score'] = topsis_score
        data['Rank'] = data['Topsis Score'].rank(ascending=False, method='min').astype(int)

        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

    except (FileNotFoundError, ValueError) as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <script_name>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python topsis.py data.csv \"1,1,1,2\" \"+,+,-,+\" result.csv")
    else:
        input_file = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        output_file = sys.argv[4]

        topsis(input_file, weights, impacts, output_file)