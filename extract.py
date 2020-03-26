import pandas as pd


def extractAverageNumberOfPeopleAtEveryTemperatureRange(gymDataFrame: pd.DataFrame) -> pd.DataFrame:
    gymDataFrame['temperatureRange'] = pd.cut(gymDataFrame['temperature'], 10)
    gymDataFrame = gymDataFrame.groupby(gymDataFrame['temperatureRange']).mean()
    gymDataFrame = gymDataFrame.rename({'number_people': 'averageNumberOfPeople', 'temperature': 'averageTemperature'}, axis=1)
    return gymDataFrame
