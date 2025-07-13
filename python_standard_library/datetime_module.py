from datetime import datetime
import time

# google: python3 strptime for documentation

# different ways to create a datetime object
dt1 = datetime(2024, 4, 6)
dt2 = datetime.now()
# parsing
dt = datetime.strptime
dt = datetime.strptime("2025/06/05", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)
