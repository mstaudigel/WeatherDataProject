# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:38:52 2019

@author: Matt

Weather data has been captured by the Northern Kentucky International Airport (CVG) 
for several decades to determine the daily weather patterns, temperatures, and 
precipitation levels for suitable flying. The FAA, or the Federal Aviation Administration, 
mandated large airports in the United States to do so in order to increase the safety 
of passengers and flights. Due to this mandate, there is a massive amount of daily 
weather data spanning back decades that we can analyze.

The dataset supplied by the NOAA contains the weather station name (CVG airport), 
the date of the observation, the precipitation (rain or sleet in inches) measurement 
of that day, the snow levels of that day in inches, the high temperature of the 
day and the low temperature of the day. The dataset was obtained via a request 
to the NOAA.

The goal of this project is to analyze weather data at CVG across 68.5 years to 
discover temperature trends and precipitation trends using Python. The following 
are analyses that will be targeted:

•	Hottest high temperature readings of each year
•	Coldest low temperature readings of each year
•	Average temperature of each year
•	Precipitation totals of each year
•	Average yearly precipitation for Cincinnati
•	Snow totals of each year
•	Average yearly snow amounts for Cincinnati
•	Wettest day of each year
•	Highest snow total of each year
•	Use the above observations to predict future readings and levels

