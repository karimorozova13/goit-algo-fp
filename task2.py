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
        
    if not user_input.isdigit():
        print('Invalid level. Enter the integer, please')
        main()
    elif int(user_input) < 100:
        print('Invalid level. Enter the number more then 100, please')
        main()
    else:
        draw_tree(int(user_input))


if __name__ == '__main__':
    main()