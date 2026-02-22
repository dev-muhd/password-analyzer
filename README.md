# Password Analyzer

A rule-based password strength analyzer built in Python.

This project evaluates a password against a defined set of validation rules and classifies its strength using ratio-based thresholds.

---

## Overview

The analyzer checks a password against multiple rules, calculates a score based on passed rules, and classifies the result as:

- **Weak**
- **Medium**
- **Strong**

The classification is determined by comparing the ratio of passed rules to total rules against predefined thresholds.

---

## Features

- Minimum length validation (≥ 8 characters)
- Requires at least one digit
- Requires at least one uppercase letter
- Requires at least one lowercase letter
- Requires at least one special character
- Disallows spaces
- Rule-driven evaluation loop
- Division-by-zero safe ratio calculation
- Threshold-based strength classification

---

## Strength Classification Logic

Strength ratio is calculated as:

    strength_ratio = score / total_rule_count

Thresholds:

- `< 0.4` → Weak
- `< 0.7` → Medium
- `≥ 0.7` → Strong

If no rules exist, the ratio safely defaults to `0` to prevent runtime errors.

---

## Project Structure

password-analyzer/
│
├── src/
│   ├── analyzer.py
│   └── main.py
│
└── README.md

### analyzer.py

Contains:
- Individual rule functions
- Rule registry (list of rule-function/message tuples)
- Score calculation logic
- Ratio-based classification
- Returns structured dictionary result

### main.py

Handles:
- User input
- Calling the analyzer
- Displaying formatted results

---

## Example Output

    Enter password: dev_muhd3005$
    Password score: 5
    Total rules: 6
    Failures: ['Password must contain at least one uppercase letter']
    Password strength: Strong

---

## How to Run

From the project root:

    python src/main.py

---

## Design Approach

This project emphasizes:

- Separation of concerns (analysis vs. I/O)
- Rule-driven evaluation
- Defensive programming (zero-division guard)
- Scalable return structure (dictionary-based result)

The architecture allows easy addition of new rules without modifying core evaluation logic.

---

## Future Improvements

- Entropy-based strength scoring
- Configurable thresholds
- Weighted rules
- CLI flags instead of interactive input
- Unit tests
- JSON output mode

---

## Author

Built as part of a structured learning journey focused on strengthening control flow, modular design, and rule-based logic implementation.