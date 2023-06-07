from datetime import datetime, timedelta


# start = datetime(2022, 2, 2, 0, 0, 0)
start = datetime(1985, 12, 11, 0, 0, 0)
today = datetime.today()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
date_time = start

square_meters = 0
while date_time < today:
    duration = date_time - start
    duration_in_s = duration.total_seconds()
    years = int(divmod(duration_in_s, 31536000)[0])
    date_time += timedelta(days=1)
    square_meters += years
    # print(date_time, years, square_meters)
# print(date_time, today, square_meters)
print(square_meters)
