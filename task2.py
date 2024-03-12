# import turtle
# def tree(branchLen,t):

#     if branchLen > 10:

#         t.forward(branchLen)

#         t.right(40)

#         tree(branchLen-30,t)

#         t.left(80)

#         tree(branchLen-30,t)

#         t.right(40)

#         t.backward(branchLen)
# def koch_curve(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [60, -120, 60, 0]:
#             koch_curve(t, order - 1, size / 3)
#             t.left(angle)

# def draw_koch_snowflake(order, size=300):
  
#     window = turtle.Screen()
#     window.bgcolor("teal")
#     t = turtle.Turtle()    

#     t.width(10)

#     t.left(90)

#     t.up()

#     t.backward(100)

#     t.down()

#     t.color("silver")

#     tree(150,t)

#     window.exitonclick()

#     for _ in range(3):
#         koch_curve(t, order, size)
#         t.right(120)  

#     window.mainloop()
   

 

import turtle

 

def tree(branchLen,t):

    if branchLen > 10:

        t.forward(branchLen)

        t.right(40)

        tree(branchLen-30,t)

        t.left(80)

        tree(branchLen-30,t)

        t.right(40)

        t.backward(branchLen)

 

def draw_tree(size):

    myWin = turtle.Screen()

    myWin.bgcolor("purple")

    t = turtle.Turtle()    

    t.width(10)

    t.left(90)

    t.up()

    t.backward(100)

    t.down()

    t.color("silver")
    
    tree(size,t)

    myWin.exitonclick()

 

def main():
    user_input =input("Please, specify the level of recursion >>>>>")
        
    if user_input.isdigit() and int(user_input) > 0:
        draw_tree(int(user_input))
    else:
        print('Invalid level. Enter the integer, please')
        main()


if __name__ == '__main__':
    main()
    
    """
    import turtle

def tree(branch_len, t):
    if branch_len > 10:
        t.forward(branch_len)
        t.right(40)
        tree(branch_len - 30, t)
        t.left(80)
        tree(branch_len - 30, t)
        t.right(40)
        t.backward(branch_len)

def draw_tree(size):
    my_win = turtle.Screen()
    my_win.bgcolor("purple")
    
    t = turtle.Turtle()
    t.width(10)
    t.left(190)
    t.up()
    t.backward(100)
    t.down()
    t.color("silver")
    
    for _ in range(3):
        tree(size, t)
        t.right(120)
    
    my_win.exitonclick()
    """