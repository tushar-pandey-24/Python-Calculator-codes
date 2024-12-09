def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

first_num = float(input("What's the first number?: "))

while True:
    for symbols in operations:
        print(symbols)

    operation_symbol = input("Choose an operation from the above: ")

    next_num = float(input("What's the next number?: "))

    calculation = operations[operation_symbol]

    answer = calculation(first_num, next_num)

    print(f"{first_num} {operation_symbol} {next_num} = {answer}")

    if input("Do you want to continue with the answer?: ") == "no":
        break
    else:
        first_num = answer
