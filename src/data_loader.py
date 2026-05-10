import os
import json
import pandas as pd


def load_negochat_dataset(base_path: str) -> pd.DataFrame:
    rows = []

    for filename in os.listdir(base_path):
        if not filename.endswith(".json"):
            continue

        dialogue_id = filename.replace(".json", "")
        file_path = os.path.join(base_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            dialogue = json.load(f)

        split = dialogue.get("set", None)
        turns = dialogue.get("turns", [])

        for turn_id, turn in enumerate(turns):
            role = turn.get("role", None)
            text = turn.get("input") or turn.get("data") or ""
            outputs = turn.get("output", [])

            if len(outputs) == 0:
                rows.append({
                    "dialogue_id": dialogue_id,
                    "split": split,
                    "turn_id": turn_id,
                    "role": role,
                    "text": text,
                    "act": "Other",
                    "issue": None,
                    "value": None
                })
            else:
                for output in outputs:
                    for act, content in output.items():
                        issue = None
                        value = None

                        if isinstance(content, dict):
                            for issue_name, issue_value in content.items():
                                issue = issue_name
                                value = issue_value
                        elif content is True:
                            value = True

                        rows.append({
                            "dialogue_id": dialogue_id,
                            "split": split,
                            "turn_id": turn_id,
                            "role": role,
                            "text": text,
                            "act": act,
                            "issue": issue,
                            "value": value
                        })

    df = pd.DataFrame(rows)
    df = df.sort_values(["dialogue_id", "turn_id"]).reset_index(drop=True)

    return df


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)



def load_processed_human_data(processed_path: str) -> pd.DataFrame:
    """
    Load the processed human negotiation dataset.
    """

    if not os.path.exists(processed_path):
        raise FileNotFoundError(
            f"Processed dataset not found: {processed_path}"
        )

    return pd.read_csv(processed_path)


def save_processed_human_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the processed human negotiation dataset.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def load_or_create_human_data(raw_path: str, processed_path: str) -> pd.DataFrame:
    """
    Load the processed human dataset if it exists.
    If it does not exist, create it from the original Negochat JSON files.
    """

    if os.path.exists(processed_path):
        return load_processed_human_data(processed_path)

    human_df = load_negochat_dataset(raw_path)

    save_processed_human_data(
        human_df,
        processed_path
    )

    return human_df