# Customer Experience Analytics for Fintech Apps

## 📌 Overview
This project analyzes customer reviews for three Ethiopian banks: Commercial Bank of Ethiopia (CBE)
, Bank of Abyssinia (BOA), and Dashen Bank. It collects data from the Google Play Store, cleans it, prepares it and analyze sentiments and themes, and visualize insights. The goal is to understand customer sentiment and identify areas for improvement of their mobile apps to enhance
customer retention and satisfaction.


## Features

- Collects reviews, ratings, and dates for three major bank apps
- Handles missing data and removes duplicates
- Normalizes dates to YYYY-MM-DD format
- Outputs clean CSV data ready for analysis

## Banks Included

1. Commercial Bank of Ethiopia (CBE) (`com.combanketh.mobilebanking`)
2. Bank of Abyssinia (BOA) (`com.boa.boaMobileBanking`)
3. Dashen Bank (`com.dashen.dashensuperapp`)

## Output Format

The script generates a CSV file with these columns:

| Column  | Description                          | 
|---------|--------------------------------------|
| review  | Customer review text                 | 
| rating  | Star rating (1-5)                    | 
| date    | Date of review                       | 
| bank    | Bank name                            | 
| source  | Source platform (always Google Play) | 

## 📂 Repository Structure
```
customer-experience-analytics-week2/
├── data/
│ ├── processed/
│ │ └── processed_bank_app_reviews.csv # Cleaned and processed data
│ └── raw/
│   └── bank_app_reviews.csv # Raw data
├── notebooks/
│ ├── data_collection.ipynb
│ └── preprocess.ipynb
├── src/
│ ├── preprocessing.py 
│ └── scraping.py 
├── .github/
│ └── workflows/ # CI/CD pipelines
├── .gitignore
├── requirements.txt # Python dependencies
└── README.md # This file
```

## 🛠 Installation

1. Clone repository:
```bash
git clone git clone https://github.com/Martha3001/customer-experience-analytics-week2.git
cd customer-experience-analytics-week2
```

2. Create virtual environment:
```bash
python -m venv .venv
source venv/bin/activate 
.venv\Scripts\activate
```

3.Install dependencies:
```bash
pip install -r requirements.txt
```
