import pandas as pd

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

def infer_human_outcome(group):
    """
    A dialogue is classified as Agreement if it contains at least one Accept act,
    Failure if it contains a Quit act and no Accept act, and Unresolved otherwise.
    """
    acts = group["act"].tolist()

    if "Accept" in acts:
        return "Agreement"

    if "Quit" in acts:
        return "Failure"

    return "Unresolved"


def infer_human_outcome_refined(group, final_window=3):
    """
    FinalAgreement means that an Accept act appears in the final turns.
    PartialOrIntermediateAccept means that Accept appears, but not near the end.
    """
    group = group.sort_values("turn_id")

    all_acts = group["act"].tolist()

    last_turn_ids = (
        group["turn_id"]
        .drop_duplicates()
        .sort_values()
        .tail(final_window)
    )

    final_acts = group[
        group["turn_id"].isin(last_turn_ids)
    ]["act"].tolist()

    if "Accept" in final_acts:
        return "FinalAgreement"

    if "Accept" in all_acts:
        return "PartialOrIntermediateAccept"

    if "Quit" in all_acts:
        return "Failure"

    return "Unresolved"