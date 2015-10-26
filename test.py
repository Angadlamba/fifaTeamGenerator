from random import sample
index = [0,1,2]
count = 0
players = ["a","b","c","d","e","f"]
teams = [[],[],[]]
for i in range(6):
	sorting_number = sample(index,1)
	teams[sorting_number[0]].append(players[i])
	print sorting_number
	print "\ncount : %d\n" % count
 	if count >= 2:
		index = [0,1,2]
		count = 0
	else:					
		count += 1
		index.remove(sorting_number[0])
		print index