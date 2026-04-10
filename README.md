# 🚀 TrendPulse: What's Actually Trending Right Now

## 📌 Project Overview

TrendPulse is a 4-stage data pipeline that collects, processes, analyzes, and visualizes trending stories from the HackerNews API.

The project demonstrates real-world data engineering concepts using Python — from raw API data to meaningful insights.

---

## 🧩 Pipeline Structure

Task 1 → Task 2 → Task 3 → Task 4
Fetch JSON → Clean CSV → Analyze Data → Visualize

---

## ⚙️ Technologies Used

* Python
* requests (API calls)
* pandas (data cleaning & analysis)
* matplotlib (data visualization)

---

## 📥 Data Source

* HackerNews API
* https://hacker-news.firebaseio.com/

---

## 🛠️ Tasks Breakdown

### 🔹 Task 1: Data Collection

* Fetched top 500 trending stories from HackerNews API
* Categorized stories into:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Extracted fields:

  * post_id
  * title
  * category
  * score
  * num_comments
  * author
  * collected_at
* Saved as JSON file

---

### 🔹 Task 2: Data Cleaning

* Loaded JSON into pandas DataFrame
* Removed duplicates using `post_id`
* Handled missing values using `fillna()`
* Cleaned text fields
* Saved cleaned data as CSV

---

### 🔹 Task 3: Data Analysis

* Calculated:

  * Average score per category
  * Total comments per category
  * Number of posts per category
* Identified:

  * Top category
  * Most active author

---

### 🔹 Task 4: Data Visualization

* Created bar charts for:

  * Posts per category
  * Average score per category
  * Total comments per category
* Used matplotlib for visualization

---

## 📊 Key Insights

* Technology dominates HackerNews in both number of posts and engagement
* Some categories like sports and entertainment have fewer posts
* High-score posts tend to generate more discussions

---

## 📁 Project Structure

```
MiniProject/
│
├── task1_data_collection.py
├── task2_clean_csv.py
├── task3_analysis.py
├── task4_visualisation.py
│
├── data/
│   ├── trends_YYYYMMDD.json
│   └── cleaned_trends.csv
│
└── README.md
```

---

## ▶️ How to Run

1. Run Task 1:

```
python task1_data_collection.py
```

2. Run Task 2:

```
python task2_clean_csv.py
```

3. Run Task 3:

```
python task3_analysis.py
```

4. Run Task 4:

```
python task4_visualisation.py
```

---

## 🎯 Learning Outcomes

* API data collection using requests
* Data cleaning using pandas
* Data analysis using groupby operations
* Data visualization using matplotlib
* Building a complete data pipeline

---

## 📌 Conclusion

TrendPulse demonstrates how raw data from an API can be transformed into meaningful insights through structured data processing and analysis.

---

by
Sri Raja Rajeshwari
