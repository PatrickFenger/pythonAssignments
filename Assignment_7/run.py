import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# Setting up useable csv file
webget.download("https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv")

#filed = glob('.\\ks-projects-201801.csv*')
#ks_projects = filed[0]
ks_df = pd.read_csv("ks-projects-201801.csv")
ks_matrix = ks_df.as_matrix()


# See columns for later use
# print(ks_df.dtypes)
def question_1():
    _, count = np.unique(ks_matrix[:,3], return_counts=True)
    mask = (ks_matrix[:,9] == "successful")
    successful_ks_projects = ks_matrix[mask]
    main_success, success_count = np.unique(
        successful_ks_projects[:,3], return_counts=True)
    print(main_success,success_count)
    success_rate = (success_count / count) * 100

    plt.figure("Question 1")
    plt.title("Successful kickstarters")
    plt.xlabel("Main Category")
    plt.ylabel("Success rate")
    plt.bar(main_success, success_rate)
    plt.show()

    print("Question 1:")
    print("Dance is the most successful main category 62,05%")

def question_2():
    mask = (ks_matrix[:, 3] == "Dance")
    grouping_ks_projects = ks_matrix[mask]
    category, count = np.unique(
        grouping_ks_projects[:, 2], return_counts=True)
    category = category[np.argsort(-count)]
    count = np.sort(count)[::-1]

    plt.figure("Question 2")
    plt.title("Proposed projects")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.bar(category, count)
    plt.show()

    print("Question 2:")
    print("Dance is the most proposed category")

def question_3():
    mask = (ks_matrix[:, 9] == "successful")
    grouping_ks_projects = ks_matrix[mask]
    ks_pledge_median = np.median(grouping_ks_projects[:, 13])
    result = "The pledged median of successful projects is: " + str(
        ks_pledge_median) + "$"
    print("Question 3:")
    print(result)

def question_4():
    mask = ((ks_matrix[:,9] == "successful") & (ks_matrix[:,13] > 5000.00))
    main_success, success_count = np.unique(
        ks_matrix[mask][:, 2], return_counts=True)
    plt.figure("Question 4")
    plt.title("number of successfully funded projects with more than 5.000$ pledged pr category")
    plt.xlabel("Category")
    plt.ylabel("successfully funded project")
    plt.bar(main_success, success_count)
    plt.show()

def question_5():
    mask = (ks_matrix[:,9] == "successful")
    main_success, main_count = np.unique(
        ks_matrix[mask][:, 3], return_counts=True)
    category = main_success[np.argsort(-main_count)[0]]
    print("The category with most funded projects: " + category)

    mask = (ks_matrix[:, 3] == category)
    max_goal = ks_matrix[mask][:,14]
    max_goal.sort()
    max_goal = [i//1000 for i in max_goal]
    most_succesfull_goal = (0,0)
    for i in range(0, int(max_goal[-1])):
        print(i)
        numbers = [j for j in max_goal if j<i+10 and j>i]
        sm = len(numbers)
        if sm > most_succesfull_goal[1]:
            most_succesfull_goal = (i, sm)

    print("Question 5")
    print("The range with most succesfull goal is : " + (str(most_succesfull_goal[0])) + " - "+(str(most_succesfull_goal[0]+10))+"k$")
    print("With : "+(str(most_succesfull_goal[1])) +" succesfull projects")


#question_1()
#question_2()
#question_3()
#question_4()
question_5()
