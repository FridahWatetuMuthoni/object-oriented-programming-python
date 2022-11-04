# The difference b2n __str__ and __repr__
# __repr__ is for developers while __str__ is for customers
# Example
import datetime
today = datetime.datetime.now()
print(str(today))  # '2012-03-14 09:21:58.130922'
print(repr(today))  # 'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
