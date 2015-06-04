# computes the area of triangle

def triangle_area(base, height):
    area = (1.0 / 2) * base * height
    return area


# print triangle_area(2, 2)

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# print fahrenheit2celsius(32)
# print fahrenheit2celsius(212)

def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# print(fahrenheit2kelvin(32))
# print(fahrenheit2kelvin(212))

def hello():
    print "Hello, world!"

h = hello()
print h
