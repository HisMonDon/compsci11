import math


def main():
    area = triangle_area(3, 3, 3)
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    area = triangle_area(3, 4, 5)
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    area = triangle_area(7, 8, 9)
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    area = triangle_area(5, 12, 13)
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    area = triangle_area(10, 9, 11)
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    area = triangle_area(8, 15, 17)
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")


def triangle_area(a: int, b: int, c: int) -> float:
    """Calculates a triangles area.
    
    Args:
        a: length of side a
        b: length of side b
        c: length of side c
    
    Returns:
        The area of the triangle
    """
    s = (a + b + c) // 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
    # ^ after computing the area, "return" it


if __name__ == "__main__":
    main()
"""
1. Yes, they both produce the same output.
2. The file with the function (This file) has 32 lines, while the other file has 49 lines.
3. It was easier to change the function, beacuse I didnt have to change every single occurence of the area calculator.
4. Yes, it was harder to change the file with the function
5.ok

"""
