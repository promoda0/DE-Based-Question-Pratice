# Python for Data Engineering Interview Marathon

## Objective

This marathon is specifically for **Product-Based / FAANG Data
Engineering interviews**.

The focus is Python used for:

-   Data transformation
-   ETL-style problems
-   Data processing
-   Aggregation
-   File processing
-   JSON processing
-   Log processing
-   Large-data handling
-   Streaming
-   Memory optimization
-   Data Engineering problem solving

This is **not** a Python Developer / SDE DSA preparation track.

------------------------------------------------------------------------

# Important Separation

We will maintain **two separate preparation tracks**.

## Track 1 --- Data Engineering Python

This marathon.

Focus:

-   Realistic Data Engineering problems
-   Business/data-processing scenarios
-   Python collections
-   Data transformation
-   ETL patterns
-   Aggregation
-   Nested data
-   Files and streaming
-   Iterators and generators
-   Memory-efficient processing
-   SQL-to-Python thinking
-   PySpark-oriented thinking
-   Scalability and cost considerations

## Track 2 --- DSA / Problem Solving

This will be maintained separately.

Focus:

-   Two Pointers
-   Sliding Window
-   Hash Map DSA problems
-   Binary Search
-   Stack / Queue
-   Heap
-   Sorting
-   Intervals
-   Matrix
-   Other interview-relevant DSA patterns

The DSA track should **not be mixed into this DE marathon**.

------------------------------------------------------------------------

# DE Marathon Philosophy

The objective is not to memorize Python syntax or solve a fixed sequence
of predictable questions.

The objective is to learn how to:

1.  Understand a data/business requirement.
2.  Identify the appropriate data-processing approach.
3.  Choose the right Python data structure.
4.  Design the algorithm.
5.  Write clean and maintainable Python.
6.  Analyze time and space complexity.
7.  Handle edge cases.
8.  Optimize for large datasets.
9.  Think about streaming and memory usage.
10. Relate the solution to real Data Engineering systems.

------------------------------------------------------------------------

# Question Style

Questions should be **Data Engineering oriented** rather than generic
Python Developer questions.

Examples:

-   Transaction processing
-   Customer analytics
-   Order processing
-   Event logs
-   Clickstream data
-   File processing
-   ETL transformations
-   Nested JSON
-   Data quality
-   Deduplication
-   Aggregation
-   Batch processing
-   Streaming-style processing

Questions should not be artificially sequenced as:

``` text
Count
Sum
Max
Min
Count + Sum
Count + Sum + Max
```

The next problem should not be predictable.

Instead, problems should require the candidate to determine the pattern
independently.

------------------------------------------------------------------------

# Discussion-Based Learning

One problem may lead to a long discussion.

We do **not** need to solve only one question and immediately move to
the next.

After solving a problem, we can explore:

-   Why the solution works
-   Alternative approaches
-   Better data structures
-   Time complexity
-   Space complexity
-   Edge cases
-   Production considerations
-   Memory optimization
-   Streaming approach
-   Large-scale data
-   SQL equivalent
-   PySpark equivalent
-   Cost considerations
-   Similar DE problems
-   Interview follow-up questions

A single problem may therefore generate **10--15 related variations and
discussion points**.

The goal is to master the underlying pattern, not maximize the number of
questions completed.

------------------------------------------------------------------------

# Code Quality Standards

All DE Python solutions should follow professional Python coding
standards.

## PEP 8

Code should follow PEP 8 conventions for:

-   Indentation
-   Naming
-   Whitespace
-   Line length
-   Blank lines
-   Imports
-   Operators
-   Function definitions

Example:

``` python
revenue_by_status = {}
```

Not:

``` python
revenue_by_status={}
```

------------------------------------------------------------------------

# Flake8

Solutions should be written so they are compatible with **Flake8-style
code quality checks**.

We should pay attention to:

-   Unused variables
-   Unused imports
-   Undefined names
-   Incorrect indentation
-   Excessive line length
-   Whitespace issues
-   Naming issues
-   Unnecessary complexity

Flake8 is a **code-quality standard for this DE marathon**, not the
focus of the DSA track.

------------------------------------------------------------------------

# Type Hints

Use type hints where they improve clarity.

Example:

``` python
def calculate_revenue(
    orders: list[tuple[str, int, str]]
) -> dict[str, int]:
    ...
```

Type hints should describe the actual input and output structure.

------------------------------------------------------------------------

# Naming

Use meaningful names.

Prefer:

``` python
revenue_by_status
customer_orders
transaction_count
total_revenue
```

Avoid:

``` python
x
y
a
b
data
value
```

unless the shorter name is genuinely clear from the context.

Names should communicate the business meaning of the data.

------------------------------------------------------------------------

# Function Naming

Function names must describe the actual responsibility of the function.

Good:

``` python
calculate_revenue_by_status()
```

Bad:

