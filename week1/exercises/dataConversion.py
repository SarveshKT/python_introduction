# Data conversion operations

# integer to string

hour = 3
ones = hour % 10
tens = hour // 10
print (tens, ones, ":00")
print (str(tens), str(ones), ":00")
print (str(tens) + str(ones) + ":00")
