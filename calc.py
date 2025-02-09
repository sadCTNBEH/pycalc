def main(input: str):
    try:
        first = int(txt.split()[0])
        second = int(txt.split()[2])
        if txt.split()[3] != None:
            raise Exception("throws Exception")
        elif first < 1 or second < 1 or first > 10 or second > 10:
            raise Exception("throws Exception")
        else:
            match txt.split()[1]:
                case "+":
                    print(first + second)
                case "-":
                    print(first - second)
                case "*":
                    print(first * second)
                case "/":
                    print(first // second)
                case _:
                    raise Exception("throws Exception")
    except Exception as e:
        print("throws Exception")
