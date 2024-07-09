import datetime
now = datetime.datetime.now()
print("Current date and time:- ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y %I:%M:%S %p"))
print(now.strftime("%a, %b %d, %Y"))
print(now.strftime("%c"))
