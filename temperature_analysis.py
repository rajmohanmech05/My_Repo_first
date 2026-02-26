# Name : Rajmohan Krishnamoorthy
# Roll Number: iitp_aimltn_2602455 
#Assignment: PythonLoops & Automation - Subjective Question

print ("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

#Assume the first temperatire is both highest and lowest initially
highest = temperatures[0]
lowest = temperatures[0]

#loop through each temearture

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print (f"Highest Tempearture :{highest}°C")
print (f"Lowest Tempearture :{lowest}°C")

print (" ===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <=30:
        continue #skip days that are 30°C and below
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")


print ("\n===== Task 3: Alert system =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for day, temp in enumerate(temperatures, start=1):
    if temp >= 40:
        print(f"Hot Days before alert:{hot_days}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    if temp > 30:
        hot_days += 1
