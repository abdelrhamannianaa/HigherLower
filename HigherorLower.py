import random
from HigherLowerHelper import data, logo, vs

def populate():
    """Populates a choice with a option from the data list"""
    return random.choice(data)
def print_layout(a,b,score):
    """Makes sure the entries aren't equal"""
    """prints the layout of the game every turn"""
    if(a==b):
        b = populate()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}") 
    print(f"Compare A, {a['name']}, a/an {a['description']}, from {a['country']} ")
    print(vs)
    print(f"Compare B, {b['name']}, a/an {b['description']}, from {b['country']} ")

score = 0
player_A = populate()
player_B = populate()
print_layout(player_A,player_B,score)
    
game_over = False
while not game_over:
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_A['follower_count'] > player_B['follower_count']:
        if answer == "A":
            score+=1
            player_B = populate()
            print_layout(player_A,player_B,score)
        elif answer == "B":
            game_over = True
            print(f"You're wrong! Final score: {score}")
    if player_B['follower_count'] > player_A['follower_count']:
        if answer == "B":
            score+=1
            player_A = player_B
            player_B = populate()
            print_layout(player_A,player_B,score)
        elif answer == "A":
            print(f"You're wrong! Final score: {score}")
            game_over = True
    
        
        
    





