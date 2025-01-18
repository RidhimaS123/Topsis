# TOPSIS Implementation in Python

This repository contains a Python implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method, which is used for multi-criteria decision-making. The algorithm helps rank alternatives based on multiple criteria, considering their weights and impacts.

---

## How to Use

### Requirements

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `numpy`

Install the required libraries using:

```bash
pip install pandas numpy
```

### Command-Line Usage

The script takes the following arguments:

1. **Input CSV File**: The input data file containing the criteria and alternatives.
2. **Weights**: A comma-separated list of numeric weights corresponding to each criterion.
3. **Impacts**: A comma-separated list of impacts (`+` for beneficial and `-` for non-beneficial criteria).
4. **Output CSV File**: The file to save the results, including TOPSIS scores and rankings.

#### Syntax:

```bash
python <script_name>.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

#### Example:

```bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv
```

---

## Input File Format

- The input file should be a CSV file with the following structure:
  - The **first column** contains the names of alternatives (e.g., products, funds, etc.).
  - The remaining columns contain numeric values representing criteria.
- Ensure there are **at least three columns** in the input file.

#### Example:

```csv
Alternative,Criterion1,Criterion2,Criterion3,Criterion4
A1,250,16,12,5
A2,200,18,14,3
A3,300,20,10,4
```

---

## Output File

The output file will be a CSV file with the following additional columns:

- **Topsis Score**: The calculated TOPSIS score for each alternative.
- **Rank**: The rank of each alternative based on the TOPSIS score (higher score = better rank).

#### Example Output:

```csv
Alternative,Criterion1,Criterion2,Criterion3,Criterion4,Topsis Score,Rank
A1,250,16,12,5,0.75,1
A2,200,18,14,3,0.60,3
A3,300,20,10,4,0.70,2
```

---

## Error Handling

The script includes error handling for the following cases:

1. **File Not Found**: If the input file does not exist.
2. **Empty File**: If the input file is empty.
3. **Invalid File Structure**: If the input file has fewer than three columns or contains non-numeric data in criteria columns.
4. **Mismatched Weights and Impacts**: If the number of weights or impacts does not match the number of criteria.
5. **Invalid Impacts**: If impacts are not `+` or `-`.

---

## Contact

For questions or issues, please reach out to rsharma1_be22@thapar.edu .

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
