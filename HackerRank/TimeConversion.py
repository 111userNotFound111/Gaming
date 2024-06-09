"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Sample Input
07:05:45PM

Sample Output
19:05:45

"""

def timeConversion(s):
    # slice string for information
    unit = s[-2:]
    hour = int(s[:2])
    time = s[2:-2]
    # time conversion
    if unit == "PM" and hour < 12 :
        hour = hour + 12
    if unit == "AM":
        if hour == 12:
            hour = 0

    # make sure the digits are correct HH : MM : SS
    if len(str(hour)) != 2:
        hour = "{:02d}".format(hour)

    output = f"{hour}{time}"
    print(output)
    return output

if __name__ == "__main__":
    testcase = ":45:54PM"
    res = timeConversion(testcase)
    print(res)