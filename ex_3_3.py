scoo = input("Enter a score between 0.0 and 1.0: ")
grade = float(scoo)

if (grade >=0.0 and grade <= 1.0 ) :  
    if (grade >= 0.9):
        print("A")
elif(grade >= 0.8):
    print("B")
elif(grade >= 0.7):
    print("C")
elif(grade >= 0.6):
    print("D")
elif(grade < 0.6):
    print("F")            
else:
    print("Please follow the instructions!")
