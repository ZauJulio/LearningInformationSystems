import pandas as pd

import utils

dfGen01, dfGen02, dfWheather01, dfWheather02 = [
    pd.read_csv(
        "/home/zau/Desktop/UFRN_S/TAP3_2021.1/data/source/Plant_1_Generation_Data.csv",
        index_col="SOURCE_KEY"),
    pd.read_csv(
        "/home/zau/Desktop/UFRN_S/TAP3_2021.1/data/source/Plant_2_Generation_Data.csv",
        index_col="SOURCE_KEY"),
    pd.read_csv(
        "/home/zau/Desktop/UFRN_S/TAP3_2021.1/data/source/Plant_1_Weather_Sensor_Data.csv"),
    pd.read_csv(
        "/home/zau/Desktop/UFRN_S/TAP3_2021.1/data/source/Plant_2_Weather_Sensor_Data.csv")
]

# Removing the Plant_ID column (contains the same value throughout the dataset)

del dfGen01['PLANT_ID']
del dfGen02['PLANT_ID']

del dfWheather01['PLANT_ID']
del dfWheather02['PLANT_ID']

del dfWheather01['SOURCE_KEY']
del dfWheather02['SOURCE_KEY']


# Conversão da coluna em DateTime string para o tipo DateTime

dt_format = "%Y-%m-%d %H:%M:%S"

dfGen01['DATE_TIME'], dfGen02['DATE_TIME'] = [
    pd.to_datetime(
        dfGen01['DATE_TIME'],
        format='%d-%m-%Y %H:%M'),
    pd.to_datetime(
        dfGen02['DATE_TIME'],
        format=dt_format)
]

dfWheather01['DATE_TIME'], dfWheather02['DATE_TIME'] = [
    pd.to_datetime(
        dfWheather01['DATE_TIME'],
        format=dt_format),
    pd.to_datetime(
        dfWheather02['DATE_TIME'],
        format=dt_format)
]

# Separation of the date and time in different columns

dfGen01['DATE'], dfGen01['TIME'] = [
    dfGen01['DATE_TIME'].dt.date,
    dfGen01['DATE_TIME'].dt.time
]

dfGen02['DATE'], dfGen02['TIME'] = [
    dfGen02['DATE_TIME'].dt.date,
    dfGen02['DATE_TIME'].dt.time,
]

dfWheather01['DATE'], dfWheather01['TIME'] = [
    dfWheather01['DATE_TIME'].dt.date,
    dfWheather01['DATE_TIME'].dt.time,
]

dfWheather02['DATE'], dfWheather02['TIME'] = [
    dfWheather02['DATE_TIME'].dt.date,
    dfWheather02['DATE_TIME'].dt.time,
]

# Get sources

sources = {1: set(dfGen01.index), 2: set(dfGen02.index)}

sourcesGen01 = {
    "AC_POWER": utils.group_by_source_date(
        df=dfGen01,
        select_column="AC_POWER"
    ),
    "DC_POWER":    utils.group_by_source_date(
        df=dfGen01,
        select_column="DC_POWER"
    )
}

sourcesGen02 = {
    "AC_POWER": utils.group_by_source_date(
        df=dfGen02,
        select_column="AC_POWER"
    ),
    "DC_POWER":    utils.group_by_source_date(
        df=dfGen02,
        select_column="DC_POWER"
    )
}

print(dfWheather01.isna().sum())
print(dfWheather02.isna().sum())
print(dfGen01.isna().sum())
print(dfGen02.isna().sum())



sourcesDailyYield = {
    "gen01":    utils.group_by_source_date(
        df=dfGen01,
        select_column="DAILY_YIELD"
    ),
    "gen02":    utils.group_by_source_date(
        df=dfGen02,
        select_column="DAILY_YIELD"
    )
}

groupsWeather01 = {
    "AMBIENT_TEMPERATURE":utils.group_by_date(
        df=dfWheather01,
        select_column="AMBIENT_TEMPERATURE"
    ),
    "MODULE_TEMPERATURE":utils.group_by_date(
        df=dfWheather01,
        select_column="MODULE_TEMPERATURE"
    ),
    "IRRADIATION":utils.group_by_date(
        df=dfWheather01,
        select_column="IRRADIATION"
    )
}

groupsWeather02 = {
    "AMBIENT_TEMPERATURE":utils.group_by_date(
        df=dfWheather02,
        select_column="AMBIENT_TEMPERATURE"
    ),
    "MODULE_TEMPERATURE":utils.group_by_date(
        df=dfWheather02,
        select_column="MODULE_TEMPERATURE"
    ),
    "IRRADIATION":utils.group_by_date(
        df=dfWheather02,
        select_column="IRRADIATION"
    )
}

# Get by weekdays

# weekdays = {
#     1: utils.group_by_weekday(dfGen01),
#     2: utils.group_by_weekday(dfGen01)
# }

