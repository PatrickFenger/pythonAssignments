## Local Group: Mushy bread

## Members:
 - Patrick Fenger
 - Pravien Thaveenrasingam
 - Sean Altoft
 - Martin Lodahl 
-----------------------------------------------------------------



## How to run pyton file : 

For you to be able to run this program you have to clone this badboy, activate your gitbash and execute the following file called exercise_v2.py

As seen below it is important that the collected data set (namely dataset 1 & dataset 2) are passed as arguments
int that given order

In case of doubt simply concede to our very best friend copy and paste the example code below into your gitbash

Eksampel : python exercise_v2.py 'https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls' 'https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls'

When you execute the file a plot will pop up , this is the answer for Question 1. The answers for question 2 ,4 and 5 will be accessible in the terminal after a short time - Patience is the key here.

Should you (hopefully you dont) encounter any errors, make sure you have the following imports:

## Imports : 
import xlrd

import matplotlib.pyplot as plt

import re

import webget
from collections import Counter

import sys

The only module that doesn't come as default is xlrd, so you have to download that.
We have placed a webget.py file in the repo and this is the webget that is used in the project. The reason why we have added this, is because our webget returns the filename so it might differ from the webget you have installed.

## Dataset 1 :

### Q1: Has the crime decreased or increased over the last 20 years?
![alt text](https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_1/Figure_1.png)

Answer: From above shown graph we can conclude that the crime have been decreasing over the last 20 years.

### Q2: Has the type of crime changed? 

{1994: "'Property  crime'", 1995: "'Property  crime'", 1996: "'Property  crime'", 1997: "'Property  crime'", 1998: "'Property  crime'", 1999: "'Property  crime'", 2000: "'Property  crime'", 2001: "'Property  crime'", 2002: "'Property  crime'", 2003: "'Property  crime'", 2004: "'Property  crime'", 2005: "'Property  crime'", 2006: "'Property  crime'", 2007: "'Property  crime'", 2008: "'Property  crime'", 2009: "'Property  crime'", 2010: "'Property  crime'", 2011: "'Property  crime'", 2012: "'Property  crime'", 2013: "'Property  crime'"}

Answer: If we take a look at the data above we can see that the most committed crime type have been properpy all the way through 1994 up and included 2013 which indicates that the type of crime has not changed.

### Q5: Which year was the most crime commited? and which crime occured most times?

Answer: By the information gather in Q1 & Q2 we can conclude that the year with most crimes was in  1994 , and the crime type was 'Property  crime'

## Dataset 2 :

### Q3: Has the crime moved from one area to another?

Answer: We experienced insufficient data in the dataset to answer this question. Feel free to elaborate should you have experienced otherwise.

### Q4: Is there a connection between type of crimes and locations?

Answer:  If we take a look at the result below, we cannot conclude that there is a specific connection between the crime being comitted and the location due to the fact that the most common crime is property crime in all states.

'ALABAMA' [("'Property crime'", 1355732)] 

'ALASKA' [("'Property crime'", 1542491)] 

'ARIZONA' [("'Property crime'", 1978262)] 

'ARKANSAS' [("'Property crime'", 3043480)] 

'CALIFORNIA' [("'Property crime'", 6239134)] 

'COLORADO' [("'Property crime'", 7172929)] 

'CONNECTICUT' [("'Property crime'", 7809293)] 

'DELAWARE' [("'Property crime'", 8044471)] 

'FLORIDA' [("'Property crime'", 10050401)] 

'GEORGIA' [("'Property crime'", 11800402)] 

'IDAHO' [("'Property crime'", 12229256)] 

'ILLINOIS' [("'Property crime'", 15729258)] 

'INDIANA' [("'Property crime'", 16476294)] 

'IOWA' [("'Property crime'", 17250998)] 

'KANSAS' [("'Property crime'", 18191710)] 

'KENTUCKY' [("'Property crime'", 19595861)] 

'LOUISIANA' [("'Property crime'", 20377482)] 

'MAINE' [("'Property crime'", 21159103)] 

'MARYLAND' [("'Property crime'", 21691712)] 

'MASSACHUSETTS' [("'Property crime'", 23621555)] 

'MICHIGAN' [("'Property crime'", 25994086)] 

'MINNESOTA' [("'Property crime'", 27508909)] 

'MISSISSIPPI' [("'Property crime'", 27778672)] 

'MISSOURI' [("'Property crime'", 30856737)] 

'MONTANA' [("'Property crime'", 31154168)] 

'NEBRASKA' [("'Property crime'", 31506935)] 

'NEVADA' [("'Property crime'", 40312276)] 

'OHIO' [("'Property crime'", 42684807)] 

'OKLAHOMA' [("'Property crime'", 44206547)] 

'OREGON' [("'Property crime'", 44960500)] 

'PENNSYLVANIA' [("'Property crime'", 52548449)] 

'TENNESSEE' [("'Property crime'", 54270782)] 

'TEXAS' [("'Property crime'", 58448650)] 

'UTAH' [("'Property crime'", 59015844)] 

'VERMONT' [("'Property crime'", 59257939)] 

'VIRGINIA' [("'Property crime'", 60288572)] 

'WASHINGTON' [("'Property crime'", 61990154)] 

'WISCONSIN' [("'Property crime'", 64023752)] 

'WYOMING' [("'Property crime'", 64279681)] 
