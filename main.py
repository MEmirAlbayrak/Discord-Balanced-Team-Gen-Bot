import discord
from discord.ext import commands 
from numpy import true_divide
import pandas as pd
from tabulate import tabulate
import random

bot = discord.Client()
list_names = []
list_lv = []
team_one=pd.DataFrame()
team_two=pd.DataFrame()


@bot.event
async def on_ready():	
	
	guild_count = 0
	for guild in bot.guilds:		
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):

	# Make list to the comming message
	words = message.content.split(" ")
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
			# print("i = ", i )
			# print(isStable ," is stable")
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


		await message.channel.send("Team 1")		
		await message.channel.send(tabulate(team_one, headers='keys', tablefmt='psql',showindex=False))
		# await message.channel.send(team_one.sum())
		await message.channel.send("---------------------------")	
		await message.channel.send("Team 2")	
		await message.channel.send(tabulate(team_two, headers='keys', tablefmt='psql',showindex=False))
		# await message.channel.send(team_two.sum())

		team_one.drop(team_one.index, inplace=True)
		team_two.drop(team_two.index, inplace=True)
		list_lv.clear()
		list_names.clear()

bot.run("Your Token")