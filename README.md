# Random Balanced Team Generator Bot for Discord

## :ghost: What it does ?  
This bot splits all players into two teams according to their ranking. The purpose is to generate 2 teams with equal power (fair) to compete in a game.
The algorithm sorts all players by their level/ranking and puts in order and adjusts power ranking as close as possible. Then program adjusts the teams and mixes randomly.

## Discord lib installation
```console
pip install -U discord.py discord-ext-typed-commands numpy pandas tabulate
```

## :wrench: Usage :
It is advised to use the ranking between one and five.
```
!vs [Player 1 Name] [Player 1 Rank] [Player 2 Name] [Player 2 Rank]...
```

![alt text](https://i.imgur.com/fmIvlTk.png)

