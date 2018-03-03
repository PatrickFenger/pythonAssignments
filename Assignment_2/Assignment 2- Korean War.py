
import pandas as pd
import numpy as np
import webget as wg
from glob import glob
import matplotlib.pyplot as plt


wg.download("https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv")


milit_files = glob('.\\KoreanCon*')
KoreanConflict_csv = milit_files[0]


KC = pd.read_csv(KoreanConflict_csv)


# # Q1 - 
# Answer 4509 

kcGrouped = KC[KC["BRANCH"]=="MARINE CORPS"]
len(kcGrouped.index)


# # Q2
# Answer ACTIVE-REGULAR

kcGrouped = KC.groupby("ENROLLMENT").count()
kcGrouped.iloc[:,2]


# # Q3
# Answer yes, WHITE

kcGrouped = KC.groupby("ETHNICITY").count()
kcGrouped.iloc[:,2]


# # Q4
# Answer 38 INF 2 DIV - 1755 lost

kcGrouped = KC.groupby("DIVISION").count()
maxValue = kcGrouped.iloc[:,2].max()
mask = (kcGrouped.iloc[:,2]==maxValue)
kcGrouped[mask]


# # Q5
# Answer California - 2582 lost

kcGrouped = KC.groupby("HOME_STATE").count()
maxValue = kcGrouped.iloc[:,2].max()
mask = (kcGrouped.iloc[:,2]==maxValue)
kcGrouped[mask]