import random

def roll() :
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)
  return roll

while True :
  players_number = input("Enter the number of players for this turn (2 - 4): ")
  if players_number.isdigit():
    players_number = int(players_number)
    if 2 <= players_number <= 4:
      break
    else:
      print("Invalid number of players. Please enter a number between 2 and 4.")
  else :
    print("Invalid input. Please enter a number between 2 and 4")

max_score = 50
players_score = [0 for _ in range(players_number)]


while max(players_score) < max_score :
  
  for player_index in range(players_number):
    print("\nPlayer number :", player_index + 1, "turn has just started!")
    print("\nYour total score is ", players_score[player_index], "\n")
    current_score = 0

    while True:
      start_rolling = input("Would you like to roll the dice (y): ").lower()
      if start_rolling != "y":
        break

      value = roll()
      if value == 1:
        print("You rolled 1! Your turn is done.")
        players_score[player_index] = 0
        current_score = 0
        break
      
      else :
        current_score += value
        print("You rolled ", value)

      print("Your score is ", current_score)
    
    players_score[player_index] += current_score
    print("Your total score is ", players_score[player_index])

max_score = max(players_score)
wining_index = players_score.index(max_score)
print("Player number : ",wining_index + 1, " is the winner with a score of ", max_score)
