import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import webget


def question_1(file_path):
    start_year = {}
    #Reads the csv file chuck by chuck - a chunk is 1 mb
    for chunk in pd.read_table(file_path, sep='\t', chunksize=1024):
        for elm in np.asarray(chunk)[0:, 5]:
            if not elm in start_year:
                start_year[elm] = 1
            else:
                start_year[elm] += 1
    year = max(start_year , key=start_year .get)
    print("The year with most movies releases was: ",year)
    # Plot the graph
    plt.bar(start_year .keys(), start_year .values(), width=0.3)
    plt.title('Amount of movies released pr year')
    plt.xticks(rotation=70, fontsize=5)
    plt.xlabel('Year')
    plt.ylabel("Amount of movies")
    plt.tight_layout()
    plt.text(year, start_year[year], str(year), horizontalAlignment="center")
    plt.show()
    plt.close()


def question_2(file_path):
    end_year = {}
    # Reads the csv file chuck by chuck - a chunk is 1 mb
    for chunk in pd.read_table(file_path, sep='\t', chunksize=1024):
        for elm in np.asarray(chunk)[0:, 6]:
            if elm not in end_year:
                end_year[elm] = 1
            else:
                end_year[elm] += 1
    # Removes the key \\N
    end_year.pop("\\N")
    year = max(end_year, key=end_year.get)
    print("The year where most series ended was: ", year)
    #Plot the graph
    plt.bar(end_year.keys(), end_year.values(), width=0.3)
    plt.title('Amount of series that ended each year')
    plt.xticks(rotation=70, fontsize=5)
    plt.xlabel('Year')
    plt.ylabel("Amount of series")
    plt.tight_layout()
    plt.text(year, end_year[year], str(year), horizontalAlignment="center")
    plt.show()
    plt.close()


def question_3(file_path):
    dict_genres = {}
    # Reads the csv file chuck by chuck - a chunk is 1 mb
    for chunk in pd.read_table(file_path, sep='\t', chunksize=1024):
        for elm in np.asarray(chunk)[0:, 7:9]:
            genres = str(elm[1]).split(",")
            try:
                runtime = int(elm[0])
            except ValueError:
                runtime = 0
            for genre in genres:
                if genre not in dict_genres:
                    dict_genres[genre] = runtime
                else:
                    if dict_genres[genre] < runtime:
                        dict_genres[genre] = runtime
    #Removes the key \\N
    dict_genres.pop("\\N")
    genre = max(dict_genres, key=dict_genres.get)
    print("The genre which has the movie/serie with the longest running time is ",genre)


def question_4(file_path):
    genre_dict = {}
    # Reads the csv file chuck by chuck - a chunk is 1 mb
    for chunk in pd.read_table(file_path, sep='\t', chunksize=1024):
        for elm in np.asarray(chunk)[0:,8]:
            genres = str(elm).split(",")
            for genre in genres:
                if genre not in genre_dict:
                    genre_dict[genre] = 1
                else:
                    genre_dict[genre] += 1
    # Removes the key \\N
    genre_dict.pop("\\N")
    genre = max(genre_dict, key=genre_dict .get)
    print("The genre the covers the most movies is: ",genre)


def question_5(file_path):
    adult_runtime = {'runtime': 0, 'amount_of_movies': 0}
    # Reads the csv file chuck by chuck - a chunk is 1 mb
    for chunk in pd.read_table(file_path, sep='\t', chunksize=1024):
        dd = chunk.as_matrix()
        mask = (dd[:, 4] == 1)
        for i in dd[mask][:,7]:
            # only if the runtime is not \\N
            if i != '\\N':
                adult_runtime['runtime'] += int(i)
                adult_runtime['amount_of_movies'] += 1
    print("The average runtime of adult movies is: ",
          int(adult_runtime['runtime']/adult_runtime['amount_of_movies']),
          " min")


def main(file_path):
    question_1(file_path)
    question_2(file_path)
    question_3(file_path)
    question_4(file_path)
    question_5(file_path)


if __name__ in "__main__":
    try:
        #Read the sys argeument at index 1
        main(sys.argv[1])
    except IndexError:
        #If the argument can be found we download the file.
        main(webget.download("https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/Assignment_4/title.basics.tsv"))
