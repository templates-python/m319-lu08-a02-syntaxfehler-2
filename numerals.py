def run():
    decimals = [1, 4, 5, 9, 10, 40, 50, 90,
                100, 400, 500, 900, 1000]
    numerals = ["I", "IV", "V", "IX", "X", "XL",
                "L", "XC", "C", "CD", "D", "CM", "M"]
    position = 12

    number = user_input()
    while number:
        div = number // decimals[position]
        number %= decimals[position]

        while div:
            print(numerals[position], end="")
            div -= 1
        position -= 1


def user_input():
    input_string = input('Natürliche Zahl > ')
    while not input_string.isdigit():
        input_string = input('Eingabe muss eine natürliche Zahl sein > ')
    return int(input_string)


if __name__ == '__main__':
    run()