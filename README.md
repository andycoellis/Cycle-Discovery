# Cycle-Discovery
Script that discovers the amount of values that develop an endless cycle

* **Author:** [Andrew Ellis](https://www.linkedin.com/in/andrew-ellis-3a199113b/)

*Please be aware that more specific information about the challenge has been hidden as to keep company name and challenge secret*

### Specifications
* Python 2.7.13

### Packages
* [PyTest 5.0.1](https://docs.pytest.org/en/latest/)

### Overview
The given challenge required a srcipt that found out how many values were looped over in an endless cycle when assigning tasks to *minions*.

The given algorithm was:
```
1) Start a random ID n, a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next ID, and go back to step 2
```

### Notes

As with previous challenges my aim was to approach this with a [Test Driven Development](https://www.martinfowler.com/bliki/TestDrivenDevelopment.html) mindset utilising [GitHub Actions](https://github.com/features/actions).
