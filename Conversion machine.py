def Temp():
    Temperature = ["Celcius","Fahrenheit"]
    for x in range(0,len(Temperature)):
        print(x+1,"): ",Temperature[x])
    TempCh = int(input("Enter the choice you want to convert : "))
    if TempCh==1:
        celcius = int(input("Enter the temperature in celcius : "))
        Fahren = (celcius * (9/5) + 32 )
        print("The Temperature in Fahrenheit is : ",Fahren,"\n")
    if TempCh==2:
        Fahren = int(input("Enter the temperature in Fahrenheit : "))
        celcius = (Fahren - 32) * (5/9)
        print("The Temperature in celcius is : ",celcius,"\n")

def Curr():
    print("(Dollar)","(Rupee)","(RMB)","(EURO)")
    print()
    Curr = input("Enter the cuurency that is to be converted: ").upper()
    CurrTo = input("Enter currency converted to ").upper()
    if Curr == "DOLLAR" :
        if CurrTo == "RUPEE":
            D = int(input("Enter Dollars: "))
            print(D," dollars = ",D*160.15," Rupees")
        elif CurrTo == "RMB":
            D = int(input("Enter Dollars: "))
            print(D," dollars = ",D*6.55," RMBs")
        elif CuuTo == "EURO":
            D = int(input("Enter Dollars: "))
            print(D," dollars = ",D*0.83," EUROs")
    elif Curr == "RUPEE":
        if CurrTo == "DOLLAR":
            R = int(input("Enter Rupees: "))
            print(R," Rupees = ",R/160.15," Dollars")
        elif CurrTo == "RMB":
            R = int(input("Enter Rupees: "))
            print(R," Rupees = ",R*0.041," RMBs")
        elif CurrTo == "EURO":
            R = int(input("Enter Rupees: "))
            print(R," Rupees = ",R*0.0052," EURO")
        
    elif Curr == "RMB":
        if CurrTo == "DOLLAR":
          RM = int(input("Enter RMBs: "))
          print(RM," RMBs = ",RM*0.15," Dollars")
        elif CurrTo == "RUPEE":
          RM = int(input("Enter RMB: "))
          print(RM," RMB = ",RM*24.46," Rupees")
        elif CurrTo == "EURO":
          RM = int(input("Enter RMB: "))
          print(RM," RMB = ",RM*0.13," EUROs")
    elif Curr == "EURO":
        if CurrTo == "DOLLAR":
          E = int(input("Enter EURO: "))
          print(RM," EURO = ",E*1.21," Dollars")
        elif CurrTo == "RUPEE":
          E = int(input("Enter EUROs: "))
          print(E," EURO = ",E*193.97," Rupees")
        elif CurrTo == "RMB":
          E = int(input("Enter EUROs: "))
          print(E," EUROs = ",E*7.93," RMBs")
    else:
        print("WRONG INPUT")
        
            
           
        
            
        
def Vol():
    size = ["Centimeter","Meter","Inches"]
    for x in range(len(size)):
        print(x+1,":) ",size[x])
    Ch = int(input("Enter choice : "))
    if Ch == 1:
        C = int(input("Enter Centimeters : "))
        C_M = C*0.01
        C_I = C*0.393701
        print(C," centimeters = ",C_M," meters and ",C_I," inches\n")
    elif Ch == 2:
        M = int(input("Enter Meters : "))
        M_C = M*100
        M_I = M*39.3701
        print(M," meters = ",M_C," centimeters and ",M_I," inches\n")
    elif Ch ==3:
        I = int(input("Enter Inches : "))
        I_C = I*2.5400013716
        I_M = I*0.025400013716
        print(I," Inches = ",I_C," centimeters and ",I_M," meters\n")
        
def mass():
    Mass = ["Pound","Kilogram"]
    for x in Mass:
        print(x)
    F = input("Enter the unit that is to be converted : ").upper()
    if F=="POUND":
        EN = int(input("Enter weight in pounds : "))
        print("The mass in kilograms is : ",EN*0.453592,"\n")
    elif F == "KILOGRAM":
        EN = int(input("Enter weight in KGs : "))
        print("The mass in pounds is : ",EN*2.20462,"\n")
    else:
        print("Wrong input\n")
        
def main():
    list1 = ["Temperature(C/F)","Currency($-R-£-RMB)","Meters/Centimeters/Inches","Mass(Pound/Kgs)"]
    print("\n*****WELCOME TO CONVERTER MACHINE*****\n")
    import datetime
    import time
    x = datetime.datetime.now()
    print("Day : ",x.strftime("%A"))
    print("Date : ",x.strftime("%D"),"\n")
    Name = input("What is your name ? ").title()
    print("\n"+Name+", select any choice: \n")
    
    Dec = "Shayesta"
    while Dec !="EXIT":
        for x in range(len(list1)):
            print(x+1,":) ",list1[x])
        print()
        choice = int(input("Your Choice: "))
        if choice==1:
            Temp()
            print()
        elif choice == 2:
            Curr()
        elif choice == 3:
            Vol()
        elif choice == 4:
            mass()
        Dec = input("Do you want to continue : YES/EXIT ").upper()

                    
main()
