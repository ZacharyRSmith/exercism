# Difference Of Squares

Find the difference between the sum of the squares and the square of the sums of the first N natural numbers.

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)**2 = 55**2 = 3025

The sum of the squares of the first ten natural numbers is,

    1**2 + 2**2 + ... + 10**2 = 385

Hence the difference between the square of the sum of the first
ten natural numbers and the sum of the squares is 2640:

    3025 - 385 = 2640

## Setup

Go through the setup instructions for PL/SQL to get ready to code:

http://help.exercism.io/getting-started-with-plsql.html

## Running the Tests

Execute the tests by calling the `run` method in the respective `ut_<exercise>#` package.
The necessary code should be contained at the end of the test package.
As an example, the test for the _hamming_ exercise would be run using

```
begin
  ut_hamming#.run;
end;
/
```

## Source

Problem 6 at Project Euler [view source](http://projecteuler.net/problem=6)