``` python
count_orders_by_status()
```

when the function actually calculates revenue.

The function name should remain correct even when another engineer reads
the code without the original problem statement.

------------------------------------------------------------------------

# Avoid Premature Python Shortcuts

During the first implementation, prioritize:

-   Clear algorithm
-   Explicit logic
-   Readability
-   Pattern recognition

Do not immediately hide the algorithm behind shortcuts such as:

``` python
Counter
defaultdict
sum(...)
filter(...)
map(...)
```

when the purpose of the problem is to understand the underlying
algorithm.

After the core solution is understood, we can discuss the Pythonic or
production-oriented alternative.

------------------------------------------------------------------------

# Complexity

Every DE solution should eventually discuss:

### Time Complexity

Example:

``` text
O(n)
```

### Space Complexity

Example:

``` text
O(k)
```

where `k` represents the number of unique groups.

Complexity should be connected to realistic data sizes.

For example:

``` text
1,000 records
1 million records
100 million records
```

------------------------------------------------------------------------

# Large-Data Thinking

For DE problems, always consider:

> What happens when the input becomes very large?

For example:

``` text
10 GB file
100 GB file
1 TB dataset
100 million records
```

Questions to consider:

-   Can the entire dataset fit in memory?
-   Can we process records incrementally?
-   Can we use a generator?
-   Can we reduce intermediate objects?
-   Can we process the data in chunks?
-   Can we perform the aggregation in one pass?
-   Can the operation be distributed?
-   What would change in Spark?

------------------------------------------------------------------------

# Streaming Thinking

For relevant problems, discuss the difference between:

``` text
Load everything
```

and:

``` text
Process incrementally
```

Example:

``` python
for record in records:
    process(record)
```

versus materializing a massive dataset into memory.

Generators and iterators will therefore be an important part of the DE
marathon.

------------------------------------------------------------------------

# SQL and PySpark Connection

When useful, we will connect Python solutions to Data Engineering
concepts.

For example:

``` text
Python Dictionary Aggregation
        ↓
SQL GROUP BY
        ↓
PySpark groupBy().agg()
```

The goal is not to replace Python with SQL or Spark.

The goal is to understand the **same data-processing pattern across
technologies**.

------------------------------------------------------------------------

# Interview Review

Solutions will be reviewed like a real engineering code review.

Review areas:

-   Requirement understanding
-   Correctness
-   Algorithm
-   Data structure
-   Complexity
-   Edge cases
-   Scalability
-   Memory usage
-   PEP 8
-   Flake8
-   Naming
-   Readability
-   Maintainability
-   Production considerations

We should not use artificial scores such as:

``` text
99/100
98/100
```

unless a specific mock interview requires scoring.

The review should instead identify:

-   What is correct
-   What is weak
-   What should be changed
-   Why it should be changed
-   What an interviewer may challenge

------------------------------------------------------------------------

# Learning Principle

The goal is **not**:

``` text
Solve 150 isolated Python questions.
```

The goal is:

``` text
Problem
   ↓
Understand the data
   ↓
Recognize the pattern
   ↓
Choose the data structure
   ↓
Implement
   ↓
Optimize
   ↓
Scale
   ↓
Connect to DE concepts
```

A single problem can therefore be more valuable than many repetitive
problems if it produces deeper understanding.

------------------------------------------------------------------------

# Target Outcome

By the end of this marathon, we should be able to take an unfamiliar
Data Engineering Python problem and independently:

-   Understand the requirement
-   Design the solution
-   Select appropriate data structures
-   Write clean Python
-   Explain complexity
-   Handle edge cases
-   Optimize memory
-   Think about large-scale processing
-   Explain the solution clearly in an interview
-   Connect the solution to SQL and PySpark when appropriate

------------------------------------------------------------------------

# Scope

### Included

-   Python for Data Engineering
-   Data processing
-   ETL-style transformations
-   Collections
-   Dictionaries
-   Sets
-   Lists
-   Tuples
-   Nested data
-   Files
-   JSON
-   CSV
-   Logs
-   Iterators
-   Generators
-   Streaming
-   Memory optimization
-   Aggregation
-   Data quality
-   SQL-to-Python thinking
-   PySpark-oriented thinking

### Excluded from this Marathon

-   Django
-   Flask
-   FastAPI
-   Backend development
-   Web development
-   Advanced SDE-only DSA
-   Competitive programming
-   AVL Trees
-   Red-Black Trees
-   Segment Trees
-   Fenwick Trees
-   Advanced Graph Algorithms
-   Hard Dynamic Programming

DSA preparation is maintained separately.

------------------------------------------------------------------------

# Core Principle

> **Understand the data first, identify the pattern second, write the
> code third, and optimize for scale last.**

The purpose of this marathon is to develop the thinking required from a
**Product-Based Data Engineer**, not simply the ability to write Python
syntax.
