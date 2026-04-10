import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Starting Task 4: Visualization...")

    # Load data
    df = pd.read_csv("data/cleaned_trends.csv")

    # ---------------- CHART 1 ----------------
    # Posts per category
    post_count = df["category"].value_counts()

    plt.figure()
    post_count.plot(kind="bar")
    plt.title("Number of Posts per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Posts")
    plt.show()

    # ---------------- CHART 2 ----------------
    # Average score per category
    avg_score = df.groupby("category")["score"].mean()

    plt.figure()
    avg_score.plot(kind="bar")
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.show()

    # ---------------- CHART 3 ----------------
    # Total comments per category
    total_comments = df.groupby("category")["num_comments"].sum()

    plt.figure()
    total_comments.plot(kind="bar")
    plt.title("Total Comments per Category")
    plt.xlabel("Category")
    plt.ylabel("Total Comments")
    plt.show()


if __name__ == "__main__":
    main()
