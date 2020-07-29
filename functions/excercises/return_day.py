'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
# this function creates a dictionary of numbers 1-7 and their associated days fhte week
# takes in day parameter, which is a integer
# checks if day is in dictionary and if so, returns day of the week
def return_day(day):
  day_of_week ={
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday',
    }
  if day in day_of_week:
    return day_of_week.get(day)
  



print(return_day(9))