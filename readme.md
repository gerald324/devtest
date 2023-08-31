# BitBottles Software Developer Test

Welcome to the BitBottles Software Developer Test! This test is designed to evaluate your coding, problem-solving, and software design skills. Please read the instructions carefully before you begin.

## Instructions

1. Fork this repository to your own GitHub account.
2. Complete the coding tasks outlined below.
3. Push your code to your GitHub repository.
4. Submit the link to your GitHub repository for review.

You can use any programming language to solve these problems, as long as the code can run in a Unix environment (Mac/Linux/etc.).

### Evaluation Criteria

- Code Quality
- Problem-Solving Skills
- Adherence to best practices
- Readability and maintainability of code

---

## Question 1: FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz" instead of the number. For numbers which are multiples of both three and five, print "FizzBuzz".

### Requirements

1. Your program should be able to run from the command line.
2. The output should be printed to the standard output (console).

#### Example Output

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```

---

## Question 2: String Permutation with Wildcards

Write a program that takes as input a string of indeterminate length consisting of the characters '0', '1', and/or '*'. The asterisk ('*') is a wildcard character that can represent either '0' or '1'.

### Requirements

1. Your program should be able to run from the command line and accept the input string as either a command-line argument or through standard input.
2. The output should be printed to the standard output (console) and should consist of an array or list containing all possible permutations where the wildcard '*' can be replaced by either '0' or '1'.
3. Consider edge cases such as an empty string or a string containing only wildcard characters.

#### Example Input and Output

##### Input
```
"0*1"
```

##### Output
```
['001', '011']
```

##### Input
```
"**"
```

##### Output
```
['00', '01', '10', '11']
```

##### Input
```
""
```

##### Output
```
['']
```

Your solution will be evaluated based on code quality, efficiency, readability, and adherence to best practices.

---

Good luck!
