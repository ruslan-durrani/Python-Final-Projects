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
