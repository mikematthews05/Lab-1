def main():
    # write your code here

    
    number_of_sides = (int(input("What is the number of sides? ")))
    exterior_angle = 360 / number_of_sides
    interior_angle = 180 - exterior_angle

    print("the exterior angle is", (exterior_angle),"and the interior angle is", (interior_angle), )



    return

if __name__ == '__main__':
    main()