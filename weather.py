import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    try:
        # Parse the ISO date string into a datetime object
        date_obj = datetime.fromisoformat(iso_string)

        # Format the datetime object into the desired human-readable format
        formatted_date = date_obj.strftime("%A %d %B %Y")

        return formatted_date
    except ValueError:
        return "Invalid date format"
    pass


def convert_f_to_c(temp_in_fahrenheit):

    # """Converts an temperature from farenheit to celcius.
    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """

    temp_in_celsius = (float(temp_in_fahrenheit) - 32 )  * 5/9
    temp_in_celsius1dp = round(temp_in_celsius, 1)

    # print(temp_in_celsius1dp)
    return temp_in_celsius1dp

    pass



def calculate_mean(weather_data):
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """

    my_weather_data = [float(item) for item in weather_data]
    
    mean_value = sum(my_weather_data) / len(my_weather_data)
    return mean_value
    pass




def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
# csv_files = ["tests\data\example_one.csv", "tests\data\example_three.csv", "tests\data\example_two.csv"]

    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        data = [] 
        for row in reader:
            if len (row)==0:
                continue
            else:
                data.append([f"{row[0]}", int(row [1]), int(row [2])])
                
            # print(data)  # Properly indented return statement within the function
        return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    new_min_data = [float(item) for item in weather_data]

    if not new_min_data:
        return ()

    min_value = min(new_min_data)

    for i in range(len(new_min_data) - 1, -1, -1):
        if new_min_data[i] == min_value:
            min_index = i
            break


    return min_value, min_index



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.
    
    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    new_max_data = [float(item) for item in weather_data]

    if not new_max_data:
        return ()

    max_value = max(new_max_data)

    for i in range(len(new_max_data) - 1, -1, -1):
        if new_max_data[i] == max_value:
            max_index = i
            break
   
    return max_value, max_index
pass



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    if not weather_data:
        return None

    lowest_temp = float('inf')
    lowest_temp_date = ""
    highest_temp = float('-inf')
    highest_temp_date = ""
    total_low_temp = 0
    total_high_temp = 0

    for day in weather_data:
        date_str, low_temp_fahrenheit, high_temp_fahrenheit = day
        date_obj = datetime.fromisoformat(date_str)

        # Convert temperatures from Fahrenheit to Celsius
        high_temp = (high_temp_fahrenheit - 32) * (5/9)
        low_temp = (low_temp_fahrenheit - 32) * (5/9)

        if low_temp < lowest_temp:
            lowest_temp = low_temp
            lowest_temp_date = date_obj.strftime("%A %d %B %Y")
        if high_temp > highest_temp:
            highest_temp = high_temp
            highest_temp_date = date_obj.strftime("%A %d %B %Y")

        total_low_temp += low_temp
        total_high_temp += high_temp

    average_low_temp = total_low_temp / len(weather_data) 
    average_high_temp = total_high_temp / len(weather_data) 

    summary = f"{len(weather_data)} Day Overview\n"
    summary += f"  The lowest temperature will be {lowest_temp:.1f}°C, and will occur on {lowest_temp_date}.\n"
    summary += f"  The highest temperature will be {highest_temp:.1f}°C, and will occur on {highest_temp_date}.\n"
    summary += f"  The average low this week is {average_low_temp:.1f}°C.\n"
    summary += f"  The average high this week is {average_high_temp:.1f}°C.\n"
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summaries = []

    for day in weather_data:
        date_str, low_temp_fahrenheit, high_temp_fahrenheit = day
        date_obj = datetime.fromisoformat(date_str)

        # Convert temperatures from Fahrenheit to Celsius
        high_temp = (high_temp_fahrenheit - 32) * 5/9
        low_temp = (low_temp_fahrenheit - 32) * 5/9

        # Format the date
        formatted_date = date_obj.strftime("%A %d %B %Y")

        # Create a daily summary
        daily_summary = f"---- {formatted_date} ----\n"
        daily_summary += f"  Minimum Temperature: {low_temp:.1f}°C\n"
        daily_summary += f"  Maximum Temperature: {high_temp:.1f}°C\n\n"

        
        # Append the daily summary to the list
    # for day in weather_data:
        daily_summaries.append(daily_summary)

    daily_summaries.append("")

    # for summary in daily_summaries:
    # print("".join(daily_summaries))

    return ("".join(daily_summaries))
    pass
