### program to convert days into vyear,week and days 
 
## INPUT VALUE
days=int(input( "enter the nmber of days"))

year=days//365
days=remaining_days= days % 365
week=remaining_week= 365 / 7

print('year',year)
print('remaining_days',remaining_days)
print('remaining_week',remaining_week)
