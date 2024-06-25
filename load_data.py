#Import data from file
import polars as pl

DATA_FILE = 'AirQuality.csv'
WINDOW_SIZE = 10

def read_file_to_df(file_name, sep):
    df_air = pl.read_csv(file_name, separator=sep)
    df = df_air.drop_nulls(subset="Date")
    # Combine Date and Time columns into a single datetime string
    df = df.with_columns((pl.col("Date") + " " + pl.col("Time")).alias("DateTimeString"))
    # Convert the combined string to a datetime object
    df = df.with_columns(pl.col("DateTimeString").str.to_datetime(pl.Datetime).alias("DateTime"))
    # # Drop the intermediate DateTimeString column if not needed
    # df = df.drop("DateTimeString")
    return df

def create_time_windows_dataframe():
    return None

def transform_data_into_time_windows(df, window_size):
    df_win = []
    return df_win


df_air = read_file_to_df(DATA_FILE, ";")
df_win = transform_data_into_time_windows(df_air, WINDOW_SIZE)

print(df_air)