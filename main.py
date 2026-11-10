print("Find your dog")
money = 10
game_running = True

while game_running:
    print("You wake up in the morning and your dog is missing because the door was left open. What do you choose to do?")
    print("1.Look through your house")
    print("2.Look in the nearby woods")
    print("3.Hire an investigator for money=20 to find your dog")
    choice1 = input("choice? ")
    if choice1 == "1":
        print("Congrats")
        print("You searched around your house and your dog was actually under your bed")
        print("the end: try again now")
        game_running = False
    if choice1 == "2":
        print("Congrats")
        print("You got yourself lost in the woods, and now don't have to worry about finding your dog anymore")
        print("the end: try again now")
        game_running = False
    if choice1 == "3":
        print("Congrats")
        print("Now you need to start working for money because you are broke. What do you choose to do?")
        print("1.start your own business")
        print("2.sell lemonade at the corner of your block")
        print("3.try to rob a bank")

    choice2 = input("Choice? ")

    if choice2 == "1":
        print("congrats")
        print("after 3 years you have enough money from selling homemade stickers.")
        print("you finally hire an investigator who leads you to the woods near your home and finds the bones of what used to be your dog")
        print("the end: try again now")
        game_running = False
    if choice2 == "2":
        print("congrats")
        print("your dog smelled the lemonade and came back to you to beg for food!") 
        print("the end: try again now")   
        game_running = False
    if choice2 == "3":
        print("congrats")    
        print("your robbery went horribly wrong and you are sentenced to life sentence in jail")
        print("you will now never have to worry about finding your dog ever again")
        print("the end: try again now")
        game_running = False
