def python():
    
    print("\n\n\t\t\t---------------Page1------------------")
    L1=[]
    L2=[]
    #Total Students 2 each has 2 preferences+++++++++++++++++++++++++++++++
    Student=1
    while Student!=3:#Total Students are 2
        print("*****Student-"+str(Student)+"*****")
        Student +=1
        n1=input("Enter Your Name:")
        n2=input("Enter The Name Of Your Father:")
        n3=input("Enter Your CNIC:")
        n4=input("Enter The CNIC of Your Father:")
        n5=input("Enter Residence:")
        n6=input("Enter The Matric Percentage:")
        n7=input("Enter The Fsc Percentage:")
        F=["BS-COMPUTER SCIENCE","BS-SOFTWARE ENGINERING","BS-BOTANY","BS-ZOLOGY","BS-PHYSICS","BS-PYSCOLOGY"]
        choice=2
        for x in range(2):
            #print(x+1,"):",F[x])
            print("------------------------SELECT THE FIELD---------------------------------")
            print("Student Choses The Following Progams:","\n")
            for k in range(len(F)):
                print(k+1,") ",F[k])

            n8=input("Selcect Your Choice In Integer:")
            #Student-=1
            
            if n8=='1':
                print(F[0])
                L1.append(F[0])
            elif n8=='2':
                print(F[1])
                L1.append(F[1])
            elif n8=='3':
                print(F[2])
                L1.append(F[2])
            elif n8=='4':
                print(F[3])
                L1.append(F[3])
            elif n8=='5':
                print(F[4])
                L1.append(F[4])
            elif n8 == '6':
                print(F[5])
                L1.append(F[5])
            if x == 1:
                print("Your Preferences are: ")
                for items in L1:
                    print(items)
                break
            SHEYSTA=input("Press Yes FOR Second Preference:").upper()
            
            if SHEYSTA != "YES":
                break
        #print("Student Choses The Following Progams:","\n")
        print()
        
        
        
        
        
    
    
    
   
    
    
    print("--------page2--------")
    print("--------page3--------")
    print("--------end----------")
python()
