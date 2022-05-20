import time
import random

       
def print_pause(message):
    print(message)
    time.sleep(2)
    
    
def intro(villain, weapon):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that " + villain + " is somewhere around " 
                "here, and has been terrorizing this land and nearby "
                "countries with bloody regime.")
    print_pause("In front of you is a red kremlin.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) " + weapon + ".\n")


def play_again():
    response = input("Would you like to play again? (y/n)\n").lower()
    if "y" in response:
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif "n" in response:
        print_pause("Thanks for playing! See you next time.\n"
                    "Make LOVE not war")
    else:
        play_again()


def choice(list, villain, weapon):
    response = input("(Please enter 1 or 2).\n")
    if "1" in response:
        kremlin(list, villain, weapon)    
    elif "2" in response:
        cave(list, villain, weapon)
    else:
        choice(list, villain, weapon)

    
def field(list, villain, weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice(list, villain, weapon)
        
    
def cave(list, villain, weapon):
    print_pause("You peer cautiously into the cave.")
    if "sword" in list:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Truth and Peace!")
        print_pause("You discard your silly old " + weapon + 
                    " and take the sword with you.")
        list.append("sword")
    print_pause("You walk back out to the field.\n")
    field(list, villain, weapon)


def kremlin(list, villain, weapon):
    print_pause("You approach the door of the red kremlin.")
    print_pause("You are about to knock when the door " 
                "opens and out steps " + villain + ".")
    print_pause("Eep! This is " + villain + "'s red kremlin!")
    if "sword" in list:
        print_pause("As " + villain + " moves to attack, " 
                    "you unsheathe your new sword.")
        print_pause("The Sword of Truth and Peace shines "
                    "brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("But " + villain + " takes one look at "
                    "your shiny new sword and runs away!")
        print_pause("You have rid these lands of " + villain + "'s bloody regime.")
        print_pause("Light won over darkness. "
                    "You are victorious!")
        play_again()
    else:
        print_pause(villain + " attacks you!")
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny " + weapon + ".")
        fight(list, villain, weapon)


def fight(list, villain, weapon):
    response = input("Would you like to (1) fight or (2) run away?\n")
    if "1" in response:
        print_pause("You do your best...")
        print_pause("but your " + weapon + " is no match for " + villain + ".")
        print_pause("You have been defeated!")
        print_pause("GAME OVER\n")
        play_again()
    elif "2" in response:
        print_pause("You run back into the field. Luckily, " 
                    "you don't seem to have been followed.")
        field(list, villain, weapon)
    else:
        choice(list, villain, weapon)


def play_game():             
    list = []
    villain = random.choice(['Putin', 'Tsar Putin', 'dictator'])
    weapon = random.choice(['dagger', 'stone', 'stick'])
    intro(villain, weapon)
    field(list, villain, weapon)
        
    
if __name__ == "__main__":
    play_game()
