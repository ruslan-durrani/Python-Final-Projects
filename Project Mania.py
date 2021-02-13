import random                        #Using random modul
def EXIT():
    quit()
def main_adv_game_menu():
    print("WELCOME TO ADVENTURE WORLD! ")
    name=input("WHAT IS YOUR NAME:  ")
    age=eval(input("WHAT IS YOUR AGE:  "))
    print("HELLO",name,"YOU ARE",age,"YEARS OLD.")

    health=10

    if age>=18:
        print("LETS PLAY! YOU ARE OLD ENOUGH TO PLAY THIS GAME.....")
   
        wants_to_play=input("DO YOU WANT TO PLAY THIS GAME? ").lower()
        if wants_to_play=="yes":
            print ("YOU ARE STARTING WITH",health,"HEALTH") 
            print("LET'S PLAY!")

            left_or_right=input("FIRST CHOICE... left or right (left/right)? ")
            if left_or_right=="left":
                ans=input("NICE, YOU FOLLOW THE RIGHT PATH AND REACHED A LAKE...DO YOU SWIM ACROSS OR GO AROUND(across/around)? ")

                if ans=="around":
                    print("YOU WENT AROUND AND REACHED THE OTHER SIDE OF THE LAKE.")
                
                elif ans=="across":
                    print("YOU MANAGED TO GET ACROSS,BUT WERE BIT BY A FISH AND LOST 5 HEALTH.")

                    health-=5

                ans=input("YOU NOTICE A HOUSE AND A RIVER.WHICH WAY DO YOU GO TO(river/house)? ")
                if ans=="house":
                    print("YOU GO TO THE HOUSE AND ARE GREATED BY THE OWNER...YOU MANAGED TO REFUGEE ALL THE KIDNAPED PEOPLE.")
                
                    if health>=5:
                        print("YOU HAVE SURVIVED....YOU WON!")

                else:
                    print("YOU FELL IN THE RIVER AND LOST.....")

        
            else:
                print("YOU FELL DOWN AND LOST YOUR LIFE.....")

        else:
            print("HAVE A NICE DAY! SEE YOU LATER....." )
    else:
        print("YOU ARE NOT OLD ENOUGH TO PLAY THIS GAME.....")

def TheFortune():
    print(" ________________ ")
    print("|                                                |")
    print("|_|Welcome to a cool fortune teller game!!!|_|")
    print("|________________|")
    colour=("Red","Blue","Pink","Purple")   #Using tuple
    print("1) Red")
    print("2) Blue")
    print("3) Pink")
    print("4) Purple")
    Fortune="True"
    while Fortune=="True":
        Pcolour=input("Select a colour: ")
        if Pcolour == colour[0] or Pcolour==colour[2]:
            number = eval(input("Select a number: 1, 2, 5, or 6:"))
            if number==1:
                print("You will be a very rich person!")
            elif number==2:
                print("You will not get homework tomorrow!")
            elif number==5:
                print("You will win a lottery!")
            elif number==6:
                print("You will live in a mansion!")
            else:
                print("Sorry! You must enter 1, 2, 5 or 6")
        elif Pcolour == colour[1] or Pcolour == colour[3]:
            number= eval(input("Select a number: 3, 4, 7, or 8:"))
            if number==3:
                print("You will slip on the floor!")
            elif number==4:
                print("You will get Rs.2000 from the floor!")
            elif number==7:
                print("You will be lost in the mall!")
            elif number==8:
                print("You will get good grades in your next test!")
            else:
                print("Sorry! You must enter 3, 4, 7, or 8")
        else:
            print("You must enter a correct colour: Red, Blue, Pink, or Purple")
        Fortune=input("Enter 0 to stop or True to continue: ")  # (0) or (True)
        if Fortune==0:
            break
def main_game_menu():
    return TheFortune()

def get_tof_statement():             #Using functions
    statements=[]                    #Using lists
    statements.append(["The World's longest sea bridge is in China","T"])
    statements.append(["28th Feb is known as leap day","F"])
    statements.append(["The capital of France is Paris","T"])
    statements.append(["The deepest point in the world is Dead Sea","F"])
    return statements
def play_tof_quiz():
    tof_statements=get_tof_statement()
    random.shuffle(tof_statements)
    score=0
    for s in tof_statements:         #Using loops
        print("True or False: "+s[0])
        guess=input("Enter T or F: ")
        if guess==s[1]:
            print("Correct! :)")
            score+=1
        else:
            print("Incorrect :(")
    print("Your final score is: "+str(score))
def get_maths_statements():
    statements=[]
    statements.append(["What is 10+20","30"])
    statements.append(["What is 25-5","20"])
    statements.append(["What is 5*5","25"])
    statements.append(["What is 4/2","2"])
    return statements
def play_maths_quiz():
    maths_statements=get_maths_statements()
    random.shuffle(maths_statements)
    score=0
    for s in maths_statements:
        print("Answer: "+s[0])
        guess=input("Enter your answer: ")
        if guess==s[1]:
            print("Correct! :)")
            score+=1
        else:
            print("Incorret :(")
    print("Your final score is: "+str(score))
def main_menu():
    print(" __________________ ")
    print("|                                                    |")
    print("|***** Welcome to QUIZ MASTER!*****|")
    print("|__________________|")
    print("|                                                    |")
    print("| Please select an option:                           |")
    print("| 1. Play General Knowledge (True or False) quiz     |")
    print("| 2. Play Maths quiz                                 |")
    print("| 0. Quit                                            |")
    print("|__________________|")
    print()
    for j in range(10): 
        choice=input("Enter 1,2 or 0: ")
        if choice=="1":                 #Using conditional statements
            play_tof_quiz()
        elif choice=="2":
            play_maths_quiz()
        else:
            if choice==0:
                quit()
                break
            print("Thanks for playing!")
            break
def Quiz():
    print("****WELCOME TO QUIZ_ARENA****")
    key=input("Enter 1 to start: ")
    if key=="1":
        main_menu()
    else:
        print("YOU HAVE EXITED THE QUIZ")
def Game():
    print("***WELCOME TO THE GAME*****")
    key=input("Enter 1 to start the fortune game or 2 to start the 2nd game: ")
    if key=="1":
        main_game_menu()
    elif key=="2":
        main_adv_game_menu()
    else:
        print("YOU HAVE EXITED THE GAME")
        
def main():
    print("*****QUIZ_MANIA******")
    import datetime
    t=datetime.datetime.now()
    print("DATE: ",t.strftime("%D"),"\n")
    Final=True
    while Final!=False:
        print(" __________________ ")
        print("|                                                  |")
        print("|            Choose any one of them                |")
        print("|_________________-|")
        print("| 1) Game                                          |")
        print("| 2) Quiz Master                                   |")
        print("| 3) Exit                                          |")
        print("|__________________|")
        choice=eval(input("Select choice 1,2 or 3: "))
        if choice==1:
            Game()
        elif choice==2:
            Quiz()
        else:
            if choice==3:
                EXIT()
        Final=input("If you want to EXIT,enter False: ")
        if Final!=False:
            continue
        else:
            if Final==False:
                quit()
main()
