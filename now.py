from datetime import date, timezone, datetime, timedelta
import pytz

today = date.today()
print(today)


# Set the time zone to Tijuana
tijuana_timezone = pytz.timezone('America/Tijuana')

# Get the current time in Tijuana
tijuana_time = datetime.now(tijuana_timezone)

# Format the time as a string
formatted_tijuana_time = tijuana_time.strftime('%Y-%m-%d %H:%M:%S')

print("Current time in Tijuana:", formatted_tijuana_time)
