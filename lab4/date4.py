from datetime import datetime

date1 = datetime(2023, 5, 15, 12, 0, 0)  
date2 = datetime(2023, 5, 20, 14, 30, 0)  

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()

print("Difference between the two dates in seconds:", difference_in_seconds)
