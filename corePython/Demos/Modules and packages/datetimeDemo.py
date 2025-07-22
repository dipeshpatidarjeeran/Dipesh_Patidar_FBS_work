import datetime

#### current date time
# d = datetime.datetime.now()
# print("current date and time:-",d)


#### get today date
# from datetime import date
# d = date.today()
# print("get today date:-",d)


#### timedelta(get future date)
# now = datetime.datetime.now()
# print(now + datetime.timedelta(days=7))


# str1 = '21-07-2025'
# date = datetime.datetime.strptime(str1, '%d-%m-%Y').date()
# print(date)

print(datetime.datetime.strptime('30-04-2025 10:23:10', '%d-%m-%Y %H:%M:%S'))