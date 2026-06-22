import pandas as pd


def group_by_weekday(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Group by weekday

    Parameters
    ----------
    df : pd.DataFrame
        data source

    Returns
    -------
    dict[str, pd.DataFrame]
        Time     |  2020-05-15
        _______________________
        00:00:00 | selectColumn
        00:00:15 | selectColumn
        00:00:30 | selectColumn
    """
    __df = df.copy()
    __df["WEEKDAY"] = __df['DATE_TIME'].dt.dayofweek

    return {group[0]: group[1] for group in df.groupby(__df["WEEKDAY"])}


def group_by_source_date(df: pd.DataFrame, select_column: str = "AC_POWER") -> dict[str, pd.DataFrame]:
    """Group by SOURCE_KEY and DATE

    Parameters
    ----------
    df : pd.DataFrame
        data source

    select_column : str, optional, Defaults to "AC_POWER"
        Column to get by group.

    Returns
    -------
    dict[str, pd.DataFrame]
        [key=SOURCE_KEY]

        Time     |  2020-05-15
        _______________________
        00:00:00 | selectColumn
        00:00:15 | selectColumn
        00:00:30 | selectColumn
    """
    __df_sources = {}

    for group in df.groupby(["SOURCE_KEY", "DATE"]):
        date = group[1]["DATE"][0]
        source = group[0][0]

        data = pd.DataFrame(
            data=group[1][select_column].to_list(),
            index=group[1]["TIME"],
            columns=[date]
        )

        data.index = pd.to_datetime(data.index,  format='%H:%M:%S')

        if source not in __df_sources:
            __df_sources.update({source: data})
        else:
            __df_sources[source][date] = data

    return __df_sources


def group_by_date(df: pd.DataFrame, select_column: str) -> pd.DataFrame:
    """Group by SOURCE_KEY and DATE

    Parameters
    ----------
    df : pd.DataFrame
        data source

    select_column : str, optional, Defaults to "AC_POWER"
        Column to get by group.
    Returns
    -------
    pd.DataFrame
        Time     |  2020-05-15
        _______________________
        00:00:00 | selectColumn
        00:00:15 | selectColumn
        00:00:30 | selectColumn
    """
    _df = None

    for group in df.groupby(["DATE"]):
        data = pd.DataFrame(
            data=group[1][select_column].to_list(),
            index=group[1]["TIME"],
            columns=[group[0]]
        )

        if _df is not None:
            _df[group[0]] = data
        else:
            _df = data

    _df.index = pd.to_datetime(_df.index,  format='%H:%M:%S')

    return _df
