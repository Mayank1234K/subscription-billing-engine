Subscription Billing & Status Evaluation Engine
Project Overview

This project implements a Python-based billing engine for a subscription-based digital service.
It processes subscription and usage data, applies business rules, calculates monthly billing, evaluates subscription status, and generates output reports.

The system is designed with modular architecture, robust error handling, logging, and unit testing to ensure reliability and maintainability.

Objectives
Process subscription and usage data from CSV files
Apply billing and status evaluation rules
Handle invalid and missing data safely
Generate billing output and summary reports
Ensure minimum 80% test coverage
Maintain clean and modular code structure

Project Structure
project/
│── data/
│   ├── subscriptions.csv
│   ├── usage.csv
│
│── src/
│   ├── loader.py
│   ├── usage_aggregator.py
│   ├── billing_engine.py
│   ├── status_engine.py
│   ├── reporter.py
│   └── main.py
│
│── tests/
│   ├── test_billing_engine.py
│   ├── test_status_engine.py
│   ├── test_usage_aggregator.py
│
│── logs/
│   └── billing.log
│
│── billing_output.csv
│── billing_summary.json
│── README.md

 Business Rules
1. Usage Aggregation
Only usage data for March 2024 is considered
Invalid dates are ignored
Total usage is aggregated per subscription
2. Billing Rules
If usage <= limit → bill = monthly fee
If usage > limit →
overage = usage - limit
overage charge = overage × 10
total bill = monthly fee + overage charge
If status = SUSPENDED → charge only monthly fee
If status = CANCELLED → bill = 0
3. Status Evaluation Rules
If usage > 150% of limit → SUSPENDED
If previously SUSPENDED and usage ≤ limit → ACTIVE
CANCELLED status remains unchanged

 Data Processing Flow
Load subscription and usage data
Aggregate monthly usage
Merge subscription and usage data
Apply billing logic
Evaluate final subscription status
Generate output files

 Output Files
1. billing_output.csv

Contains:

subscription_id
customer_id
plan
total_usage_gb
overage_gb
total_bill
final_status
2. billing_summary.json

Contains:

total_subscriptions
active_subscriptions
suspended_subscriptions
cancelled_subscriptions
total_revenue
average_bill

🧪 Unit Testing
Framework Used
pytest
Test Coverage
Minimum 80% coverage
Test Categories
Billing Logic Tests
Status Evaluation Tests
Usage Aggregation Tests
Run Tests
python -m pytest

▶ How to Run the Application
Step 1: Install dependencies
pip install pandas pytest
Step 2: Navigate to project
cd src
Step 3: Run application
python main.py

 Logging:
Logging is implemented using Python’s logging module
Errors and processing details are stored in:
logs/billing.log

 Error Handling:
Invalid dates are skipped
Missing numeric values default to safe values (e.g., usage = 0)
Application does not crash due to bad data

 Assumptions
Input CSV files are correctly formatted
Missing usage records imply zero usage
Data types are handled safely using conversions
NumPy data types are converted to Python types for JSON serialization

 Edge Cases Handled:
No usage records
Invalid usage dates
Missing or null values
Suspended and cancelled subscriptions
Over-usage scenarios

Technologies Used:
Python
Pandas
Pytest
Logging module
* Evaluation Criteria Covered
✔ Correct implementation of business logic
✔ Modular and clean code structure
✔ Comprehensive unit testing
✔ Robust error handling
✔ Logging and documentation

Conclusion:

This project demonstrates a scalable and maintainable approach to building a subscription billing engine, ensuring accuracy, reliability, and testability.