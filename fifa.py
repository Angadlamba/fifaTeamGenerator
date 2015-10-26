""" Programs generates football teams by distributing players on the basis of their
	1. overall stats 
	2. position"""

from sys import argv
from random import sample

script, filename, n = argv						# retrieving file and number of teams from command-line

players = open(filename, "r")   			    # 'players' is the file containing player data

teams = [[],[],[]]  							# creating 'n-teams'.
player_by_position = [[],[],[],[]]
player_data = []								# contains all players data

def sort_player(player_data, length):
	for i in range(length):
		for j in range(length):
			if (player_data[j][2] < player_data[i][2]):
				temp = player_data[j]
				player_data[j] = player_data[i]
				player_data[i] = temp

def teaming(players, length):
	index = [0,1,2]
	count = 0
	for i in range(length):
		sorting_number = sample(index,1)
		teams[sorting_number[0]].append(players[i])
		if count >= 2:
			index = [0,1,2]
			count = 0
		else:					
			count += 1
			index.remove(sorting_number[0])



for line_counter, i in enumerate(players):									# parsing the 'players' file
	player_data.append(i.split())    										# cleaning data
	player_data[line_counter][2] = player_data[line_counter][2][:2]			 

no_player = len(player_data)

sort_player(player_data, no_player)			# sorting players on the basis of their overall stats

for i in range(no_player):
	if player_data[i][1] == "f":
		player_by_position[0].append(player_data[i])
	elif player_data[i][1] == "m":
		player_by_position[1].append(player_data[i])
	elif player_data[i][1] == "d":
		player_by_position[2].append(player_data[i])
	elif player_data[i][1] == "g":
		player_by_position[3].append(player_data[i])	

teaming(player_by_position[0], len(player_by_position[0]))
teaming(player_by_position[1], len(player_by_position[1]))
teaming(player_by_position[2], len(player_by_position[2]))
teaming(player_by_position[3], len(player_by_position[3]))


print teams[0], "\n\n"
print teams[1], "\n\n"
print teams[2]

players.close()