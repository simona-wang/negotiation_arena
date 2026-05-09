import matplotlib.pyplot as plt
import seaborn as sns


def plot_outcomes_by_condition(outcomes_df):
    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=outcomes_df,
        x="condition",
        hue="outcome"
    )

    plt.title("Negotiation Outcomes by Condition")
    plt.xlabel("Condition")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_average_turns_by_condition(outcomes_df):
    avg_turns = (
        outcomes_df
        .groupby("condition")["n_turns"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=avg_turns,
        x="condition",
        y="n_turns"
    )

    plt.title("Average Negotiation Length by Condition")
    plt.xlabel("Condition")
    plt.ylabel("Average Turns")
    plt.tight_layout()
    plt.show()


def plot_transition_heatmap(transition_matrix):
    plt.figure(figsize=(8, 6))

    sns.heatmap(
        transition_matrix,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Dialogue Act Transition Matrix")
    plt.tight_layout()
    plt.show()