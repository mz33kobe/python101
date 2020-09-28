#5.2 Write a program that repeatedly prompts a user
#  for integer numbers until the user enters 'done'.
#  Once 'done' is entered, print out the largest and smallest of the numbers.
#  If the user enters anything other than 
# a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. 
# Enter the numbers from the book for problem 5.1
#  and Match the sample output below.

largest = None

smallest = None
while True:
     try:
         num= input(" enter the number: ")
         if num== "done":
             break
             n=int(num)
             if largest is None or largest > num:
                 largest=num
         elif smallest is None or smallest < num:
                smallest=num
     except:
            print("invalid input")
     continue
print("maximum is ", largest)
print( "minimum is", smallest)