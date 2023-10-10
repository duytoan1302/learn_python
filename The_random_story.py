import random
woman = ["Scientist","The queen","The docter","The giant people"]
man = ["The police" ,"The artits","The jack the killer"]
place = ["In the mars","In the market","In the dark cave"]
sheWore = ["The dress","The paper bag","The skirt"]
heWore = ["The jumper","The shark costume","The dinosaur"]
womansays = ["'Who are you'?","'What your name'?","'How old are you'?"]
mansays = ["'bip bip'","'What is your job'?'","'Why are you here'?"]
Theworldsays = ["'The silly story!'","'The bad story!'"]
while True:
    print(random.choice(woman),"see", random.choice(man),random.choice(place))
    print("She wear",random.choice(sheWore))
    print("He wear",random.choice(heWore))
    print("Woman says", random.choice(womansays))
    print("Man says", random.choice(mansays))
    print("The world says", random.choice(Theworldsays))
    print()
    input("press enter to play again")
    print()
