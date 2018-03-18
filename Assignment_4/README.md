
## Imports

These are the following imports you will be needing.

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import sys - Standard module

import webget - In this repo i have added the webget, because, our webget might be different that yours.

## How to run file
So the python file can be executed through the terminal with the following command.

python run.py

You can add a argument. This argument should be the path to the title.basics.tsv file.
An example of this could be - 

python run.py path/title.basics.tsv

By doing this the program will use the specified file.

If you dont provide the argument, the script will will look for the title.basics.tsv in the directory where the script is placed. If it doesnt find the file here it will download the file from https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_4/title.basics.tsv

The easiest way to run the program is to fork the repo and call the command - python run.py
By doing this all the files the script will have the files it needs to run.

## Answers:
### Q1: Which year was the most movies released?
![alt text](https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_4/Figure_1.png)

The year with most movies releases was:  2004

### Q2: Which year was most series ended?
![alt text](https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_4/figur_2.png)

The year where most series ended was:  2004

### Q3: Which genres has the longest runtime per movies?

The genre which the movie/series with the longest running time is  Documentary

### Q4: Which genre covers the most movies?

The genre the covers the most movies is:  Drama

### Q5: What is the average runtime on adult films?

The average runtime of adult movies is:  92 min
