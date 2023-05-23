import nfl_data_py as nfl



years = [2022]  # Specify the year of the season you want to retrieve information about


season_info = nfl.import_seasonal_data(years)

printU(season_info.head())