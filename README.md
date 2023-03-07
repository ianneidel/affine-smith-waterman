# Smith-Waterman Algorithm Implementation
A Python implementation of the Smith-Waterman algorithm, supporting an affine gap penalty.


## Usage:
Run the following
  `python hw1.py -i <input file> -s <score file>`

Including optional arguments
  `python hw1.py -i <input file> -s <score file> [-o open-gap-penalty] [-e extend-gap-penalty]`
  
As such, an example run would use the following command
  `python hw1.py -i input.txt -s blosum62.txt`


## Arguments:
`-i`: include the path to your input file, formatted as in the example sample-input1.txt, i.e., two sequences, delimited by a new line.

`-s`: include the path to your score file, formatted as in the example blosum62.txt, i.e., a tab-delimited similarity matrix including all of the characters used in the sequences

`-o`: the penalty incurred by opening a new gap; defaults to -2

`-e`: the penalty incurred by extending an existing gap; defaults to -1


## Output:
Running the script prints the input sequences, the score matrix used to calculate the optimal local alignment, and the aligned sequences. See example output in sample-output1.txt.
