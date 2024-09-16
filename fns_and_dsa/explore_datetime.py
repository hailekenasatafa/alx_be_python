# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """
    Calculate and display the date after adding a specified number of days to the current date.

    Parameters:
    days (int): The number of days to add to the current date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
