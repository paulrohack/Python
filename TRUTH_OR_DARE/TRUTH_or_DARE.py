<<<<<<< HEAD:TRUTH_OR_DARE/TRUTH_or_DARE.py
import random

player = (input("[T]ruth or [D]are	:"))
player = player.upper()
truth = "T"
dare = "D"
print('\n')
if player == truth:
	txt = open('GAMES\\TRUTH OR DARE\\DARE.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
elif player == dare:
	txt = open('GAMES\\TRUTH OR DARE\\TRUTH.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
else:
	print("nope")


 





=======
import random

player = (input("[T]ruth or [D]are	:"))
player = player.upper()
truth = "T"
dare = "D"
print('\n')
if player == truth:
	txt = open('GAMES\\TRUTH OR DARE\\DARE.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
elif player == dare:
	txt = open('GAMES\\TRUTH OR DARE\\TRUTH.txt')
	words = txt.readlines()
	print(words[random.randint(0, len(words)-1)])
else:
	print("nope")


 





>>>>>>> 1716e3ac153e6b6805d02dd7397be643a7ac4293:GAMES/TRUTH OR DARE/TRUTH_or_DARE.py
