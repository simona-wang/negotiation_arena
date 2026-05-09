import re


def parse_structured_response(text: str) -> dict:
    result = {
        "message": None,
        "salary_offer": None,
        "hours_offer": None,
        "decision": None
    }

    for line in text.splitlines():
        line = line.strip()

        if line.startswith("MESSAGE:"):
            result["message"] = line.replace("MESSAGE:", "").strip()

        elif line.startswith("SALARY_OFFER:"):
            value = line.replace("SALARY_OFFER:", "").strip()

            if value.upper() == "NONE":
                result["salary_offer"] = None
            else:
                number = re.search(r"\d[\d,]*", value)
                if number:
                    result["salary_offer"] = int(number.group().replace(",", ""))

        elif line.startswith("HOURS_OFFER:"):
            value = line.replace("HOURS_OFFER:", "").strip()

            if value.upper() == "NONE":
                result["hours_offer"] = None
            else:
                number = re.search(r"\d+(\.\d+)?", value)
                if number:
                    result["hours_offer"] = float(number.group())

        elif line.startswith("DECISION:"):
            result["decision"] = line.replace("DECISION:", "").strip().lower()

    return result