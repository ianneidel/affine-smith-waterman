# Smith-Waterman Algorithm Implementation
A Python implementation of the Smith-Waterman algorithm, supporting an affine gap penalty. We provide a pip installable package and the base script, along with instructions for each. The script and example files for inputs and outputs are in the smithwaterman folder.

## The Python Package
### Package Installation
Run `pip install git+https://github.com/ianneidel/affine-smith-waterman`

### Package Usage
Use in Python scripts by importing with `from smithwaterman import runSW`

Use runSW within a Python script as follows:

`runSW(<inputFile>, <scoreFile>, [openGap, extGap])`

The function's arguments are:
* `<inputFile>` is the path to your input file, formatted as in the example sample-input1.txt, i.e., two sequences, delimited by a new line; required.

* `<scoreFile>` is the path to your score file, formatted as in the example blosum62.txt, i.e., a tab-delimited similarity matrix including all of the characters used in the sequences; required.

* `[openGap]` is the penalty incurred by opening a new gap; optional, defaults to -2

* `[extGap]` is penalty incurred by extending an existing gap; optional, defaults to -1

An example usage of the runSW function is as follows:
`runSW("sample-input1.txt", "blosum62.txt")`

This will print out the alignment results (for the above command's results peruse sample-output1.txt); see the Script output section below for more details.


## The Script:
### Script Usage
After cloning the repository, run the following from the smithwaterman directory
  `python hw1.py -i <input file> -s <score file>`

Including optional arguments,
  `python hw1.py -i <input file> -s <score file> [-o open-gap-penalty] [-e extend-gap-penalty]`
  
As such, an example run would use the following command
  `python hw1.py -i input.txt -s blosum62.txt`

### Script Arguments:
* `-i`: include the path to your input file, formatted as in the example sample-input1.txt, i.e., two sequences, delimited by a new line.

* `-s`: include the path to your score file, formatted as in the example blosum62.txt, i.e., a tab-delimited similarity matrix including all of the characters used in the sequences

* `-o`: the penalty incurred by opening a new gap; optional, defaults to -2

* `-e`: the penalty incurred by extending an existing gap; optional, defaults to -1

## Output:
Running the script/function prints the input sequences, the score matrix used to calculate the optimal local alignment, and the aligned sequences. See example output in sample-output1.txt.
