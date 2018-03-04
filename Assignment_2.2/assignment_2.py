import numpy as np
import webget
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import sys
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def download_file(url):
    return webget.download(url)


def question_1(filename):
    korean_conf_stat = pd.read_csv(filename)
    dd = korean_conf_stat.as_matrix()
    mask = (dd[:, 3] =="MARINE CORPS")
    row,col = dd[mask].shape
    print(row," entered from the MARINE CORPS")


def question_2(filename):
    korean_conf_stat = pd.read_csv(filename)
    dd = korean_conf_stat.as_matrix()
    enrolments = np.unique(dd[1:,2])
    y=[np.size(dd[(dd[:,2]==i)],0) for i in enrolments]
    x = list(np.arange(len(y)))
    plt.bar(enrolments, y,color="blue")
    #plt.savefig("question_2")
    plt.xlabel("Enrollment")
    plt.ylabel("Amount of people")
    plt.savefig("question_2")

def question_3(filename):
    korean_conf_stat = pd.read_csv(filename)
    dd = korean_conf_stat.as_matrix()
    mask_ethnicity_1 = (dd[:, 15] != "")
    mask_ethnicity_2 = (dd[:, 16] != "")
    mask_ethnicity_3 = (dd[:, 17] != "")

    eth_1 = np.unique(list(dd[mask_ethnicity_1][:,15]))
    eth_2 = np.unique(list(dd[mask_ethnicity_2][:, 16]))
    eth_3 = np.unique(list(dd[mask_ethnicity_3][:, 17]))

    temp1=Counter({i:np.size(dd[dd[:,15]==i],0)  for i in eth_1 if i != "nan"})
    temp2 = Counter({i: np.size(dd[dd[:, 16] == i], 0) for i in eth_2 if i != "nan"})
    temp3 = Counter({i: np.size(dd[dd[:, 17] == i], 0) for i in eth_3 if i != "nan"})
    res = temp1+temp2+temp3
    plt.bar(res.keys(),res.values())
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
    plt.xticks(rotation='vertical', fontsize=5)
    plt.xlabel("Ethnicity")
    plt.ylabel("Amount of people")
    plt.savefig("question_3")


def question_4(filename):
    korean_conf_stat = pd.read_csv(filename)
    dd = korean_conf_stat.as_matrix()
    mask = (dd[:, 18] != None)
    divions = dd[mask]
    templist = []
    templist = [str(division[18]) for division in divions if division[18] not in templist]
    templist = set(templist)
    casualties = {i:np.size(dd[(dd[:, 18] == i)], 0) for i in templist}
    maximum = max(casualties, key=casualties.get)

    print("The division with name: "+maximum)

def question_5(filename):
    korean_conf_stat = pd.read_csv(filename)
    dd = korean_conf_stat.as_matrix()
    mask = (dd[0:, 13] != "")
    print(mask)
    homestates = np.unique(list(dd[mask][:,13]))
    for index,i in enumerate(homestates):
        if i in states.keys():
            homestates[index]=states[i].upper()
    homestates = np.unique(list(homestates))
    casualties = {i: np.size(dd[(dd[:, 13] == i)], 0) for i in homestates if i != "nan"}
    print(casualties)
    plt.bar(casualties.keys(),casualties.values())
    plt.xticks(rotation='vertical',fontsize=5)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
    plt.ylabel("Casualties")
    plt.xlabel("Home state")
    plt.savefig("question_5")

if __name__ in "__main__":
    filename = download_file(sys.argv[1])
    print(filename)
    question_1(filename)
    #question_2(filename)
    #question_3(filename)
    #question_4(filename)
    #question_3(filename)

