import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    return roll

while True:
    players = input("Enter the number of players(2-4)? ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Please enter a valid number")
            continue
    else:
        print("Invalid Choice ..Please try again Sir")
        continue
max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        score_counter = 0
        print(f'\nPlayer {player_idx + 1} turn has just started with  a score of:{score_counter}\n')
        while True:
         ask = input("Do you want to roll the dice  (y)? ").lower()
         if ask != "y":
          break
         value = roll()
         if value == 1 :
          print("You dice a 1!.Your turn is done")
          score_counter = 0
          break
         else:
          print(f"You dice a {value}")
          score_counter += value
         print(f"Your  score is {score_counter}")
        players_score[player_idx] += score_counter
        print(f"The total score for the player {player_idx + 1} is {players_score[player_idx]} ")
max_scores = max(players_score)
winning_idx = players_score.index(max_scores)
print(f"Player no {winning_idx + 1} has won the game with a score of {max_scores}")
        

    
