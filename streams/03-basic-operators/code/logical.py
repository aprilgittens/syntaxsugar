# AND - both must be True
age = 25
has_license = True
can_rent_car = age >= 21 and has_license
# print(can_rent_car)

# OR - at least one must be True
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
# print(can_sleep_in)

# NOT - flip the value
is_raining = False
is_sunny = not is_raining
# print(is_sunny)

# Combining them
temperature = 75
is_nice_weather = temperature > 65 and temperature < 85 and not is_raining
# print(is_nice_weather)