"""


# import libraries needed
import csv
import matplotlib.pyplot as plt
from decimal import Decimal


# Define const variables
LEAP_YEARS = ("1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", 
              "1984", "1988", "1992", "1996", "2000", "2004", "2008", "2012", "2016")
LINE_GRAPH = SCATTER_PLOT = 0
STEM_PLOT = 1
BAR_GRAPH = 2


# Plot Function
def PlotData(xValues, yValues, highestYValue, lowestYValue, title, xAxisLabel, yAxisLabel, plotCharacteristics, typeOfGraph):
    
    # Clear data from plot object
    plt.clf()
    
    highestYValue = highestYValue * 1.05
    
    if (lowestYValue > 0):
        lowestYValue = lowestYValue * 0.95
    else:
        lowestYValue = lowestYValue * 1.05
    
    
    # Handle Different types of graphs
    if (typeOfGraph == LINE_GRAPH):
        plt.plot(xValues, yValues, plotCharacteristics)
    elif (typeOfGraph == STEM_PLOT):
        plt.stem(xValues, yValues, plotCharacteristics)
#    elif (typeOfGraph == BAR_GRAPH):
#        plt.
    else:
        print("ERROR: Plot could not be printed")
        return
    
    plt.axis([1950, 2019, lowestYValue, highestYValue])
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.show()
    



# Function imports data from CSV file and stores data in dictionary
def ImportWeatherData():
    
    print("Importing weather data...")
    
    # Define dictionary for weather data
    dataDictionary = {}
    
    # Traverse through CSV file
    with open('Python_Climate_Dataset_1950_2019.csv', 'r') as csvfile:
        dataReader = csv.reader(csvfile, quotechar='|')
        count = 0
        for row in dataReader:
            
            # Ignore first row of CSV
            if (count != 0):
                # Define tuple as value for dictionary entry
                weatherDataOfRow = (row[4], row[5], row[8], row[9])
                
                # Add daily weather data to dictionary
                dataDictionary[row[3]] = weatherDataOfRow
                
            count = count + 1

    # Return dictionary
    return(dataDictionary)
    
 


# Function calculates annual top values, averages, and precip totals
def CalculateAnnualWeatherDataAveragesAndTotals(weatherDict):
    
    print("Calculating yearly averages and Totals...")
    
    # Create Annual Weather Data Averages Dictionary
    AnnualAvgsDictionary = {}
    
    # Create Top precip days dictionary of each year
    TopPrecipDaysDictionary = {}
    
    # Create Top snow days dictionary of each year
    TopSnowDaysDictionary = {}
    
    # Create Top high temp days dictionary of each year
    TopHighTempDaysDictionary = {}
    
    # Create Top low temp days dictionary of each year
    TopLowTempDaysDictionary = {}
    
    
    # Define averaging values
    prcpTotals = 0.0
    highTmpTotals = 0.0
    lowTmpTotals = 0.0
    snowTotals = 0.0
    totalHighs = 0
    totalLows = 0
    count = 0
    
    # Get the date of the first day
    key = list(weatherDict.keys())[count]
    lengthOfKey = len(key)
    
    # Get the year of the first day
    currentYear = int(key[lengthOfKey - 4] + key[lengthOfKey - 3] + key[lengthOfKey - 2] + key[lengthOfKey - 1])
    
    # Define Top day trackers
    topPrecipDayOfYr = [key, 0.0]
    topSnowDayOfYr = [key, 0.0]
    topHighTempDayOfYr = [key, 0.0]
    topLowTempDayOfYr = [key, 100]
    
    # Plot results values
    topPrcpVals = []
    topSnowVals = []
    topHighVals = []
    topLowVals = []
    prcpVals = []
    snowVals = []
    highVals = []
    lowVals = []
    years = []
    
    # Loop through each day in the weather dictionary
    for day in weatherDict:
        
        
        # Get the date of the current day
        key = list(weatherDict.keys())[count]
        lengthOfKey = len(key)
        
        # Get the year of the current day
        year = int(key[lengthOfKey - 4] + key[lengthOfKey - 3] + key[lengthOfKey - 2] + key[lengthOfKey - 1])
        
        # Get weather readings of the day
        readings = list(weatherDict.values())[count]
        
        
        # Continue averaging until the next year begins
        if (year == currentYear):
            
            
            # if statements are for error handling to prevent addition of empty readings
            if (readings[0] != ""):
                prcpTotals = prcpTotals + float(readings[0])
                topPrecipDayOfYr = [key, float(readings[0])] if (topPrecipDayOfYr[1] < float(readings[0])) else topPrecipDayOfYr
            
            if (readings[1] != ""):    
                snowTotals = snowTotals + float(readings[1])
                topSnowDayOfYr = [key, float(readings[1])] if (topSnowDayOfYr[1] < float(readings[1])) else topSnowDayOfYr
            
            if (readings[2] != ""):
                highTmpTotals = highTmpTotals + float(readings[2])
                topHighTempDayOfYr = [key, int(readings[2])] if (topHighTempDayOfYr[1] < float(readings[2])) else topHighTempDayOfYr
                totalHighs = totalHighs + 1
            
            if (readings[3] != ""):
                lowTmpTotals = lowTmpTotals + float(readings[3])
                topLowTempDayOfYr = [key, int(readings[3])] if (topLowTempDayOfYr[1] > float(readings[3])) else topLowTempDayOfYr
                totalLows = totalLows + 1
            
                
        else:
            
            highTmpAvg = highTmpTotals/totalHighs
            lowTmpAvg = lowTmpTotals/totalLows
                
            # Create tuple for the annual averages dictionary
            yearAvgs = (prcpTotals, snowTotals, highTmpAvg, lowTmpAvg)
            
            
            
            # Add to dictionaries
            AnnualAvgsDictionary[year] = yearAvgs
            TopPrecipDaysDictionary[year] = topPrecipDayOfYr
            TopSnowDaysDictionary[year] = topSnowDayOfYr
            TopHighTempDaysDictionary[year] = topHighTempDayOfYr
            TopLowTempDaysDictionary[year] = topLowTempDayOfYr
            
            
            # Add to arrays for plotting
            prcpVals.append(prcpTotals)
            snowVals.append(snowTotals)
            highVals.append(highTmpAvg)
            lowVals.append(lowTmpAvg)
            topPrcpVals.append(topPrecipDayOfYr[1])
            topSnowVals.append(topSnowDayOfYr[1])
            topHighVals.append(topHighTempDayOfYr[1])
            topLowVals.append(topLowTempDayOfYr[1])
            years.append(year)
            
            
            # Reset averaging values
            prcpTotals = 0.0
            highTmpTotals = 0.0
            lowTmpTotals = 0.0
            snowTotals = 0.0
            totalHighs = 0
            totalLows = 0
            topPrecipDayOfYr = [key, 0.0]
            topSnowDayOfYr = [key, 0.0]
            topHighTempDayOfYr = [key, 0.0]
            topLowTempDayOfYr = [key, 100]
            
            
            
            # Increment to the next year
            currentYear = currentYear + 1
        
        # Increment overall day counter
        count = count + 1
        
    
    
    # Plot data and Print Overall Average Results
    PlotData(years, prcpVals, max(prcpVals), min(prcpVals), "Precipitation Totals 1950 to 2019", "Years", 
             "Precipitation Levels (inches)", '-.', STEM_PLOT)
    print("The average annual precipitation level, based on data between 1950-2019, is " + str(round(Decimal(sum(prcpVals) / len(prcpVals)), 2)) + " inches.")
    PlotData(years, snowVals, max(snowVals), min(snowVals), "Snow Totals 1950 to 2019", "Years", "Snow Levels (inches)", '-.', STEM_PLOT)
    print("The average annual snow level, based on data between 1950-2019, is " +  str(round(Decimal(sum(snowVals) / len(snowVals)), 2)) + " inches.")
    PlotData(years, highVals, 80, 50, "Average Annual High Temperature 1950 to 2019", "Years", "Temperature (F)", '-.', STEM_PLOT)
    print("The average annual high temperature, based on data between 1950-2019, is " +  str(round(Decimal(sum(highVals) / len(highVals)), 2)) + "*F")
    PlotData(years, lowVals, 60, 30, "Average Annual Low Temperature 1950 to 2019", "Years", "Temperature (F)", '-.', STEM_PLOT)
    print("The average annual low temperature, based on data between 1950-2019, is " +  str(round(Decimal(sum(lowVals) / len(lowVals)), 2)) + "*F")
    PlotData(years, topPrcpVals, max(topPrcpVals), min(topPrcpVals), "Highest Amount of Precipitation in a Single Day Per Year, 1950-2019", "Years", "Precipitation (inches)",
             'go', SCATTER_PLOT)
    PlotData(years, topSnowVals, max(topSnowVals), min(topSnowVals), "Highest Amount of Snow in a Single Day Per Year, 1950-2019", 
             "Years", "Snow Levels (inches)", 'bo', SCATTER_PLOT)
    PlotData(years, topHighVals, max(topHighVals), min(topHighVals), "Highest Recorded Temperature per Year, 1950-2019", 
             "Years", "Temperature (F)", 'ro', SCATTER_PLOT)
    PlotData(years, topLowVals, max(topLowVals), min(topLowVals), "Lowest Recorded Temperature per Year, 1950-2019", 
             "Years", "Temperature (F)", 'mo', SCATTER_PLOT)
    

# Create weather data dictionary    
weatherDataDictionary = ImportWeatherData()

# Calculate annual weather data averages
annualWeatherDataAvgsAndTotals = CalculateAnnualWeatherDataAveragesAndTotals(weatherDataDictionary)