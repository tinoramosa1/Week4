def rectangle():
    # ask user to enter length
    l = float(input('Enter the length of a Rectangle: '))

    # ask user to enter width
    b = float(input('Enter the width of a Rectangle: '))

    # formula for calculating area
    Area = l * b

    # printing final result
    print("Area of a Rectangle is: %.2f" % Area)


def circle():
    # initializing pi
    pi = 3.14

    # ask user to enter radius
    rad = float(input("Enter the radius of a circle:"))

    # formula for calculating area of circle
    area = pi * rad * rad

    # final result
    print("Area of a circle = %.2f" % area)


def sphere():
    # initialize pi
    pi = 22 / 7

    # ask user to enter radius of sphere
    rad = float(input('Radius of sphere: '))

    # formula for finding volume of sphere
    volume = (4 / 3) * (pi * rad ** 3)

    # final result
    print("Volume is: ", volume)


def celsius():
    # ask user to enter temp in celsius
    celsius = float(input("Temperature value in degree Celsius: "))

    # given formula
    Fahrenheit = (celsius * 1.8) + 32

    # print the result
    print('The %.2f degree Celsius is equal to: %.2f Fahrenheit' % (celsius, Fahrenheit))


def fahrenheit():
    # ask user to enter temperature in fahrenheit
    Fahrenheit = float(input('Temp in Fahrenheit '))

    # formula of converting fahrenheit to celcius
    Celsius = ((Fahrenheit - 32) * 5) / 9

    # final result
    print("Temperature in Celsius is: ");
    print(Celsius);


def quadratic():
    # import complex math module
    import cmath
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))


def distance():
    x1 = int(input("enter x1 : "))
    x2 = int(input("enter x2 : "))
    y1 = int(input("enter y1 : "))
    y2 = int(input("enter y2 : "))
    result = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    print("distance between", (x1, x2), "and", (y1, y2), "is : ", result)
