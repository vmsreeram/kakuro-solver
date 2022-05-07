# kakuro-solver
This project is an implementation of the classical Constraint Satisfaction Problem (CSP). The goal was to implement a Kakuro solver that treats the puzzle as a CSP. 

It is assumed that the input is valid, and a unique solution exists for it. If multiple valid solutions exist, then only one valid solution will be returned.

## Kakuro
Kakuro is a kind of logic puzzle that is often referred to as a mathematical transliteration of the crossword. Solving it involves placement of non zero digits in squares satisfying certain row and column constraints. Learn more about the puzzle from the Wikipedia article - https://en.wikipedia.org/wiki/Kakuro

## What all were implemented?
1. Input checking to handle unsupported input format.
2. AC-3 algorithm was implemented which reduced the domain of each variables.
3. A generic Bactracking Search (BS) was implemented, without any heuristics. 
4. The BS could also be used with MAC (Maintaining Arc Consistency) which calls AC-3 for related variables if BS alters the domain of some variable. 

## Input-output format
The puzzle supported by this project is in the format as given in ``` samples/input0.txt ```. First two lines indicates number of rows and columns respectively. The horizontal and vertical represents one by one filling of respective cells in the row or column format of the board. ‘#’ represents black cells that do not have to be filled. Empty cells in the puzzle that need to be filled with a number are represented as ‘0’.

The output will be of same format as the input, except that all the ‘0’s will be replaced by the solution digits.

## How to run?
Once the file is available locally, you can run it by executing this command :  
  ```zsh
  python3 kakuro.py -i <path/to/input-file> -o <path/to/output-file>
  ```
