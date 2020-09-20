# Basic python functions...

# Function 1: converts minutes to hours
def minutes_to_hours(minutes):
    hours = minutes / 60 # hours is a local variable
    return hours 

# Function 2: converts seconds to hours
def seconds_to_hours(seconds):
    hours = seconds / 3600 # hours is a local variable
    return hours 

print(minutes_to_hours(70))
print(seconds_to_hours(7200))

# constant functions - Functions created by you
# built-in functions - Functions created by someone else e.g print
# print code is low-level: written in c
