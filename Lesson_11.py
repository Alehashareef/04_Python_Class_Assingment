# Lesson 11: The Math & Date Time Calendar

import math
import datetime
import calendar

# Math module example
angle = 45
print(f"Sine of {angle} degrees:", math.sin(math.radians(angle)))
print("Logarithm of 1000 (base 10):", math.log10(1000))

# DateTime module example
current_time = datetime.datetime.now()
future_time = current_time + datetime.timedelta(days=30)
print("Current Date & Time:", current_time)
print("Date After 30 Days:", future_time)

# Calendar module example
year = 2025
print("Full Year Calendar (Created by Aleha Shareef):")
print(calendar.TextCalendar().formatyear(year))