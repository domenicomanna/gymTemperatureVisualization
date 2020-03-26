import pandas as pd

def cleanData(gymDataFrame: pd.DataFrame) -> pd.DataFrame:
    cleanedDataSet: pd.DataFrame = gymDataFrame.copy()
    cleanedDataSet = _removeUnnecessaryColumns(cleanedDataSet)
    return cleanedDataSet


def _removeUnnecessaryColumns(gymDataFrame: pd.DataFrame) -> pd.DataFrame:
    columnsToDrop: list[str] = ['timestamp', 'date', 'day_of_week', 'is_weekend',
                                'is_holiday', 'hour', 'is_start_of_semester', 'is_during_semester', 'month']
    gymDataFrame = gymDataFrame.drop(columnsToDrop, axis=1)
    return gymDataFrame

