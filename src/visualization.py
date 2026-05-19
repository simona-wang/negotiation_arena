import matplotlib.pyplot as plt
import seaborn as sns

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