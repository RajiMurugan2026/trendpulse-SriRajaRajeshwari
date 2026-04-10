import json
import pandas as pd
import os

# ---------------- LOAD JSON ----------------
def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Error loading JSON:", e)
        return []

# ---------------- CLEAN DATA ----------------
def clean_data(df):
    # Remove duplicate posts
    df = df.drop_duplicates(subset="post_id")

    # Handle missing values
    df["title"] = df["title"].fillna("No Title")
    df["author"] = df["author"].fillna("unknown")

    df["score"] = df["score"].fillna(0)
    df["num_comments"] = df["num_comments"].fillna(0)

    # Clean text
    df["title"] = df["title"].str.strip()
    df["category"] = df["category"].str.strip().str.lower()

    return df

# ---------------- MAIN ----------------
def main():
    print("Starting Task 2: Cleaning Data...")

    file_path = input("Enter JSON file path: ")

    data = load_json(file_path)

    if not data:
        print("No data found!")
        return

    # Convert to DataFrame
    df = pd.DataFrame(data)

    print(f"Original records: {len(df)}")

    # Clean
    df = clean_data(df)

    print(f"After cleaning: {len(df)}")

    # Create folder
    os.makedirs("data", exist_ok=True)

    # Save CSV
    output_file = "data/cleaned_trends.csv"
    df.to_csv(output_file, index=False)

    print(f"Cleaned CSV saved to {output_file}")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
