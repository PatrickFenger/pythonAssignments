##How to run pyton file : 

The file you need to run, to generate the output stated below is exercise_v2.py.
The to url should be given as arguments.

its important that dataset 1 is given as first argument and dataset 2 as second argument: 

Eksampel : python exercise_v2.py 'https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls' 'https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls'

##Imports : 

Our solution uses the following imports : 
import xlrd
import matplotlib.pyplot as plt
import re
import webget
from collections import Counter
import sys

I think the only modules you need to download is xlrd and webget, because our webget return the path of the downloaded file.
The webget modules can be downloaded from this link : https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_1/webget.py



Dataset 1 :

Q1: Has the crime decreased or increased over the last 20 years?
![alt text](https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_1/Figure_1.png)

We can see that the amout of crimes commited has been decresing over the year.

Q2: Has the type of crime changed? 

{1994: "'Property  crime'", 1995: "'Property  crime'", 1996: "'Property  crime'", 1997: "'Property  crime'", 1998: "'Property  crime'", 1999: "'Property  crime'", 2000: "'Property  crime'", 2001: "'Property  crime'", 2002: "'Property  crime'", 2003: "'Property  crime'", 2004: "'Property  crime'", 2005: "'Property  crime'", 2006: "'Property  crime'", 2007: "'Property  crime'", 2008: "'Property  crime'", 2009: "'Property  crime'", 2010: "'Property  crime'", 2011: "'Property  crime'", 2012: "'Property  crime'", 2013: "'Property  crime'"}

If we take a look at the data above we can se that the most commited crime type always has been property crime.

Dataset 2 :

Q3: Has the crime moved from one area to another?

Q4: Is there a connection between type of crimes and locations?

If we take a look at the result below, we can se that the there isnt a connection between the crime and location , because the most common crime is property crime in all states.

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

Q5: Which year was the most crime commited? and which crime occured most times?

The year with most crimes was in  1994 , and the crime type was 'Property  crime'
