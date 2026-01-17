# AI Code Review Assignment (Python)

## Candidate
- Name: Melaku Azene
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Division by total number of orders instead of non-cancelled orders
- No handling for empty orders list
- Potential division by zero if all orders are cancelled

### Edge cases & risks
- Empty orders list
- All orders cancelled
- Non-numeric order amounts
- Missing or invalid order status
- Large number of orders (performance)

### Code quality / design issues
- No input validation
- No type hints
- No docstring
- Magic string for status

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added input validation
- Only count non-cancelled orders in average
- Handle empty list and all-cancelled cases
- Added type hints and docstring
- Improved variable names

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
- Empty orders list
- All orders cancelled
- Mixed cancelled and valid orders
- Large order lists
- Non-numeric amounts
- Missing order fields
- Different order status formats

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Incorrectly states it divides by number of non-cancelled orders (actually divides by total)
- Doesn't mention edge cases
- Overly confident about correctness

### Rewritten explanation
This function calculates the average value of non-cancelled orders. It sums the amounts of all orders with status not equal to "cancelled" and divides by the count of those orders. Returns 0.0 if there are no valid orders or if the input is empty. Handles edge cases including empty input and all-cancelled orders.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The core logic is mostly correct but fails on edge cases and has potential division issues. The function needs input validation and better handling of edge conditions.
- Confidence & unknowns: High confidence in identified issues. Unknown if there are specific business rules about order status values.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Only checks for '@' character, allowing many invalid formats
- No validation of email structure
- Doesn't handle None or non-string inputs

### Edge cases & risks
- Empty strings
- Multiple @ symbols
- Invalid TLDs
- International characters
- Very long strings
- Non-string inputs

### Code quality / design issues
- No input validation
- No type hints
- No docstring
- Overly simplistic validation

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added proper email validation with regex
- Added input type checking
- Improved error handling
- Added type hints and docstring
- Extracted validation to separate function

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations
- Valid email formats
- Common invalid formats
- Edge cases (missing @, multiple @, invalid TLDs)
- Non-string inputs
- Empty strings and None values
- Very long strings
- International characters

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Overstates the function's validation capabilities
- Doesn't specify what makes an email "valid"
- Implies it handles edge cases it doesn't

### Rewritten explanation
This function counts email addresses that match a standard email format pattern. It validates each input string against a regex pattern that checks for basic email structure (local@domain.tld). Returns 0 for non-list inputs. Note that while it catches many invalid formats, email validation is complex and this implementation may have some false positives/negatives.

## 4) Final Judgment
- Decision: Reject
- Justification: The current implementation's validation is too simplistic for production use. It would allow many invalid email formats while potentially rejecting some valid ones.
- Confidence & unknowns: High confidence in the need for better validation. Unknown if there are specific business rules about email formats.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by total length including None values
- No input validation
- Converts all non-None values to float without type checking
- No handling of invalid numeric strings

### Edge cases & risks
- All None values
- Non-numeric strings
- Very large/small numbers
- Mixed types in input
- Empty input list
- Non-list inputs

### Code quality / design issues
- No input validation
- No type hints
- No docstring
- Magic string for status

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added input type validation
- Only count valid numeric values in average
- Properly handle None values and invalid numbers
- Added type hints and docstring
- Improved error handling
- Return 0.0 for empty or invalid input

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
- Empty input list
- All None values
- Mixed valid and invalid numbers
- Large/small numbers
- Numeric strings vs actual numbers
- Non-numeric strings
- Non-list inputs
- Very large input lists
- Mixed types (int, float, string, None)

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation
- Implies it handles all mixed types safely
- Doesn't mention division by zero risk
- Overstates the function's safety with invalid inputs

### Rewritten explanation
This function calculates the average of valid numeric values in the input list, ignoring None values and non-numeric entries. It safely handles type conversion and returns 0.0 if no valid numbers are found. The function is designed to be resilient to various input types and edge cases, though performance may degrade with very large lists due to the type checking overhead.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The function needs better input validation and error handling. The current implementation could be more explicit about what constitutes a valid measurement and handle edge cases more gracefully.
- Confidence & unknowns: High confidence in the need for improvements. Unknown if there are specific numeric ranges or formats that should be considered invalid.
