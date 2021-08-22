
# Author: Le Nguyen Thanh Toan  
# Email Id: acemarco9@gmail.com

#
import blackjack

def output_player(player):
    player_name = player.get_name() #name of user
    player_hand = player.get_hand() #cards in user's hand 
    player_hand_value = player.get_hand_value()  #value of each card in user's hand
    alternative_player_hand = []
    for card in player_hand:
        value = card.get_value()
        if value == 1:   #convert 1 to Ace
            value = "Ace"  
        else:
            value = str(value)
        suit  = str(card.get_suit())
        alternative_player_hand.append(value+" "+suit)
    alternative_player_hand = ", ".join(alternative_player_hand)
    print(player_name+"'s hand: ", alternative_player_hand)
    print(player_name, "Total:", player_hand_value)
    
def play_game(player, dealer, deck):
    for time in range(2):  #2 cards for player and 2 cards for dealer
        player.hit_me(deck.draw_card()) 
        dealer.hit_me(deck.draw_card())
    output_player(player)
    output_player(dealer)
    
def player_turn(player, deck):
    decision = input("hit or stand? ")          #user enter decision
    while decision != "hit" and decision != "stand":
        print("ERROR, only enter 'hit' or 'stand'")
        decision = input("hit or stand? ")
    if decision == "stand":         #if user want to stand, end the function here
        return 
    while decision == "hit" and player.is_bust() == False: #if user is eligible for being hit
        new_card = deck.draw_card()         #get him new card
        player.hit_me(new_card)
        output_player(player)
        if player.is_bust() == False:   #if user still doesnt bust, ask him again (reuse this function)
            return player_turn(player, deck)
        else: return    #if user busts after getting a new card, he lose, end the function


def dealer_turn(dealer, deck):
    while dealer.get_hand_value() < 17: 
        dealer.hit_me(deck.draw_card())
        output_player(dealer)
        
        

def read_high_scores(filename, names, scores):
    file = open(filename, "r") #open filename to read
    all_lines = file.readlines()    #readlines() will return a list contains all lines in file
    for line in all_lines:
        find_space = line.find(" ")
        player_name = line[0:find_space]
        player_score = line[find_space + 1:len(line)-1]   #the line end with \n, the end point is before \n
        if line == all_lines[len(all_lines)-1]:  #the last line does not end with \n
            player_score = line[find_space + 1: len(line)] #the end point is the last character
        names.append(player_name)
        scores.append(int(player_score))
    file.close()    #close the file

def get_high_score_index(player, score, scores):
    for i in range(len(scores)):  #get the first item in scores list that lower than score
        if scores[i] <= score:
            return i  #end function if got it 
    if len(scores) < 5:  #if cannot find it and the length of scores list smaller than 5
        return len(scores)  #return length of scores list
    else: return -1     #else return -1
    
def insert_high_score(name, score, pos, names, scores):
    names.insert(pos, name) #insert name 
    scores.insert(pos, score) #insert score
    if len(names) > 5:    #if the ranking larger than 5, remove the last one
        names.remove(names[len(names)-1])
        scores.remove(scores[len(scores)-1])
    else:
        print("New high score!")
        

def output_high_scores(names, scores):
    for index in range(len(names)):
        print(str(names[index])+" "+str(scores[index]))
        
    
def write_high_scores(filename, names, scores):
    file = open(filename, "w")
    for index in range(0, len(names), 1):
        file.write(names[index]+" "+str(scores[index])+"\n")
    file.close()

    
print("Welcome to Blackjack")

deck = blackjack.Deck()
dealer = blackjack.Player("Dealer")

# Write your main program code here
name = input("Enter your name: ")  #allow user enter their name
while len(name) == 0 or name.find(" ") != -1:         #if name contain space
    print("ERROR Must only be one word")
    name = input("Enter your name: ") #enter the name again

player = blackjack.Player(name) # Take input for the player name
deck = blackjack.Deck()
dealer = blackjack.Player("Dealer")
play = "yes"
while play == "yes":
    player.reset_hand()
    dealer.reset_hand()
    deck.reset()
    deck.shuffle()
    play_game(player, dealer, deck)
    player_turn(player, deck)
    if player.is_bust() == True:  #if player busts the dealer will win immediately
        print(player.get_name(), "busts!")
        print("Dealer wins!")
        dealer.win()
        player.lose()
    else:   #if player doesnt bust, it is dealer's turn now
        dealer_turn(dealer, deck)
        if dealer.is_bust() == True or player.get_hand_value() > dealer.get_hand_value(): #how can player win?
            print(name,"wins!")         #if player doesnt bust and player > dealer --> player win
            player.win()
        elif dealer.get_hand_value() > player.get_hand_value() and dealer.is_bust() == False: #how can dealer win? 
            print("Dealer wins!")   #if dealer doesnt bust and dealer > player --> dealer wins
            dealer.win()
        else:
            print("Draw")
    play = input("Would you like to play again (yes/no): ")
    while play != "yes" and play != "no":
        print("Error, only enter 'yes' or 'no'!")
        play = input("Would you like to play again (yes/no): ")
names = []
scores = []
read_high_scores("highscores.txt", names, scores)
high_score_index = get_high_score_index(player, player.get_score(), scores)
if high_score_index > -1:
    insert_high_score(name, player.get_score(), high_score_index, names, scores)
print()
print("|","-"*5+"High Scores"+"-"*5,"|")
for i in range(len(names)):
    print("|", format(names[i], "<16s"), format(scores[i], ">4d"), "|")
print("|", "-"*21, "|")
print()
print("Goodbye")
write_high_scores("highscores.txt", names, scores)



 
