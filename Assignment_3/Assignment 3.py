import webget
import pandas as pd
from glob import glob

# Solutions to TEAM: Naughty Solution | Ali Khazendar, Casper Emde Christensen, Stephan Pedersen, Nicklas Vikke


# Setting up usable csv file
webget.download('https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv')

filed = glob('.\\complete.csv*')
complete_csv = filed[0]

data = pd.read_csv(complete_csv)

#See labels for later use
print(data.dtypes)


##
#Question 1: The 3 most expensive teams and the 3 cheapest teams according to player value.
##

df = data.groupby('club')['eur_value'].sum()
print(df.sort_values(ascending=False))


##
#Question 2: Which nationality is the most frequent amongst all players
##

sf = data.groupby('nationality').count()

print(sf.sort_values(['name'],ascending=False))

##
#Question 3: What is the difference between the release clause and the value of top 10 most valuable players
##

data['rel_value_diff'] = data['eur_release_clause'] - data['eur_value']
asc_valued_players = data.iloc[:, [1, 16, 18, 185]].sort_values(['eur_value'], ascending=False).head(10)
print(asc_valued_players)

##
#Question 4: What is the frequency of age, height and weight for all players
##

print(data.groupby(['age'])['age'].count())
print(data.groupby(['height_cm'])['height_cm'].count())
print(data.groupby(['weight_kg'])['weight_kg'].count())


##
#Question 5: How big is the average difference between value and wage of the players
##

data['val_wage_diff'] = data['eur_value'] - data['eur_wage']
val_wage = data.iloc[:, [186]]
#print(val_wage.sum() % val_wage.count()) #Modolus
#print(val_wage.sum() / val_wage.count()) #Division 
print(val_wage.sum() // val_wage.count()) #Division to int - no decimals 
