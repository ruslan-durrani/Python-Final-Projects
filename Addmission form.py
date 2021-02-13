class Addmission:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
class CourseM(Addmission):
    def __init__(self,name,marks,subject):
        self.subject = subject        
        super().__init__(name,marks)
    def add (self,subject):
        if self.subject =="MATH" and self.marks>90 :
            self.submit(self.subject)
        elif self.subject =="ENGLISH" and self.marks>70 :
            self.submit(self.subject)
        elif self.subject =="SCIENCE" and self.marks>80 :
            self.submit(self.subject)
        else:
            print("you Do not Qualify")
    def submit(self,S):
        File = open("Addmission Form.txt","a+")
        File.write("\n")
        N = str(self.name)
        S = str(self.subject)
        M = str(self.marks)
        File.write("Addmission Granted In SCIENCE Subject")
        File.write("\n")
        File.write(str("Name: "+N))
        File.write("\n")
        File.write(str("Subject: "+S))
        File.write("\n")
        File.write(str("Marks: "+M))
        File.close()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
try:
    New = open("Addmission Form.txt")
    New.close()
except:
    New = open("Addmission Form.txt","w")
    New.close()

DICT = {"Science": 80,"English": 70,"Math":90}
for x in DICT:
    print("Subject: ",x)
    print("Qualificiation criteria (Marks should be greater than) : ",DICT[x])
print("Addmission form ")
X = "YES"
while X != "NO":
    name = input("Your name : ").upper()
    marks = int(input("Enter marks : "))
    subject = input("In whcih you want to take addmission : ").upper()
    ##Object
    C = CourseM (name,marks,subject)
    C.add(subject)
    X = input("Another Addmission: Yes/NO ").upper()



