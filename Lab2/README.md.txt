# Python Lab 2

This repository contains the Python programs for Lab 2, covering loops, functions, patterns, and interactive applications.

### 1. Armstrong Number
* **Aim:** To check if a single number is an Armstrong number and print all Armstrong numbers in a user-provided range.
* **Logic:** The program extracts digits of the number, raises each digit to the power of the total number of digits, and checks if their sum equals the original number.
* **Sample Input / Output:**
  * Input: `153`
  * Output: `153 is an Armstrong number.`

### 2. Prime Number
* **Aim:** To check if a number is prime and print all prime numbers up to a given limit.
* **Logic:** The program checks for divisibility from 2 up to the square root of the number. If no divisor is found, it is identified as a prime number.
* **Sample Input / Output:**
  * Input: `7`
  * Output: `7 is a Prime number.`

### 3. Perfect Number
* **Aim:** To check if a number is a perfect number and print all perfect numbers up to a given limit.
* **Logic:** The program calculates the sum of all proper divisors of the number (excluding the number itself). If the sum equals the number, it is a perfect number.
* **Sample Input / Output:**
  * Input: `6`
  * Output: `6 is a Perfect number.`

### 4. Palindrome
* **Aim:** To check if a number is a palindrome using arithmetic operations and to check if a string is a palindrome.
* **Logic:** For the number, it reverses the digits using modulus and division. For the string, it uses Python's slicing method to compare the original and reversed string.
* **Sample Input / Output:**
  * Input: `121`
  * Output: `121 is a palindrome number.`

### 5. Fibonacci Series
* **Aim:** To print the first n terms of the Fibonacci series using a loop and recursion.
* **Logic:** The loop version iteratively adds the previous two terms. The recursive version calls itself until it reaches the base case (n=0 or 1), calculating the sum of two previous recursive calls.
* **Sample Input / Output:**
  * Input: `5`
  * Output: `[0, 1, 1, 2, 3]`

### 6. Pattern Printing
* **Aim:** To print a right-angled triangle of stars, a number pattern, and a centered pyramid using nested loops.
* **Logic:** Nested loops are used where the outer loop controls rows and the inner loop controls column printing (stars, numbers, or spaces for alignment).
* **Sample Input / Output:**
  * Input: `3`
  * Output:
    ```
    *
    **
    ***
    ```

### 7. Menu-Driven Application
* **Aim:** To provide a single interface to run all previous programs (1-6) using a menu-driven approach.
* **Logic:** The program uses a `while True` loop to continuously display a menu and takes user input to select and execute the corresponding function until the user chooses to exit.
* **Sample Input / Output:**
  * Input: `1`
  * Output: `(Runs Armstrong Number logic)`

### 8. Number Guessing Game
* **Aim:** To create a game where the user guesses a randomly generated number within a fixed range and attempt limit.
* **Logic:** The `random` module generates a target number. The program compares the user's guess to the target, providing "too high" or "too low" hints until the correct guess or the attempt limit is reached.
* **Sample Input / Output:**
  * Input: `50`
  * Output: `Too low!`