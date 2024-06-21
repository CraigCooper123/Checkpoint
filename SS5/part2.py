# 1
# for i in range(3, 13, 1):
#     print(i)

# 2
# n = float(input("Please input a positive number: "))
# k = 0
# if n > 0:
#     while k <= n:
#         print(k, end=' ')
#         k += 1
# else:
#     print("Please input a positive number.")


# 3
# n = float(input("Please input a positive number: "))
# k = 1
# if n > 0:
#     while k <= n:
#         print(k, end=' ')
#         k += 2
# else:
#     print("Please input a positive number.")

# 4
import turtle

def draw_polygon(sides):
    angle = 360 / sides

    for _ in range(sides):
        turtle.forward(100)  
        turtle.right(angle) 

sides = int(input("Please input amount of sides: "))

draw_polygon(sides)

turtle.done()

