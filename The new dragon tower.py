import random

exitChoice = "nothing"
while exitChoice!="exit":
    print("you are in the dark room in the dangerous tower")
    print("have four door.please choose one door to explore")
    
    playerChoice = input("please choose 1,2,3 or 4")
    if playerChoice == "1":
        print("You found the treasure room.You is rich!")
        print("You are win the game.the game is over")
    elif playerChoice =="2":
        print("The door is open.The angry monter run out and hit you in the head with a mace")
        print("You are lose.The game is over.")
    elif playerChoice == "3":
        print("you walk to the room and see the dragon is sleep.")
        print("you can:")
        print("1) try to steal the dragon's gold.")
        print("2)try to walk around the dragon to get to the door.")
        
        dragonchoice = input("Fill in 1 or 2")
        if dragonchoice == "1":
            print("The dragon is wake up and eat you.Wow it yummy!")
            print("You are lose.The game is over")
        elif dragonchoice == "2":
            print("you are walk around the dragon but the dragon is not wake up and you are outside the tower.Hello the sunlight!")
            print("you are win!The game is over")
        else:
            print("Sory you don't choose 1 or 2")
    
    elif playerChoice == "4":
        print("The room you walk have a sphinx.")
        print("Sphinx froce you to guess the number it think to,the number is 1 to 10.")
        number = int(input("what you guess?"))
        if number == random.randint(1,10):
            print("sphinx shout becus you guess true.")
            print("sphinx get you out.")
            print("You win the game.The game is over.")
        else:
            print("sphinx says your guess is false.")
            print("you is the prisoner always.")
            print("you lots the game.The game is over.")
            
    else: 
        print("Sory you are not choose 1,2,3 or 4!")
    
    print("Let s tart again to explore this dragon tower")
    exitChoice = input("press Enter to play again or write exit to get out the game.")
