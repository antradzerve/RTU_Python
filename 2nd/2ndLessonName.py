import datetime
currentYear = datetime.datetime.now().year

userName = input("Hello there! What is your name?")
userAge = int(input(f"Hello, {userName}! Would you mind telling me your age? In whole years, please."))

timeTillHundred = 100 - userAge
hundredYearsLater = userAge + 100
yearOfHundred = currentYear + timeTillHundred

print(f"Well, if today is {currentYear}, then it will take you {timeTillHundred} years to reach the age of 100 and that will be on year {yearOfHundred}. And in a 100-years time you will be {hundredYearsLater} years old!")

print("I want to know more about you!")
height = float(input("How high is the ceiling of your room? Give the value in meters, please"))
width = float(input("And how about the width? Still asking for meters."))
lenght = float(input("How long in meters would you estimate the room is?"))

volumeOfTheRoom = height * width * lenght

print(f"Based on the information provided, you are located in a room with total volume of {volumeOfTheRoom} cube meters")