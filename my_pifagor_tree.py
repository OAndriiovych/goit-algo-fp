import turtle

def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pifagor_tree(t, branch_length * 0.7, level - 1)
    t.right(90)
    draw_pifagor_tree(t, branch_length * 0.7, level - 1)
    t.left(45)
    t.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    turtle.speed(0)
    turtle.up()
    turtle.setpos(0, -400)
    turtle.down()
    turtle.left(90)
    draw_pifagor_tree(turtle, 200, level)
    turtle.mainloop()

if __name__ == "__main__":
    main()
