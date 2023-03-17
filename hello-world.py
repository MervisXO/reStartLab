# print("Hello, World")
# print("Hello, World")
# print("Python has three numeric types: int, float, and complex")
# myValue=1
# print (myValue)
# print(str(myValue) + " is of the data type " + str(type(myValue)))
# myValue=3.14
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))
# myValue=5j
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))
# myValue=True
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))
# myString = "This is a string."
# print(myString)
# print(type(myString))
# print(str(myString) + " is of the data type " + str(type(myString)))
# firstString= "water"
# secondString= "fall"
# thirdString= firstString + secondString
# print(thirdString)
# name=input("What is your name? ")
# print (name)
# color =input("what is your favorite color? ")
# animal =input("what is your favorite animal? ")
# # print("{}, you like a {} {}".format(name, color, animal))
# # print("{}, you like {} that is {}".format(name, animal, color))
# myFruitList = ["apple", "banana", "cherry"]
# print(myFruitList)
# print(type(myFruitList))
# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])
# myFruitList[2]= "orange"
# myFruitList[0]= "papaya"
# print (myFruitList)
# myFinalAnswerTuple = ( "apple", "banana", "cherry")
# print(myFinalAnswerTuple)
# print(type (myFinalAnswerTuple))
# print(myFinalAnswerTuple[0])
# print(myFinalAnswerTuple[1])
# print(myFinalAnswerTuple[2])
# myFavoriteFruitDictionary = {
#   "Akua" : "apple",
#   "Saanvi" : "banana",
#   "Paulo" : "pineapple"
# }
# myFavoritePet = {
#     "Bella" : "Dog",
#     "Sara" : "Cat",
#     "Brienne" : "Bunny"
#     }
# print(myFavoritePet)
# print(type(myFavoritePet))
# print(myFavoritePet['Bella'])
# print(myFavoriteFruitDictionary['Paulo'])
# myMixedTypeList = ["45", "Adeolu", 123, 14.5, True, "my Dog loves to eat"]
# print("{} is of the data type {}".format(14.5,type(14.5)))
# print("{} is of the data type {}".format("Adeolu",type("Adeolu")))
# print("{} is of the data type {}".format(123, type(123)))
# print("{} is of the data type {}".format(True, type (True)))
# print("{} is of the data type {}".format("my Dog loves to eat", type ("my Dog loves to eat")))
import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0,
}
myInventoryList = []
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1
    print(f'processed {lineCount} lines')
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")