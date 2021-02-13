print("*****************  WELCOME TO STUDY WITH ENTERTAINMENT  *****************")
import datetime
import time
x = datetime.datetime.now()
print("Day : ",x.strftime("%A"))
print("Date : ",x.strftime("%D"),"\n")
Name = input("What is your name ? ").title()
def Study_Quiz():
    print("\n***********WELCOME TO STUDY KNOWLEGE**************\n")
#def Maze_Game():
''''    
    print("\n***********WELCOME TO MASTER MIND MAZE GAME**************\n")
    time.sleep(1.5)
    print("You have 3 moves to win")
    again = "ICT"
    while again != "YES":
        move = input("You are driving a  car ; you move : left/right/forward ").upper()
        if move=="FORWARD":
            n_move = input("Overspeeding\n moving..."+move+"...Hey here are the Copes...next move: left/right/forward ").upper()
            if n_move == "RIGHT":
                l_move = input("You drawn into the river....You swam...next move..: left/right/forward  ").upper()
                if l_move == "LEFT":
                    print("The Cops Captured you: Game over ")
                elif l_move =="RIGHT":
                    print("You escaped : Victory***")
                else:
                    print("You were eaten by Shark...Destroyed")
        elif move == "LEFT":
            m_move = input("You smashed an old Man: escaping...move: Left/Right").upper()
            if m_move == "LEFT":
                print("You escaped..*VICTORY")
            else:
                print("You were caught by the civilians...*Game over")
        elif move =="RIGHT":
            b_move == input("Moving ", move,"..road blocked..Army check post ahead .Move: left/right ").upper()
            if b_move=="RIGHT":
                b_move == input("You Pass by the military academy :move left/right").upper()
                if b_move=="LEFT":
                    print("You escaped : *Victory")
                else:
                    print("YOU fell off the cliff")
            elif b_move == "LEFT":
                print("You enter the football gound: *Enjoy")
                
                
                
'''
#def Score():
def main():
    List = ["Play Game","Study with Quiz","Results"]
    Yes = "Shayesta"
    while Yes != "EXIT" and Yes != "NO":
        for x in range(len(List)):
            print(str(x+1)+":)",List[x])
        choice = int(input(Name+" select any of your choice: "))
        time.sleep(1.5)
        if choice == 1:
            Maze_Game()
            
        Yes = input(Name+" do you want another Experience: Yes/Exit: ").upper()
main()
