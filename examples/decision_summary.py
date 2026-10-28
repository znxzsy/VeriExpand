"""Fictional bookkeeping only: no verification, generation or training logic."""

import json


def summarize(record):
    """Summarize externally supplied decisions; None means evidence is missing."""
    name = record["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a nonempty string")
    capability = record["capability_checks_passed"]
    learning = record["learning_evidence_supports_use"]
    if any(value is not None and type(value) is not bool
           for value in (capability, learning)):
        raise ValueError("decisions must be bool or None")
    if learning is True and capability is not True:
        raise ValueError("training use requires capability admission")
    admission = "pending" if capability is None else (
        "admitted" if capability else "not_admitted")
    if capability is not True:
        training_use = "not_eligible"
    elif learning is None:
        training_use = "pending"
    else:
        training_use = "supported" if learning else "not_supported"
    return {"name": name, "fictional": True,
            "capability_admission": admission, "training_use": training_use}


def main():
    fictional_records = [
        {"name": "toy_candidate_a", "capability_checks_passed": True,
         "learning_evidence_supports_use": False},
        {"name": "toy_candidate_b", "capability_checks_passed": True,
         "learning_evidence_supports_use": True},
        {"name": "toy_candidate_c", "capability_checks_passed": None,
         "learning_evidence_supports_use": None},
    ]
    print(json.dumps({"notice": "Fictional illustration; not experiment results",
                      "records": [summarize(row) for row in fictional_records]},
                     indent=2))


if __name__ == "__main__":
    main()
