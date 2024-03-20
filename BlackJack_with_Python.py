import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_card = []
user_card = []


def random_card():
  return random.choice(cards)


for i in range(2):
  user_card.append(random_card())
  computer_card.append(random_card())


def calculate_score(user_list):
  if 11 in user_list and 10 in user_list:
    return 0
  if 11 in user_list and sum(user_list) > 21:
    user_list.remove(11)
    user_list.append(1)
  return sum(user_list)


# print(calculate_score(user_card))
# print(user_card)
game_situation = True
while game_situation:
  user = calculate_score(user_card)
  computer = calculate_score(computer_card)
  print(f"your score is {user}")
  if user == 0 or computer == 0:
    print("End Game")
    game_situation = False
  elif user < 21 and computer < 21:
    new_card = input("Do you want take a new card ? 'y' or 'n' : ")
    if computer < 17:
      computer_card.append(random_card())
    if new_card == 'y':
      user_card.append(random_card())
    else:
      game_situation = False
      print("End Game")
  else:
    game_situation = False
    print("End Game")


def compare():
  if user == 0:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("User Won!")
  elif computer == 0:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("Computer Won!")
  elif user == computer:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("Draw!")
  elif user > 21:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("Computer Won!")
  elif computer > 21:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("User Won!")
  elif user > computer:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("User Won!")
  elif computer > user:
    print(f"your score is {user}")
    print(f"deal score is {computer}")
    print(f"Your cards : {user_card}")
    print(f"deal cards : {computer_card}")
    print("Computer Won!")


compare()
