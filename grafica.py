import random
import datetime
import matplotlib.pyplot as plt

def generate_random_glucose_data(start_date, end_date, min_glucose, max_glucose):
    """
    Generate random glucose data for consecutive days between start_date and end_date.

    Parameters:
        start_date (datetime.date): The start date for the data.
        end_date (datetime.date): The end date for the data.
        min_glucose (int): The minimum glucose value (mg/dL).
        max_glucose (int): The maximum glucose value (mg/dL).

    Returns:
        dates (list): List of dates.
        glucose_levels (list): List of random glucose levels corresponding to the dates.
    """
    dates = []
    glucose_levels = []

    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        glucose_levels.append(random.randint(min_glucose, max_glucose))
        current_date += datetime.timedelta(days=1)

    return dates, glucose_levels

def plot_glucose_data(dates, glucose_levels):
    """
    Plot glucose levels over time using Matplotlib.

    Parameters:
        dates (list): List of dates.
        glucose_levels (list): List of glucose levels corresponding to the dates.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dates, glucose_levels, marker='o', linestyle='-', color='r')
    plt.title('Glucose Levels Over Time')
    plt.xlabel('Date')
    plt.ylabel('Glucose Level (mg/dL)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define parameters
    start_date = datetime.date(2025, 1, 20)
    end_date = datetime.date(2025, 1,27)
    min_glucose = 70
    max_glucose = 180

    # Generate data
    dates, glucose_levels = generate_random_glucose_data(start_date, end_date, min_glucose, max_glucose)

    # Plot data
    plot_glucose_data(dates, glucose_levels)
