import pandas as pd


def is_valid_agreement_for_candidate(salary, hours) -> bool:
    return (
        salary is not None
        and hours is not None
        and salary >= 85000
        and hours <= 9
    )


def is_valid_agreement_for_employer(salary, hours) -> bool:
    return (
        salary is not None
        and hours is not None
        and salary <= 87000
        and hours >= 9
    )


def check_acceptance(speaker: str, parsed: dict) -> bool:
    salary = parsed["salary_offer"]
    hours = parsed["hours_offer"]
    decision = parsed["decision"]

    if decision != "accept":
        return False

    if speaker == "Candidate":
        return is_valid_agreement_for_candidate(salary, hours)

    if speaker == "Employer":
        return is_valid_agreement_for_employer(salary, hours)

    return False


def compute_outcome_distribution(outcomes_df: pd.DataFrame) -> pd.Series:
    return outcomes_df["outcome"].value_counts()


def compute_agreement_rate_by_condition(outcomes_df: pd.DataFrame) -> pd.Series:
    return outcomes_df.groupby("condition")["outcome"].apply(
        lambda x: (x == "Agreement").mean()
    )


def compute_average_turns_by_condition(outcomes_df: pd.DataFrame) -> pd.Series:
    return outcomes_df.groupby("condition")["n_turns"].mean()


def compute_transition_matrix(df: pd.DataFrame, act_col: str = "act") -> pd.DataFrame:
    transitions = []

    for _, group in df.groupby("dialogue_id"):
        group = group.sort_values("turn_id")
        acts = group[act_col].tolist()

        for i in range(len(acts) - 1):
            transitions.append((acts[i], acts[i + 1]))

    transition_df = pd.DataFrame(
        transitions,
        columns=["current_act", "next_act"]
    )

    return pd.crosstab(
        transition_df["current_act"],
        transition_df["next_act"]
    )