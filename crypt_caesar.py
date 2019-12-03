def my_encode(in_str):
    res = crypt(in_str, 2, 1)
    return res


def my_decode(in_str):
    res = crypt(in_str, -2, -1)
    return res


def crypt(in_str, step, step1):
    alpha = ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ0123456789'
    res = ''
    digit = ''
    for c in in_str:
        if c.isalpha():
            if digit:
                res += str(int(digit) + int(step1))
                digit = ''
            res += alpha[(alpha.index(c) + step) % len(alpha)]
        elif c == ' ':
            if digit:
                res += str(int(digit) + int(step1))
                digit = ''
            res += c
        elif c.isnumeric():
            digit += c
        else:
            res += c
    if digit:
        res += str(int(digit) + int(step1))
    return res


if __name__ == "__main__":
    print("Hello")
