from datetime import datetime

dt = datetime.now()

print(dt.date())
print(dt.time())
#dt.microsecond


dt_string = datetime.now().strftime("%Y%m%d-%H:%M:%S")
print(dt_string)