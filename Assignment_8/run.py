import webget
import pandas as pd
import numpy as np
import re
from collections import Counter
import matplotlib.pyplot as plt

# Setting up useable csv file
webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv")
webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv")


obama_df = pd.read_csv("BarackObama.csv", encoding='ANSI')
donald_df = pd.read_csv("realDonaldTrump.csv", encoding='ANSI')
obama_matrix = obama_df.as_matrix()
donald_matrix = donald_df.as_matrix()
#                              0        1   2   3       4           5       6
#Help understanding, lines: created_at,text,url,replies,retweets,favorites,user - Trump and Obama .. Both datasets.

# See columns for later use
# print(ks_df.dtypes)
def question_1():
    count = Counter(donald_matrix[:,6])
    print("Question 1:")
    print(sum(count.values()))


def question_2():
    count = Counter(obama_matrix[:,6])
    print("Question 2:")
    print(sum(count.values()))

def question_3():
    obama_text = ''.join(obama_matrix[:,1]).lower()
    obama_count = [m.start() for m in re.finditer('yes we can', obama_text)]

    donald_text = ''.join(donald_matrix[:,1]).lower()
    donald_count = [m.start() for m in re.finditer('makeamericagreatagain', donald_text)]
    donald_count2 = [m.start() for m in re.finditer('make america great again', donald_text)]
    print("Question 3:")
    print("Obama mentions his slogan: " + str(len(obama_count))+" times")
    print("Donald mentions his slogan: " + str(len(donald_count)+len(donald_count2))+" times")

def question_4():
    obama_text = ''.join(obama_matrix[:,1]).lower()
    obama_count = [m.start() for m in re.finditer('iran', obama_text)]

    donald_text = ''.join(donald_matrix[:,1]).lower()
    donald_count = [m.start() for m in re.finditer('iran', donald_text)]
    print("Question 4:")
    print("Obama mentions Iran: " + str(len(obama_count)) + " times")
    print("Donald mentions Iran: " + str(len(donald_count)) + " times")

def question_5():
    obama_text = ''.join(obama_matrix[:,1]).lower()
    obama_count = [m.start() for m in re.finditer('obamacare', obama_text)]

    donald_text = ''.join(donald_matrix[:,1]).lower()
    donald_count = [m.start() for m in re.finditer('obamacare', donald_text)]
    print("Question 5:")
    print("Obama mentions Obamacare: " + str(len(obama_count)) + " times")
    print("Donald mentions Obamacare: " + str(len(donald_count)) + " times")


question_1()
question_2()
question_3()
question_4()
question_5()
