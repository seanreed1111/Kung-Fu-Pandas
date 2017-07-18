def describetriangle():

    side1 = input(("Enter the length of side 1: "))
    side2 = input(("Enter the length of side 2: "))
    side3 = input(("Enter the length of side 3: "))

    if ((side1 == side2) and (side2 == side3) and (side1 == side3)):
       print("The triangle is equilateral.")
    elif ((side1 == side2) or (side2 == side3) or (side1==side3)):
       print("The triangle is isosceles.")
    else:
       print("The triangle is scalene.")

describetriangle()      
