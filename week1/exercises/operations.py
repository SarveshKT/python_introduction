# get the ones digit of a number
num = 49
tens = num // 10
ones = num % 10
# print tens, ones
# print 10 * tens + ones

# 24 hour clock
hour = 20
shift = 8
# print (hour + shift) % 24

# screen wraparound
width = 800
position = 797
move = 5
position = (position + move) % width
print position
