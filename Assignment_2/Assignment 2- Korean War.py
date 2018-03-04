
import webget as wg
import pandas as pd
from glob import glob

wg.download("https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv")


milit_files = glob('.\\KoreanCon*')
KoreanConflict_csv = milit_files[0]


KC = pd.read_csv(KoreanConflict_csv)


# # Q1 - 
# Answer 4509 

kcGrouped = KC[KC["BRANCH"]=="MARINE CORPS"]
print("Marine Corps: ")
print(len(kcGrouped.index))


# # Q2
# Answer ACTIVE-REGULAR

kcGrouped = KC.groupby("ENROLLMENT").count()
print(kcGrouped.iloc[:,2])


# # Q3
# Answer yes, WHITE

kcGrouped = KC.groupby("ETHNICITY").count()
print(kcGrouped.iloc[:,2])


# # Q4
# Answer 38 INF 2 DIV - 1755 lost

kcGrouped = KC.groupby("DIVISION").count()
maxValue = kcGrouped.iloc[:,2].max()
mask = (kcGrouped.iloc[:,2]==maxValue)
print("Division : "+kcGrouped[mask].index.values+" had the most losses, with a total off: "+str(kcGrouped[mask].iloc[0,0]))


# # Q5
# Answer California - 2582 lost

kcGrouped = KC.groupby("HOME_STATE").count()
maxValue = kcGrouped.iloc[:,2].max()
mask = (kcGrouped.iloc[:,2]==maxValue)
print("The state of : "+kcGrouped[mask].index.values+" had the most losses, with a total off: " +str(kcGrouped[mask].iloc[0,0]))
