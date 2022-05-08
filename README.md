# kakuro-solver
This project is an implementation of the classical Constraint Satisfaction Problem (CSP). The goal was to implement a Kakuro solver that treats the puzzle as a CSP. 

## Kakuro
Kakuro is a kind of logic puzzle that is often referred to as a mathematical transliteration of the crossword. Solving it involves placement of non zero digits in squares satisfying certain row and column constraints. Learn more about the puzzle from the Wikipedia article - https://en.wikipedia.org/wiki/Kakuro

## What all were implemented?
1. Input checking to handle unsupported input format.
2. AC-3 algorithm to reduce the domain of each variable.
3. A generic Backtracking Search (BS) algorithm without any heuristics.
4. MAC (Maintaining Arc Consistency) algorithm which calls AC-3 for related variables if BS alters the domain of some variable.

## Input-output format
The puzzle supported by this project is in the format as given in ``` simple/input0.txt ```. First two lines indicate the number of rows and columns respectively. `Horizontal` and `Vertical` represents one by one filling of respective cells in the row or column format of the board. ‘#’ represents black cells that do not have to be filled. Empty cells in the puzzle that need to be filled with a digit are represented as ‘0’.

The output will be of the same format as the input, except that all the ‘0’s will be replaced by the solution digits.

It is assumed that the input is valid, and a unique solution exists for it. If multiple valid solutions exist, then only one valid solution will be returned.

## How to run?
Once the `kakuro.py` file is available locally, it can run be run by executing the command:  
  ```zsh
  python3 kakuro.py -i <path/to/input-file> -o <path/to/output-file>
  ```

## Licence
[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2022 VM Sreeram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
