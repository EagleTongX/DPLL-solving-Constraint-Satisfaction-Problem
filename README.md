##Davis-Putnam algorithm 
Implement Davis-Putnam algorithm and use it to solve parallel program optimization problem.

**Input Format:**

*DP.py:*

Take input from input.txt

The input to the Davis-Putnam procedure has the following form:
An atom is denoted by a natural number: 1,2,3 ... The literal P is the same number as atom P; the literal ~P is the negative. A clause is a line of text containing the integers of the corresponding literals. After all the clauses have been given, the next line is the single value 0; anything further in the file is ignored in the execution of the procedure and reproduced at the end of the output file.

*front_back.py:*

Take input as the format:

1 A 2 B 3 C 4 D

2 A 3 A 4 C

2

First line: A list of alternative registers and values at the start state, separated by white space. Assume
that the registers are numbers in increasing order and that the value are simple alphabetical symbols.
Second line: A specification of the goal state: same format as first line.
Third line: The time limit K,
