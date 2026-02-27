# Data Cleaning Automation (Python)

## 📌 Project Description

This project is a **Python automation script** that processes CSV and Excel files.

The script automatically:

- Reads CSV or Excel files
- Removes duplicate rows
- Cleans missing values
- Sorts the data
- Saves a cleaned CSV file

This project demonstrates **basic data automation using Python and Pandas**.

## ⚙️ Requirements

Install required libraries:

```
pip install pandas openpyxl
```

Or

```
pip install -r requirements.txt
```

## 📂 Project Structure

```
data-cleaning-automation/
│
├── process_data.py
├── data.csv
├── data.xlsx
├── cleaned_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ How to Run

Run the script from the terminal:

```
python process_data.py data.csv
```

or

```
python process_data.py data.xlsx
```

## 📥 Input Example

```
name,age,city
John,25,London
Mike,30,Paris
John,25,London
Anna,,Berlin
Tom,22,Rome
```

## 📤 Output Example

```
name,age,city
John,25,London
Mike,30,Paris
Tom,22,Rome
```

The cleaned file will be saved as:

```
cleaned_data.csv
```

## 🛠 Features

- CSV support
- Excel support
- Duplicate removal
- Missing value cleaning
- Data sorting
- Command line usage

## 🧰 Technologies Used

- Python
- Pandas

---
