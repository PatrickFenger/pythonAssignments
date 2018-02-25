import xlrd
import matplotlib.pyplot as plt
import re
import webget
from collections import Counter
url ="https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls"
#print(os.system("s"))
url2 = "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls"



# This fuction donwnload a xls file and return xl sheet object
def _get_sheet(url):
    xl_workbook = xlrd.open_workbook(webget.download(url))
    sheet_names = xl_workbook.sheet_names()

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    return xl_sheet

#Question 1
def question_1(url,plot=None):
    xl_sheet = _get_sheet(url)
    dict = {}
    for row_idx in range(4, 24):
        key = list(str(xl_sheet.cell(row_idx,0)).split(":"))[1]
        key  = key.replace("\'", "")
        key = key[0:4]
        sumd = 0.0
        for col_idx in range(2,20,2):
            temp = str(xl_sheet.cell(row_idx, col_idx)).split(":")
            sumd +=float(temp[1])
        dict[int(key)]=sumd
    if plot:
        listx = list(dict.keys())
        listt = list(dict.values())

        plt.bar(listx,listt,color='g')
        plt.xlabel('Year', fontsize=18)
        plt.ylabel('Amount of crime', fontsize=16)
        plt.show()
    return dict


#question 2
def question_2(url):
    xl_sheet = _get_sheet(url)
    dict = {}
    for row_idx in range(4, 24):
        key = list(str(xl_sheet.cell(row_idx, 0)).split(":"))[1]
        key = key.replace("\'", "")
        key = key[0:4]
        sumd = 0.0
        most_common_crime = ""
        for col_idx in range(2, 20, 2):
            temp = float(list(str(xl_sheet.cell(row_idx, col_idx)).split(":"))[1])
            if sumd < temp:
                sumd = temp
                col_value = list(str(xl_sheet.cell(3, col_idx)).split(":"))
                most_common_crime = col_value[1].replace('\\n', ' ')
        dict[int(key)] = most_common_crime
    return dict

#Question 5
def question_5(url):
    dict1 = question_1(url)
    dict2 = question_2(url)
    temp_value_sum = 0.0
    key = 0
    for year,value in dict1.items():
        if value > temp_value_sum:
            temp_value_sum = value
            key = year
    print("The year with most crimes was in ",key,", and the crime type was",dict2.get(key))

#Question 4
def question_4(url):
    xl_sheet1 = _get_sheet(url)
    state = ""
    dict = {}
    temp_dict = {}
    for row_idx in range(4, 9297):
        temp_state = list(str(xl_sheet1.cell(row_idx, 0)).split(":"))[1]
        city = list(str(xl_sheet1.cell(row_idx, 1)).split(":"))[1]
        temp_list = []
        temp_sum = 0.0
        crime_type = ""
        if re.match("\'([A-Za-z]+)\'",temp_state):

            state=temp_state
            dict[state] = []
        for col in range(3, 14):
            temp_value = list(str(xl_sheet1.cell(row_idx, col)).split(":"))[1]
            if "\'" not in temp_value:
                if float(temp_value) > temp_sum and "\'" not in temp_value:
                    temp_sum = float(temp_value)
                    crime_type = str(list(str(xl_sheet1.cell(3, col)).split(":"))[1]).replace("\\n"," ")

        temp_dict[city] = crime_type
        dict[state].append(temp_dict)
    _most_frequent_value(dict)



#This code need to be optimized...
# this function is used to display the most frequent crime in each state.
def _most_frequent_value(dict):
    c = Counter()
    for key,value in dict.items():
        for obj in value:
            for crimtype in obj.values():
                arts = crimtype
                c[arts] += 1
        print(key,str(c.most_common(1)),"\n")

question_1(url,True)
question_2(url)
question_4(url2)
question_5(url)
