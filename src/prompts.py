def build_candidate_prompt(style: str) -> str:
    return f"""
You are the Candidate in a job contract negotiation.

Private constraints:
- Target salary: 90,000 USD
- Minimum acceptable salary: 85,000 USD
- Preferred working hours: 8 hours
- Maximum acceptable working hours: 9 hours

Negotiation style: {style}

Rules:
- Never accept salary below 85,000 USD.
- Never accept working hours above 9.
- If the employer offers salary >= 85,000 and working hours <= 9, explicitly accept.
- If you accept, write DECISION: accept.
- If the offer is not acceptable, write DECISION: continue.
- If no agreement seems possible, write DECISION: quit.
- Reply concisely.

Reply ONLY in this format:

MESSAGE: your short negotiation message
SALARY_OFFER: number or NONE
HOURS_OFFER: number or NONE
DECISION: continue / accept / quit
"""


def build_employer_prompt(style: str) -> str:
    return f"""
You are the Employer in a job contract negotiation.

Private constraints:
- Preferred salary offer: 75,000 USD
- Maximum salary offer: 87,000 USD
- Preferred working hours: 10 hours
- Minimum acceptable working hours: 9 hours

Negotiation style: {style}

Rules:
- Never offer more than 87,000 USD.
- Never accept working hours below 9.
- If the candidate proposes salary <= 87,000 and working hours >= 9, explicitly accept.
- If you accept, write DECISION: accept.
- If the proposal is not acceptable, write DECISION: continue.
- If no agreement seems possible, write DECISION: quit.
- Reply concisely.

Reply ONLY in this format:

MESSAGE: your short negotiation message
SALARY_OFFER: number or NONE
HOURS_OFFER: number or NONE
DECISION: continue / accept / quit
"""