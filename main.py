from numpy import true_divide
import pandas as pd
from tabulate import tabulate
import random

list_names = []
list_lv = []
team_one=pd.DataFrame()
team_two=pd.DataFrame()

def on_message(message):

	# Make list to the comming message
	words = message.split(" ")
	if(words[0] == "!vs"):
		for i in range(len(words)):
			if(i % 2 == 1):
				list_names.append(words[i])
			if(i != 0 and i%2==0):
				list_lv.append(words[i])
    

		# Set var(s)
		df = pd.DataFrame(list(zip(list_names, list_lv)), columns =['Name', 'Level'])

		convert_dict = {'Level': int} 
		df = df.astype(convert_dict) 
		df=df.sort_values(by=['Level'])
		df=df.reset_index(drop=True)
		isStable = 0

		# Put values at the DataFrame
		for i, row in df.iterrows():
			print("i = ", i )
			print(isStable ," is stable")
			if i % 2 == 0:
				team_one.loc[i,'Player']=(row['Name'])
				team_one.loc[i,'Rank']=(row['Level'])
			if i%2 == 1:
				team_two.loc[i,'Player']=(row['Name'])
				team_two.loc[i,'Rank']=(row['Level'])
				if team_one.loc[i-1,'Rank'] < team_two.loc[i,'Rank']:
					isStable += 1
					if isStable%2 == 0:
						temp4 = team_two.loc[i,'Player']
						temp3 = team_one.loc[i-1,'Player']
						temp = team_one.loc[i-1,'Rank']
						temp2= team_two.loc[i,'Rank']
						team_one.loc[i-1,'Rank'] = temp2
						team_two.loc[i,'Rank'] = temp
						team_one.loc[i-1,'Player'] = temp4
						team_two.loc[i,'Player'] = temp3



		# Random switch places between player who are equal by level
		for i in range(len(team_one)):
				for j in range(len(team_two)):
					if(team_one.iloc[i,1] - team_two.iloc[j,1] == 0):
						rnd = random.randint(1,2)
						if rnd == 1:
							temp4 = team_two.iloc[j,0]
							temp3 = team_one.iloc[i,0]
							temp = team_one.iloc[i,1]
							temp2= team_two.iloc[j,1]

							team_one.iloc[i,1] = temp2
							team_two.iloc[j,1] = temp
							team_one.iloc[i,0] = temp4
							team_two.iloc[j,0] = temp3


		print("Team 1")		
		print(tabulate(team_one, headers='keys', tablefmt='psql',showindex=False))
		print(team_one.sum())
		print("---------------------------")	
		print("Team 2")	
		print(tabulate(team_two, headers='keys', tablefmt='psql',showindex=False))
		print(team_two.sum())

		team_one.drop(team_one.index, inplace=True)
		team_two.drop(team_two.index, inplace=True)
		list_lv.clear()
		list_names.clear()

on_message("!vs a 5 b 4 c 3 d 2 e 5 f 1 g 5 h 4 j 3 t 2")
