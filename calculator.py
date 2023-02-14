import PySimpleGUI as sg


def num_button(text):
    """Returns formatted Button types"""
    return sg.Button(text, size=(3, 1), font=("Times New Roman", "14"))


def clear():
    """Clears Display Text"""
    window["-DISPLAY-"].update("")


layout = [
    [
        sg.Text(
            "",
            expand_x=True,
            background_color="white",
            font=("Times New Roman", "14"),
            text_color="Black",
            key="-DISPLAY-",
            justification="right",
        )
    ],
    [num_button("n^2"), num_button("x^y"), num_button("/"), num_button("C")],
    [num_button("7"), num_button("8"), num_button("9"), num_button("*")],
    [num_button("4"), num_button("5"), num_button("6"), num_button("-")],
    [num_button("1"), num_button("2"), num_button("3"), num_button("+")],
    [num_button("+/-"), num_button("0"), num_button("."), num_button("=")],
]

sg.theme("BluePurple")

window = sg.Window("Simple Calculator", layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event in "1 2 3 4 5 6 7 8 9 0 .".split():
        display = window["-DISPLAY-"].get()
        display += event
        window["-DISPLAY-"].update(display)

    elif event == "n^2":
        display = window["-DISPLAY-"].get()
        n1 = float(display)
        window["-DISPLAY-"].update(n1**2)
        n1 = None

    elif event in ["x^y", "/", "*", "-", "+"]:
        display = window["-DISPLAY-"].get()
        n1 = float(display)
        window["-DISPLAY-"].update("")
        operation = event

    elif event == "=":
        display = window["-DISPLAY-"].get()
        n2 = float(display)
        operations = {
            "x^y": n1**n2,
            "/": n1 / n2,
            "*": n1 * n2,
            "-": n1 - n2,
            "+": n1 + n2,
        }
        output = operations[operation]
        n1 = output
        window["-DISPLAY-"].update(output)

    elif event == "+/-":
        display = window["-DISPLAY-"].get()
        display = float(display) * -1
        window["-DISPLAY-"].update(display)

    elif event == "C":
        clear()


window.close()
