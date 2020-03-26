from clean import cleanData
from extract import extractAverageNumberOfPeopleAtEveryTemperatureRange
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

 
def main():
    originalDataSet: pd.DataFrame = pd.read_csv('./gymDataSet.csv')
    cleanedDataSet: pd.DataFrame = cleanData(originalDataSet)
    averageNumberOfPeopleAtEveryTemperature: Pd.DataFrame = extractAverageNumberOfPeopleAtEveryTemperatureRange(
        cleanedDataSet
    )
    averageTemperatue = averageNumberOfPeopleAtEveryTemperature['averageTemperature'].tolist()
    averageNumberOfPeople = averageNumberOfPeopleAtEveryTemperature['averageNumberOfPeople'].tolist()

    polynomialCoefficients = np.polyfit(averageTemperatue, averageNumberOfPeople, 3)
    polynomialFunction = np.poly1d(polynomialCoefficients)

    evenlySpacedTemperatureSamples = np.linspace(averageTemperatue[0], averageTemperatue[-1], 100)
    populationBasedOnPolynomial = polynomialFunction(evenlySpacedTemperatureSamples)

    print(f"Polynomial model: \n {polynomialFunction}")
    plt.plot(averageTemperatue, averageNumberOfPeople, 'o')
    plt.plot(evenlySpacedTemperatureSamples, populationBasedOnPolynomial, label='curve of best fit')
    plt.legend(loc="upper left")
    plt.title('Gym Population VS. Temperature')
    plt.xlabel('Temperature (in degrees)')
    plt.ylabel('Number of People')
    plt.show()


main()
