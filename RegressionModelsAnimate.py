#Programing Assignment #2 BONUS
#CSci 1523
#Ben Carey

#This program will open a file containing a list points and
#   read the x and y values into two seperate lists. it then calculates the
#   averages of the values contained in each list to use in the calculation of
#   the standard deviation of each list, the slope of the regression line, and the
#   y intercept of the regression line.
#   Then useing the calculated values and Zelle's Graphics Module the program
#   then opens a graph window and plots the contents of each list to the window
#   and draws the line of regression to the screen. Once this is completed the
#   program calculates and displys the distance of each point plotted from
#   the line of regression


#----------------------------------MODULES--------------------------------------

#import math module for use
import math
import time
from graphics import *

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

    return rSqr ** 2


#----------------------------GRAPHICS FUNCTION----------------------------------

#graphIt function using Zelle's graphics module creates a graphics window and
#   diplays the calculations made in the main section of program it accepts two
#   lists, the average of each list, the standard deviation of each list, the y
#   intercept of the regression line, and the slope of the regression line

#---------------------------------------------prepaire window to display a graph

def graphIt(xArr, yArr, avgx, avgy, standDevX, standDevY, yIntercept, slope):
    #open a window to draw to
    # set the window to 100px by 700px
    # in the window set a graph starting at
    # point (-0.5,-1) and extending to (10,33)
    win = GraphWin("Csci1523Assign2Animate", 1000, 700) #set Window to 600x600
    win.setCoords(-0.5,-1,10,33)

    win.getMouse()

    #draw blue x axis boundery arrow to graph window
    xAxis = Line(Point(-1,0), Point(10,0))
    xAxis.setArrow('last')
    xAxis.setOutline('blue')
    xAxis.draw(win)
    #draw blue vertical markers along the xAxis
    for x in range(1, 10, 1):
        l = Line(Point(x,0), Point(x,-0.3))
        l.setOutline('blue')
        l.draw(win)
        #mark each odd marker with its index value
        if x % 2 != 0:
            lineLable = Text(Point(x , -0.7), x)
            lineLable.setOutline('blue')
            lineLable.setSize(8)
            lineLable.draw(win)

    #draw red y axis boundery arrow to graph window
    yAxis = Line(Point(0,-1), Point(0,33))
    yAxis.setArrow('last')
    yAxis.setOutline('red')
    yAxis.draw(win)
    #draw red vertical markers along the yAxis
    for y in range(1, 33, 1):
        l = Line(Point(0,y),Point(-0.1,y))
        l.setOutline('red')
        l.draw(win)
        #mark each fifth marker with its index value
        if y % 5 == 0:
            lineLable = Text(Point(-0.3, y), y)
            lineLable.setOutline('red')
            lineLable.setSize(8)
            lineLable.draw(win)

    #----------------------------------------------graph imported data to screen
    #graph points from file to sceen
    for i in range(0, len(xArr), 1):
        points = Point(xArr[i],yArr[i])
        points.draw(win)
        #pause 0.3 seconds between each point plotted to screen
        time.sleep(0.3)

    #calculate x for y=24.75
    regressionLineXpoint = (24.75 - yIntercept) / slope
    #set the first point of the regression line to the yintercept
    # set the second point on the line to the calculated x point, and the y
    # to 24.75
    regressionPointOne = Point(0,yIntercept)
    regressionPointTwo = Point(regressionLineXpoint, 24.75)

    #plot and draw regression line in purple with arrows at both ends
    regressionLine = Line(regressionPointOne, regressionPointTwo)
    regressionLine.setArrow('both')
    regressionLine.setOutline('purple')
    regressionLine.draw(win)

    #for each point calculate distance from regressionLine and draw orange line
    # between point and regression line to display difference and lable point
    # with distance from regression line
    for i in range(0, len(xArr), 1):
        #set origin point
        orgPoint = Point(xArr[i],yArr[i])
        #calculate y for point on regression line corresponding to the current
        # x value
        regressionLinePointY = slope * xArr[i] + yIntercept
        #set point on regression line dirrectly above or below current x value
        regressionLinePoint = Point(xArr[i], regressionLinePointY)
        #set orange line between origin point and point on regression line
        errorLine = Line(orgPoint, regressionLinePoint)
        errorLine.setOutline('orange')
        #draw organge error line to screen
        errorLine.draw(win)

        #if origin point is above the regression line set error lable above
        # the origin point
        # else set error lable below origin point
        if yArr[i] > (slope * xArr[i] + yIntercept):
            lablePoint = Point(xArr[i], (yArr[i]+0.35))
            lableTitle = yArr[i] - (slope * xArr[i] + yIntercept)
        else:
            lablePoint = Point(xArr[i], (yArr[i]-0.35))
            lableTitle = (slope * xArr[i] + yIntercept) - yArr[i]
        #set error lable text to appear at size 10px font and round the calculated
        # error to the nearest hundreth
        lable = Text(lablePoint, round(lableTitle, 2))
        lable.setSize(10)
        lable.draw(win)
        #wait 0.3 seconds before drawing the next error line
        time.sleep(0.3)

    #wait for mouse click to close the window
    win.getMouse()
    win.close()


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
#-------------------------------------------access functions to calculate slope,
#-----------------------------------calculate y intercept of the regression line

#calculate average of the xvalues
avgx = sum(fileDataX)/len(fileDataX)
#calculate averageof the yvalues
avgy = sum(fileDataY)/len(fileDataY)

#calculate slope for regression line
slope = slope(fileDataX, fileDataY, avgx, avgy)

#calculate standard deviation for x values
standDevX = standDev(fileDataX, avgx)

#calculate standard deviation for y values
standDevY = standDev(fileDataY, avgy)

#calculate y intercept for regression line
yintercept = avgy - slope * avgx

#call the graphIt function to access Zelle's Graphics Module
graphIt(fileDataX, fileDataY, avgx, avgy, standDevX, standDevY, yintercept, slope)
