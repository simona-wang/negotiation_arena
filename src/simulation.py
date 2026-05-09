from src.prompts import build_candidate_prompt, build_employer_prompt
from src.parsing import parse_structured_response
from src.metrics import check_acceptance


def run_negotiation_simulation(
    scenario,
    condition,
    run_id,
    generate_response_fn,
    max_turns=6
):
    conversation_log = []

    candidate_prompt = build_candidate_prompt(condition["candidate_style"])
    employer_prompt = build_employer_prompt(condition["employer_style"])

    current_message = """
MESSAGE: I would like a salary of 90,000 USD and an 8 hour workday.
SALARY_OFFER: 90000
HOURS_OFFER: 8
DECISION: continue
"""

    outcome = None

    for turn in range(max_turns):

        employer_text = generate_response_fn(
            employer_prompt,
            current_message
        )

        parsed_employer = parse_structured_response(employer_text)

        conversation_log.append({
            "scenario_id": scenario["scenario_id"],
            "condition": condition["condition_name"],
            "run_id": run_id,
            "turn": turn,
            "speaker": "Employer",
            "text": employer_text,
            "salary_offer": parsed_employer["salary_offer"],
            "hours_offer": parsed_employer["hours_offer"],
            "decision": parsed_employer["decision"]
        })

        if check_acceptance("Employer", parsed_employer):
            outcome = "Agreement"
            break

        if parsed_employer["decision"] == "quit":
            outcome = "Failure"
            break

        current_message = employer_text

        candidate_text = generate_response_fn(
            candidate_prompt,
            current_message
        )

        parsed_candidate = parse_structured_response(candidate_text)

        conversation_log.append({
            "scenario_id": scenario["scenario_id"],
            "condition": condition["condition_name"],
            "run_id": run_id,
            "turn": turn,
            "speaker": "Candidate",
            "text": candidate_text,
            "salary_offer": parsed_candidate["salary_offer"],
            "hours_offer": parsed_candidate["hours_offer"],
            "decision": parsed_candidate["decision"]
        })

        if check_acceptance("Candidate", parsed_candidate):
            outcome = "Agreement"
            break

        if parsed_candidate["decision"] == "quit":
            outcome = "Failure"
            break

        current_message = candidate_text

    if outcome is None:
        outcome = "Timeout"

    return conversation_log, outcome