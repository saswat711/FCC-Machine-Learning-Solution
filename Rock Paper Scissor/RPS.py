# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random
from collections import Counter

victory = {"R":"P","P":"S","S":"R"} #for having the victory values
sol = {} # dictonary of solution to story values
def player(prev_play, opponent_history=[]):
  global sol
  n = 3 # to wait for the turns have to change based on perfecting
  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R" # default guess value

  if len(opponent_history)>n:
    inp = "".join(opponent_history[-n:]) # to join list as a string with:  for the dictonary key from values in index n starting from last

    if "".join(opponent_history[-(n+1):]) in sol.keys(): # to see if the dictionary have the certain key
      sol["".join(opponent_history[-(n+1):])]+=1 # if yes than adding the value 1 to it
    else:
      sol["".join(opponent_history[-(n+1):])]=1
      # else adding the key and value in the diconary

    possible =[inp+"R", inp+"P", inp+"S"] # to get possible values list

    for i in possible:
      if not i in sol.keys(): # check if value in possible is not the sol dictonary key
        sol[i] = 0

    predict = max(possible, key=lambda key: sol[key]) # to predic geting the max from possible values and sol 
     #dictonary key
    
    # value fo rthe predicted value
    guess = victory[predict[-1]]
  return guess