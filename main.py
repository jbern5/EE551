import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# import sklearn
# from sklearn import preprocessing
# from sklearn.preprocessing import scale


rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

#cars = pd.read_csv("mtcars.csv")
cars = pd.read_csv("data.csv")

choice = -1

while choice != 0:
# ===================Menu======================

    print("Enter 0 to quit")
    print("Enter 1 to see all cars")
    print("Enter 2 to search a specific car")
    print("Enter 3 to search cars based on specs")
    print("Enter 4 to see summary statistics")

    choice = int(input("Choice: "))

#================Show Cars====================
    if choice == 1:
        print('Total Cars: ' + str(cars['Make'].count()))
        for car in set(cars['Make'] + ' ' + cars['Model']):
            print(car)
#================Search Specific Car=========================
    elif choice == 2:
        carType = input("What type of car? \n")
        for car in set(cars[cars['Make'] == str(carType.capitalize())]['Model']):
            print(car)
        print(' ')
        modelType = input("Which Model? \n")
        print(cars[cars['Make'] == str(carType.capitalize())][cars['Model'] == str(modelType.capitalize())].iloc[:,0:3])
#================Search By Specification=========================
    elif choice == 3:
        carSpec = input("What are you looking for?\n You can search by the following:\n Make, Model, Year, Fuel, Horsepower, Cylinders, Tranmission, Drive, Doors, Size, Style, MPG, and MSRP")
        if carSpec.capitalize() == "Make":
            carMake = input("What make of car? \n")
#             for car in set(cars[cars['Make'] == str(carMake.capitalize())]['Model']):
#                 print(car)
            modelType = input("Which Model? \n")
            print(cars[cars['Make'] == str(carMake)][cars['Model'] == str(modelType.capitalize())].iloc[:,0:3])
        elif carSpec.capitalize() == "Model":
            modelType = input("Which Model? \n")
            print(cars[cars['Model'] == str(modelType.capitalize())].iloc[:,0:3])
        elif carSpec.capitalize() == "Year":
            year = input("Which Year? \n")
            print(cars[cars['Year'] == int(year)].iloc[:,0:3])
        elif carSpec.capitalize() == "Fuel":
            fuelType = input("What fuel type? \n")
            print(cars[cars['Engine Fuel Type'] == str(fuelType.lowercase()) + 'unleaded'].iloc[:,0:3])
        elif carSpec.capitalize() == "Horsepower":
            hp = input("How much hp? \n")
            print(cars[cars['Engine HP'] == int(hp)].iloc[:,0:3])
        elif carSpec.capitalize() == "Cylinders":
            cyl = input("How many cylinders? \n")
            print(cars[cars['Engine Cylinders'] == int(cyl)].iloc[:,0:3])
        elif carSpec.capitalize() == "Transmission":
            trans = input("What transmission type? \n")
            print(cars[cars['Transmission Type'] == trans.upper()].iloc[:,0:3])
        elif carSpec.capitalize() == "Transmission":
            trans = input("What transmission type? \n")
            print(cars[cars['Transmission Type'] == trans.upper()].iloc[:,0:3])
        elif carSpec.capitalize() == "Drive":
            drive = input("What drive mode? \n")
            print(cars[cars['Driven_Wheels'] == drive].iloc[:,0:3])
        elif carSpec.capitalize() == "Doors":
            doors = input("How many doors? \n")
            print(cars[cars['Number of Doors'] == int(doors)].iloc[:,0:3])
        elif carSpec.capitalize() == "Size":
            size = input("What size? \n")
            print(cars[cars['Vehicle Size'] == size.capitalize()].iloc[:,0:3])
        elif carSpec.capitalize() == "Style":
            style = input("What style? \n")
            print(cars[cars['Vehicle Style'] == style.capitalize()].iloc[:,0:3])
        elif carSpec.upper() == "MPG":
            mpg = input("highway or city? \n")
            if mpg.lower() == "highway":
                mpgType = input("What MPG? \n")
                print(cars[cars['highway MPG'] >= int(mpgType)].iloc[:,0:6])
            elif mpg.lower() == "city":
                mpgType = input("What MPG? \n")
                print(cars[cars['city mpg'] == int(mpgType)].iloc[:,0:3])
        elif carSpec.upper() == "MSRP":
            msrp = input("Max MSRP? \n")
            print(cars[cars['MSRP'] <= int(msrp)].iloc[:,0:3])
        else:
            print("Spec not found, try again")

#================Show Stats====================
    elif choice == 4:
        print(cars.describe())
        plt.hist(cars['Year'])
        plt.title("Cars per Year")
        plt.xlabel("Year of Car")
        plt.ylabel("# of Cars")
        plt.show()

        plt.hist(cars['highway MPG'])
        plt.title("Cars per MPG")
        plt.xlabel("MPG of Car")
        plt.ylabel("# of Cars")
        plt.xlim(10,45)
        plt.show()

