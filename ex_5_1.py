largest = None
smallest = None
while True :
   aval = input("Enter a number: ")
   if aval == 'done' :
       break
   try :
      flval = float(aval)
   except:
       print('Invalid input')
       continue
if largest is None:
        largest = flval
elif largest < flval:
        largest = flval

if smallest is None:
        smallest = flval
elif smallest > flval:
        smallest = flval

print("Maximum is", largest)
print("Minimum is", smallest)