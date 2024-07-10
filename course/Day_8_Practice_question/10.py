# extract the temperature data of the week from the csv file and find the average temperature for each day

import pandas as pd

def calculate_average_daily_temperatures(csv_filename, time_interval_hours=6):
    try:
        # Step 1: Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_filename, parse_dates={'DateTime': ['Date', 'Time']})
        
        # Step 2: Set DateTime as index
        df.set_index('DateTime', inplace=True)
        
        # Step 3: Resample to 6-hour intervals and calculate mean temperature
        df_resampled = df.resample(f'{time_interval_hours}H').mean()
        
        # Step 4: Calculate average temperature for each day
        daily_averages = df_resampled.groupby(df_resampled.index.date)['Temperature'].mean()
        
        # Step 5: Print or return average daily temperatures
        for date, avg_temp in daily_averages.items():
            print(f"Average temperature on {date}: {avg_temp:.2f} °C")
        
        # Alternatively, return the daily_averages series if you want to use it further
        return daily_averages
    
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_filename}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse '{csv_filename}' as a CSV file.")
        return None

# Example usage:
csv_filename = 'D:\course\Day_8_Practice_question\\temperature_data.csv'
calculate_average_daily_temperatures(csv_filename, time_interval_hours=6)
