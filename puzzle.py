from random import randint

buttons = [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]

while not (
    (buttons[0] == 1) and (buttons[0] == buttons[1] == buttons[2] == buttons[3])
):

    for i in range(randint(1, 100)):
        buttons.append(buttons.pop(0))

    print("  ", buttons[0])
    print(buttons[3], "   ", buttons[1])
    print("  ", buttons[2])

    press = eval(input("Press: "))

    for i in press:
        if buttons[i - 1] == 0:
            buttons[i - 1] = 1
        else:
            buttons[i - 1] = 0
