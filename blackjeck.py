import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_game = True
def game():
  input("do you want to play? y or n: ")
  if input == "y":
    continue_game = True
  if input == "n":
    continue_game = False
  def deal_card_for_player(cards):
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    print(f"your 2 cards are: {first_card}, {second_card}")
    third_card_q = input("do you want another card? y od n: ")
    third_card = 0
    if third_card_q == "y":
      third_card += random.choice(cards)
      print(f"you drew {third_card}")
    sum_player_cards = first_card + second_card + third_card
    return sum_player_cards
  
  def deal_cards_for_computer(cards):
    cumputer_first_card = random.choice(cards)
    print(f"the computer drow {cumputer_first_card}")
    cumputer_second_card = random.choice(cards)
    sum_computer_cards = cumputer_first_card + cumputer_second_card
    if sum_computer_cards < 17:
      cumputer_third_card = random.choice(cards)
      sum_computer_cards += cumputer_third_card
      return sum_computer_cards
    else:
      return sum_computer_cards

  player_cards_sum = deal_card_for_player(cards)
  comuter_cards_sum = deal_cards_for_computer(cards)

  def the_results(player_cards_sum, comuter_cards_sum):
    players_score = player_cards_sum
    computer_score = comuter_cards_sum
    print(f"your final hand is {players_score}")
    print(f"the computers final hand is{computer_score}")
    if players_score == 21:
      print("you win")
      game()
    if players_score > 21:
      print("you lose")
      game()
    if computer_score == 21:
      print("you lose")
      game() 
    if computer_score > 21:
      print("you win")
      game()
    if computer_score > players_score:
      print("you lose")
      game() 
    if computer_score < players_score:
      print("you win")
      game()
    if computer_score == players_score:
      print("drow")
      game()
  the_results(player_cards_sum, comuter_cards_sum)

while continue_game:
  game()



