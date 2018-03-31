import pandas as pd
import webget
import collections
import re
import operator

temp_list = []

question3_dict = {"name": "no song", "amount": 0}

question4_dict = {"words": 0, "songs": 0}



def file_reader():
    for chunk in pd.read_table("songdata.csv", sep=',', chunksize=1024):
        yield chunk


def question_3(dd, word="LOVE"):
    for i in dd:
        temp_value = re.findall(r'(\w+[\']*)+',str(i[3]).replace('\n', '').replace('\r', '').replace('\\n', '').upper())
        if word.upper() in temp_value:
            amount = collections.Counter(temp_value).get(word.upper())
            if amount > question3_dict.get("amount"):
                question3_dict["name"] = i[1]
                question3_dict["amount"] = amount


def question_1(dd):
    global temp_list
    temp = re.findall(r'(\w+[\']*)+', str(dd[:, 3]).replace('\n', '').replace('\r', '').replace('\\n', '').upper())
    non_valid_word = ["THE", "I", "YOU", 'AND', 'TO', 'A', 'ME', "T", "S", 'MY', 'IN', 'IT', 'M', "ON", 'THAT', 'OF',
                      'YOUR', 'ALL', 'FOR', 'WE', 'IS', 'BE', 'KNOW', 'UP', 'LIKE', 'BUT', 'GET', 'SO', 'WITH', ]
    temp_list += [elm for elm in temp if elm not in non_valid_word]

def question_2(dd,title="It's So Cool"):
        for i in dd:
            if title in i:
                length = len(re.findall(r'(\w+[\']*)+',str(i[3]).replace('\n', '').replace('\r', '').replace('\\n', '').
                                        upper()))
                print("Question-2: ", "The amount of words in ", title, " is ", length)


def question_4(dd):
    for i in dd[:,3]:
        question4_dict["words"] += len(re.findall(r'(\w+[\']*)+', str(i).replace('\n', '').replace('\r', '').replace('\\n', '').upper()))
        question4_dict["songs"] += 1


def main():
    chunk = file_reader()
    for i in chunk:
        dd = i.as_matrix()
        question_1(dd)
        question_2(dd)
        question_4(dd)
        question_3(dd)

    print("Question-1: The most used word is", max(collections.Counter(temp_list), key=collections.Counter(temp_list).
                                                   get))
    print("Question-3: ", question3_dict.get("name"))
    print("Question-4: ", round(question4_dict.get("words")/question4_dict.get("songs"),2))


if __name__ == "__main__":
    webget.download('https://github.com/KasperOnFire/ImpossibleTechnology/raw/master/Datasets/songdata.csv')
    main()