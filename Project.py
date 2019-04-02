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


# Define const variables
LEAP_YEARS = ("1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", 
              "1984", "1988", "1992", "1996", "2000", "2004", "2008", "2012", "2016")


# Plot Function
def PlotData(xValues, yValues, title, xAxisLabel, yAxisLabel):
    
    # Clear data from plot object
    plt.clf()
    
    plt.plot(xValues, yValues, 'r-')
    plt.axis([1950, 2019, 0, 100])
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

# 
def CalculateAnnualWeatherDataAveragesAndTotals(weatherDict):
    
    print("Calculating yearly averages and Totals...")
    
    # Create Annual Weather Data Averages Dictionary
    AnnualAvgsDictionary = {}
    
    # Loop through each day in the weather dictionary
    count = 0
    
    # Get the date of the first day
    key = list(weatherDict.keys())[count]
    lengthOfKey = len(key)
    
    # Get the year of the first day
    currentYear = int(key[lengthOfKey - 4] + key[lengthOfKey - 3] + key[lengthOfKey - 2] + key[lengthOfKey - 1])
    
    # Define averaging values
    prcpTotals = 0.0
    highTmpTotals = 0.0
    lowTmpTotals = 0.0
    snowTotals = 0.0
    totalHighs = 0
    totalLows = 0
    
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
            
            if (readings[1] != ""):    
                snowTotals = snowTotals + float(readings[1])
            
            if (readings[2] != ""):
                highTmpTotals = highTmpTotals + float(readings[2])
                totalHighs = totalHighs + 1
            
            if (readings[3] != ""):
                lowTmpTotals = lowTmpTotals + float(readings[3])
                totalLows = totalLows + 1
                
                
        else:
            # Increment to the next year
            currentYear = currentYear + 1
            
            highTmpAvg = highTmpTotals/totalHighs
            lowTmpAvg = lowTmpTotals/totalLows
                
            # Create tuple for the annual averages dictionary
            yearAvgs = (prcpTotals, snowTotals, highTmpAvg, lowTmpAvg)
            
            # Reset averaging values
            prcpTotals = 0.0
            highTmpTotals = 0.0
            lowTmpTotals = 0.0
            snowTotals = 0.0
            totalHighs = 0
            totalLows = 0
            
            
            # Add to dictionary
            AnnualAvgsDictionary[year] = yearAvgs
        
        # Increment overall day counter
        count = count + 1
    
    # Plot results
    prcpVals = []
    snowVals = []
    highVals = []
    lowVals = []
    years = []
    
    
    # Prepare data for plotting
    for key, value in AnnualAvgsDictionary.items():
        years.append(key)
        prcpVals.append(value[0])
        snowVals.append(value[1])
        highVals.append(value[2])
        lowVals.append(value[3])
    
    # Plot data
    PlotData(years, prcpVals, "Precipitation Totals 1950 to 2019", "Years", "Precipitation Levels (inches)")
    PlotData(years, snowVals, "Snow Totals 1950 to 2019", "Years", "Snow Levels (inches)")
    PlotData(years, highVals, "Average Annual High Temperature 1950 to 2019", "Years", "Temperature (F)")
    PlotData(years, lowVals, "Average Annual Low Temperature 1950 to 2019", "Years", "Temperature (F)")

# Create weather data dictionary    
weatherDataDictionary = ImportWeatherData()

# Calculate annual weather data averages
annualWeatherDataAvgsAndTotals = CalculateAnnualWeatherDataAveragesAndTotals(weatherDataDictionary)