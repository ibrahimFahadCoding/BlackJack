
#main.py 

import random

PC = []
DC = []

pchoice = ""
dchoice = 0

pCards = 0
dCards = 0

print("Number Card Game")
print()

			
		
ranP = random.randint(2,10)
ranP2 = random.randint(2,10)
PC.append(ranP)
PC.append(ranP2)
pCards = ranP + ranP2

print("Here is your hand:")
print(PC)
print("Cards: " + str(pCards))
dchoice = 5
while dchoice != 1:
  if dchoice != 1:
  	if pCards > 21:
  		print("The Dealer Won!")
  		break
  	if dCards > 21:
  		break
  	pchoice = input("Enter (S/H) to stay or hit: ")
  	if pchoice == "H":
  		ranP = random.randint(2,11)
  		pCards += ranP
  		PC.append(ranP)
  		print("Here is your hand:")
  		print(PC)
  		print("Cards: " + str(pCards))
  	if pchoice == "S":
  		ranD = random.randint(2,11)
  		ranD2 = random.randint(2,11)
  		DC.append(ranD)
  		DC.append(ranD2)
  		dCards = ranD + ranD2
  		print("Here is the dealer's hand:")
  		print(DC)
  		print("Cards: " + str(dCards))
  		if dCards > 21:
  			print("You Won!")
  			break 
  		dchoice = random.randint(0,1)
  		while dchoice == 0:
  			ranD = random.randint(2,11)
  			dCards += ranD
  			DC.append(ranD)
  			print("Here is the dealer's hand:")
  			print(DC)
  			print("Cards: " + str(dCards))
  			if dCards > 21:
  				print("You Won!")
  				break 
  			dchoice = random.randint(0,1)
  		if dchoice == 1:
  		  if dCards > pCards:
  		    print("The Dealer Won")
  		    break
  		  elif pCards > dCards:
  		    print("You Won!")
  		    break
  		  else:
  		    print("Tie!")
  		    break
      			
 
	
				
		
	

	
