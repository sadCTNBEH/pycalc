def main(input: str):
    txt = input.split()
    if len(txt) != 3:
        raise Exception("throws Exception 0")
    try:
        first = int(txt[0])
        second = int(txt[2])
        op = txt[1]
    except ValueError:
        raise Exception("throws Exception 1")
    if not (1 <= first <= 10) or not (1 <= second <= 10):
        raise Exception("throws Exception 2")
    match op:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case "*":
            result = first * second
        case "/":
            result = first // second
        case _:
            raise Exception("throws Exception 3")
            
    return str(result)

if __name__ == "__main__":
    while True:
        checkInput = input("Проверка: ")
        output = main(checkInput)
        print(output)
