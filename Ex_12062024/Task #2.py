side1 = int(input("Enter the length of the first side of the triangle: "))
side2 = int(input("Enter the length of the second side of the triangle: "))
side3 = int(input("Enter the length of the third side of the triangle: "))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
