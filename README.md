# Mathematical Expression Evaluator

This Python program is designed to parse and evaluate mathematical expressions provided as strings.

## Functions

1. `spaces(string)`: This function removes all spaces from the input string.
    - **Input**: A string (`string`) representing the expression.
    - **Output**: A string with all spaces removed.

2. `Paren_evaluate(string,a,b)`: This function splits the input string into a list of sub-expressions based on parentheses.
    - **Input**: A string (`string`) representing the expression. The opening parenthesis symbol (`a`) and the closing parenthesis symbol (`b`).
    - **Output**: A tuple consisting of two lists. The first list contains the sub-expressions, while the second list contains the corresponding priority levels for each sub-expression.

3. `Ope_evaluation(string)`: This function splits the input string into a list of numbers and operators.
    - **Input**: A string (`string`) representing the expression.
    - **Output**: A list that alternates between numbers and operators from the input string.

4. `Remuve_list_spaces(lista)`: This function removes all empty strings from the input list.
    - **Input**: A list (`lista`) that may contain empty strings.
    - **Output**: The same list but without any empty strings.

5. `math_evaluation(lista,ope)`: This function evaluates one operation in the input list of numbers and operators.
    - **Input**: A list (`lista`) of numbers and operators. An operator (`ope`) to evaluate.
    - **Output**: The same list but with the specified operation evaluated and replaced with the result.

6. `main_math_evaluation(lista)`: This function evaluates all operations in the input list of numbers and operators.
    - **Input**: A list (`lista`) of numbers and operators.
    - **Output**: The same list but with all operations evaluated and replaced with their results.

7. `main(string)`: This is the main function that evaluates a mathematical expression.
    - **Input**: A string (`string`) representing a mathematical expression.
    - **Output**: The result of the mathematical expression as a float.

## Usage

```python
A = "2+2"
print(main(A))
```

This will output `4`, which is the expected result of `2+2`.
