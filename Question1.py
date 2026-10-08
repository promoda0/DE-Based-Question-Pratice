'''# Question 1 — Positive Transaction Validation

## Difficulty

Easy

## Business Scenario

An e-commerce system receives transaction amounts from customers.

Before processing a transaction, the system needs to validate whether the transaction amount is valid.

A transaction amount is considered **valid only when it is greater than 0**.

## Problem

Write a Python function that checks whether a given transaction amount is valid.

## Input

```python
amount = 2500
```

## Output

```python
True
```

### Example 2

```python
amount = -500
```

Output:

```python
False
```

### Example 3

```python
amount = 0
```

Output:

```python
False
```

## Requirements

- Return `True` when the amount is greater than `0`.
- Return `False` when the amount is `0` or negative.
- Use a function.
- Add appropriate type hints.
- Handle the input as an integer.

## Expected Function

```python
def is_valid_transaction(amount: int) -> bool:
    ...
```

## Tags

`Python` `Conditional Logic` `Data Validation`

## Complexity Target

- Time: `O(1)`
- Space: `O(1)` '''