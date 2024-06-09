
def standard_digit(str_input):
    str_output = str_input
    if len(str_input) == 1:
        str_output = f'0{str_input}'
    return str_output 

def day_conversion(day_input):
    day = day_input[0:-2]
    day = standard_digit(day)
    return day

def month_conversion(month_input):
    month_input = month_input.lower()
    month_conversion_dict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    month = month_conversion_dict[month_input]
    month = str(month)
    month = standard_digit(month)
    return month

# convert the date to YYYY-MM-DD
def preprocessDate(dates):
    res_list = []
    # read str
    for date in dates:
        date_list = date.split(' ')
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        # day conversion
        res_day = day_conversion(day)
        # month conversion 
        res_month = month_conversion(month)
        # combine str 
        res = f"{year}-{res_month}-{res_day}"
        res_list.append(res)
        
    return res_list


if __name__ == "__main__":
    dates = [
    "20th Oct 2052",
    "6th Jun 1933",
    "26th May 1960",
    "20th Sep 1958",
    "16th Mar 2068",
    "25th May 1912",
    "16th Dec 2018",
    "26th Dec 2061",
    "4th Nov 2030",
    "28th Jul 1963"
    ]
    print(preprocessDate(dates))