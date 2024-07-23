def convert_seconds(seconds):
    days = seconds // (24* 3600)
    hours = (seconds % (24 *3600)) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days,hours,minutes,seconds
seconds = int(input('input seconds: '))
days, hours, minutes, seconds = convert_seconds(seconds)
print(days, hours, minutes, seconds)