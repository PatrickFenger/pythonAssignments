## Dataset

https://www.kaggle.com/mousehead/songlyrics/data

## Dependencies & Info

The following dependencies should be intalled on your system, either via conda install of pip install through your terminal:

pandas\n
webget/n
collections
re
matplotlib.pyplot

Clone the project from our repository, use the "cd" command to get into our "Assignment_6" folder. From here run the project from command prompt by typing "python run.py"

Upon running the file, the program will conduct a download process to retrive the neccesary dataset & produce answers for the questions listed below.

## Questions

1. What is the most used words in the songs?
2. How many times are each word repeated in a song? (Or        perhaps - what song repeats the top 4 repeated words        the most? - finds the most repetitive song)
3. What song uses the word "X" the most time? (X meaning a     specific word, choose your own!)
4. What is the average number of words per song?
5. Show the distribution of number of words in the songs.      (Example: how many songs have 5-10 words, 10-20 words)


## Answers:

### Q1:

To make the answer a bit more solid we invalidated the following words:
"THE", "I", "YOU", 'AND', 'TO', 'A', 'ME', "T", "S", 'MY', 'IN', 'IT', 'M', "ON", 'THAT', 'OF', 'YOUR', 'ALL', 'FOR', 'WE', 'IS', 'BE', 'KNOW', 'UP', 'LIKE', 'BUT', 'GET', 'SO', 'WITH'

After removing these words, we can conclude tat the most used word is: "Love"

### Q2:

For this question we chose a song called "It's so cool". The amount of words in the song is 337

### Q3: What song uses the word "X" the most times?

Here the word was up for grasp. We chose the word "Love" and the song with that word being used the most was "It's so cool"

### Q4: What is the average number of words per song?

The average number of words per song is 220.13.

### Q5: Show the distribution of number of words in the songs.

Below we provided a visual presentation.

![alt text]https://github.com/PatrickFenger/pythonAssignments/blob/master/Assignment_6/Figure_1.png


