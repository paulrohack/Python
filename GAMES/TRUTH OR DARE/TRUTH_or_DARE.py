import random

player = (input("[T]ruth or [D]are	:"))
player = player.upper()
truth = "T"
dare = "D"
print('\n')
if player == truth:
	txt = open('C:\\Users\\paulr\\Documents\\Projects\\My_Projects_All\\Projects-Python-master\\Game_s\\TRUTH.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
elif player == dare:
	txt = open('C:\\Users\\paulr\\Documents\\Projects\\My_Projects_All\\Projects-Python-master\\Game_s\\DARE.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
else:
	print("nope")


 





