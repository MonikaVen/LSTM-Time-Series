#Import data from file
import polars as pl

DATA_FILE = 'AirQuality.csv'
WINDOW_SIZE = 10

def read_file_to_df(file_name, sep):
    df_air = pl.read_csv(file_name, separator=sep)
    return df_air

def transform_data_into_time_windows(df, window_size):
    return df_win


df_air = read_file_to_df(DATA_FILE, ";")
df_win = transform_data_into_time_windows(df_air, WINDOW_SIZE)

print(df_air)