
from datetime import datetime, timedelta
from dateutil import parser



def calculate_future_date(task_date, dias):
	input_date = datetime.strptime(task_date, "%Y-%m-%d")
	future_date = input_date + timedelta(days=dias)
	return future_date



task_date = input("Enter the day to perform your task as YYYY-MM-DD: ")

dias = int(input("Enter the number of days your task expires: "))

try:
	result_date = calculate_future_date(task_date, dias)
	print(f"The future date from {task_date} after {dias} days will be: {result_date.strftime('%Y-%b-%d')}")

except ValueError:
	print("Invalid date format. Please use the format 'YYYY-MM-DD'.")
except Exception as e:
	print(f"An error occurred: {e}")
