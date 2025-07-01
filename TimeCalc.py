# this is the second project from freecodecamp

def convert_time_12h_format(s_time,dur,_12h_format):

    time_sum = []
    day = 0
    # sum the hours and minutes separately
    for i,j in zip(s_time,dur):
        time_sum.append(i+j)

    if time_sum[1] > 60:
        # if the minutes are greater than 60, add the reminder to the minutes and add 1 to the hour
        time_sum[1] %= 60
        time_sum[0] += 1

    print(time_sum)
    print(time_sum[0]/12)
    print(time_sum[0]/24)
    if time_sum[0]/12 > 1 and _12h_format == 'PM':
        day += round(time_sum[0]/24)
    elif time_sum[0]/24 > 1 and _12h_format == 'AM':
        day += round(time_sum[0]/24)


    

    print(day)

    #if _12h_format == 'AM' and day == 1:


    aRp_determine = time_sum[0]//12

    if aRp_determine%2 != 0:
        if _12h_format == 'AM':
            _12h_format = 'PM'
        else:
            _12h_format = 'AM'
    # subtract the number of days from the summed time
    if time_sum[0] > 12:
        time_sum[0] %= 12

    if time_sum[0] % 12 == 0:
        time_sum[0] = 12

    print(time_sum)
    return [str(x) for x in time_sum], day, _12h_format

        


def add_time(start, duration, day=None):

    # final time 
    final_time = []

    # start time is a 12h format with AM or PM in the end eg: 3:10 PM
    # AM or PM
    am_or_pm = start.split(' ')[-1]
    print(am_or_pm)

    # remove am or pm tag from the time
    start = start.replace(am_or_pm,'')

    # split hours and minutes and convert them to int for ease of calculation
    start_split = [int(x.strip()) for x in start.split(':')]
    # split duration into hours and minutes
    duration_split = [int(x.strip()) for x in duration.split(':')]
    
    final_time, day_num, aRp = convert_time_12h_format(start_split,duration_split,am_or_pm)

    # making sure that the minutes is always displayes in 2 digits
    final_time[1] = final_time[1].zfill(2)

    # combining hours and minutes into a single string
    final_time = ':'.join(final_time)

    # add the additional day statement
    if day_num == 1:
        day_statement = f" (next day)"
    elif day_num < 1:
        day_statement = ""
    else:
        day_statement = f" ({day_num} days later)"

    if day is None:
        final_time = f"{final_time} {aRp}{day_statement}"
    else:
        day_of_week = [i for i,x in enumerate(DAYS_OF_WEEK) if x.lower() == day.lower()][0]
        select_day = (day_of_week + day_num)%7
        final_day = DAYS_OF_WEEK[select_day]
        final_time = f"{final_time} {aRp}, {final_day}{day_statement}"
        
        
    
    # return the final time
    return final_time 

DAYS_OF_WEEK = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


# print(add_time('3:00 PM', '3:10'))
# # Returns: 6:10 PM
# print('--------------------------------')
# print(add_time('11:30 AM', '2:32', 'Monday'))
# # Returns: 2:02 PM, Monday
# print('--------------------------------')
# print(add_time('11:43 AM', '00:20'))
# # Returns: 12:03 PM
# print('--------------------------------')
# print(add_time('10:10 PM', '3:30'))
# # Returns: 1:40 AM (next day)
# print('--------------------------------')
# print(add_time('11:43 PM', '24:20', 'tueSday'))
# # Returns: 12:03 AM, Thursday (2 days later)
# print('--------------------------------')
# print(add_time('6:30 PM', '205:12'))
# # Returns: 7:42 AM (9 days later)

# tests

print(add_time('2:59 AM', '24:00', 'saturDay'))