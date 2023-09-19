# Time Calculator - Victor Freire(devbuda)

def add_time(start, duration, start_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    duration_hour, duration_minute = map(int, duration.split(':'))

    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    new_minutes = total_minutes % (24 * 60)
    days_later = total_minutes // (24 * 60)

    new_period = "PM" if new_minutes >= 12 * 60 else "AM"

    new_hour = new_minutes // 60 % 12
    new_minute = new_minutes % 60

    if new_period == "AM" and new_hour == 0:
        new_hour = 12

    if start_day:
        start_day = start_day.lower().capitalize()
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]

        result = f"{new_hour}:{new_minute:02} {new_period}, {new_day}"
    else:

        result = f"{new_hour}:{new_minute:02} {new_period}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    
    return result
