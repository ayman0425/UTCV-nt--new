print ("You enter a dark room with two doors.  Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake.  What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")
    print ("3. Play dead.")

    bear = input("> ")

    if bear == "1":
        print ("The bear eats you.  Game Over!")
    elif bear == "2":
        print ("It's a Grizzly bear! The bear eats you. Game Over!")
    else:
        print ("The bear smells you and runs away. Good Job!")

elif door == "2":
    print ("You see a hall full of treasure. What do you do?")
    print ("1. Take as much treasure as you can.")
    print ("2. Take one gold coin and run.")
    print ("3. Walk through and don't take anything.")

    treasure = input("> ")

    if treasure == "1" or treasure == "2":
        print ("A dragon wakes up and burns you to a crisp.  Game Over!")
    else:
        print ("You survive to live another day.  Good job!")

else:
    print ("You stumble around and fall into a deep well. Game Over!")
