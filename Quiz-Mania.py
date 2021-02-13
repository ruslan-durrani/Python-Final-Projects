def Quiz():
  print("***********_QUIZ_ARENA*************\n")
def Game():
  print("****************WELCOME_TO_GAME ARENA****************\n")

def result():
  print("*********RESULT_MENUE****************\n")
#Main function_____________________________________________
def main ():
  print("************__QUIZ-MANIA__*************\n")
  
  import datetime
  import random
  t = datetime.datetime.now()
  print("DATE : ",t.strftime("%D"),"\n")
  Final = "Shyesta "
  while Final != "EXIT":
    list1 = ["Game","Quiz","Result"]
    for x in range(len(list1)):
      print(str(x+1)+":) ",list1[x])
    choice=eval(input("Select choice:  "))
    if choice==1:
      Game()
      #game pr kaam kro ab 
    elif choice == 2:
      Quiz()
      #Quiz pr kaam kro 
    elif choice == 3:
      result()
    #result pr kaam kro 
  
      
    
    
    Final = input("Do you want to cintinue? Yes/EXIT").upper()
  
    
    
  

main()
