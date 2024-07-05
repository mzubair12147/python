import time

# epoch : a date and time from which a computer measures system time
# a time , when the computer thinks the time begin (reference point)


# ctime converts a time expressed in seconds since epoch to a readable string
# print(time.ctime(10000000000))
# print(time.time())  # returns the current no. of seconds passed since epoch
# print(time.ctime(time.time()))  # get the current time in strings

# creates a time object based on the current time (struct time object, made up of different keywords)
timeObj = time.localtime()

# formating time object
# time.strftime(format, time_object)
local_time = time.strftime("%B %d %Y %H:%M", timeObj)
# print(local_time)

# getting the UTC time
# UTC time: coordinated universal time is the primary time standard by which the world regulates clock and time.
# it is within about 1 second of mean solar time at 0 degree longitude, and is not adjusted for daylight saving time
timeObj2 = time.gmtime()  # UTC time object
# print(timeObj2)

# it takes a string input representing a time and returns a time object
time_string = "20 april, 2000"
timeObj3 = time.strptime(time_string, "%d %B, %Y")
# print(timeObj3)

# this function accepts a time object or a tuple representation of a relative time
# (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_tuple = (2003, 9, 20, 10, 30, 0, 0, 0, 0)
time_string2 = time.asctime(time_tuple)
# print(time_string2)


# mktime takes time and convert it into seconds since epoch
time_tuple = (2003, 9, 20, 10, 30, 0, 0, 0, 0)
seconds_time = time.mktime(time_tuple)
print(seconds_time)
