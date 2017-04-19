#Programing Assignment #2
#CSci 1523
#Ben Carey
#
#Purpose: This program will open a file containing a list points and
#   read the x and y values into two seperate lists. it then calculates the
#   averages of the values contained in each list to use in the calculation of
#   the standard deviation of each list, the slope of the regression line, the y
#   intercept of the regression line, and the coefficient of determination.
#   it then will print th slope, y intercept, and coefficient of determination
#   to the terminal window.


#----------------------------------MODULES--------------------------------------

#import math module for use
import math

#-----------------------------------FUNCTIONS-----------------------------------

#the slope function will calculate and return
# the slope of the regression line
# it will accept two lists of floats, and two float arguments
def slope(xArr, yArr, avgx, avgy):
    numerator = 0
    denomonator = 0
    #iterate through values until end of list is reached
    for i in range(0,len(xArr), 1):
        numerator = numerator + (xArr[i] - avgx) * (yArr[i] - avgy)
        denomonator = denomonator +(xArr[i] - avgx) ** 2
    slope = numerator/denomonator

    return slope

#the standDev function calculates and returns the standard deviation
# it will accept an list of floats andthe average of that list
def standDev(arr, avg):
    standDev = 0

    for i in range(0, len(arr), 1):
        standDev = standDev + ((arr[i] - avg) ** 2)/len(arr)

    return math.sqrt(standDev)

#the coeffDeterm function calculates and returns the value of the
# coefficient of determination, R**2
def coeffDeterm(xArr, yArr, avgx, avgy, standDevX, standDevY):
    iterate = 0
    for i in range(0, len(xArr), 1):
        iterate = iterate + (xArr[i] - avgx) * (yArr[i] - avgy)
    rSqr = (1/len(xArr)) * iterate / (standDevX * standDevY)

    return rSqr **2



#-----------------------------------MAIN----------------------------------------

#----------------------------------import data from file and save into two lists

#set empty string to signify EndOfFile
eof_str = ''

#a list to hold data from file to store in X value
fileDataX = []
#a list to hold data from file to store in Y value
fileDataY = []

#open Regression.dat file to read
input_file = open('Regression.dat', 'r')

#read first line into fileIn object
fileIn = input_file.readline()

#keep reading until eof_str encountered
while fileIn != eof_str:
    #strip newLine /n
    line = fileIn.strip('\n')
    #split the string at the comma
    line = fileIn.split(',')

    #savefirst String value cast
    #as a float into Xarray
    fileDataX.append(float(line[0]))

    #save second String value cast
    #as a float into y array
    fileDataY.append(float(line[1]))

    #read next line in file
    fileIn = input_file.readline()
#close input file
input_file.close


#---------------------------------------calculate averages of data in both lists
#----------------------------access functions to calculate slope, coefficient of
#------------------------------------------determination, and standard deviation
#-----------------------------------calculate y intercept of the regression line

#calculate average of the xvalues
avgx = sum(fileDataX)/len(fileDataX)
#calculate averageof the yvalues
avgy = sum(fileDataY)/len(fileDataY)

#calculate slope for regression line
slope = slope(fileDataX, fileDataY, avgx, avgy)
print( "m (the slope of the line of regression)is : ", slope )

#calculate standard deviation for x values
standDevX = standDev(fileDataX, avgx)
#calculate standard deviation for y values
standDevY = standDev(fileDataY, avgy)

#calculate Coefficient of Determination
rSqrd = coeffDeterm(fileDataX, fileDataY, avgx, avgy, standDevX, standDevY)
print( "R^2 or the Coefficient of Determination or: ", rSqrd )

#calculate y intercept for regression line
yintercept = avgy - slope * avgx
print("b (the y intercept of the lineof regression) is: ", yintercept)
