import pandas as pd

def main():
    print("Starting Task 3: Data Analysis...")

    # Load CSV
    file_path = "data/cleaned_trends.csv"
    df = pd.read_csv(file_path)

    print("\nTotal records:", len(df))

    # ---------------- ANALYSIS ----------------

    # 1. Average score per category
    avg_score = df.groupby("category")["score"].mean()

    print("\nAverage Score per Category:")
    print(avg_score)

    # 2. Total comments per category
    total_comments = df.groupby("category")["num_comments"].sum()

    print("\nTotal Comments per Category:")
    print(total_comments)

    # 3. Number of posts per category
    post_count = df["category"].value_counts()

    print("\nNumber of Posts per Category:")
    print(post_count)

    # 4. Top category
    top_category = post_count.idxmax()
    print("\nTop Category:", top_category)

    # 5. Most active author
    top_author = df["author"].value_counts().idxmax()
    print("Most Active Author:", top_author)


if __name__ == "__main__":
    main()
