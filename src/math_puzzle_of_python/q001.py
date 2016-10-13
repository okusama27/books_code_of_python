"""10進数, 8進数, 2進数の回文"""


def check_num(num):
    s10 = str(num)
    s8 = str(oct(num))[2:]
    s2 = str(bin(num))[2:]

    if s10 == ''.join(reversed(s10)):
        if s8 == ''.join(reversed(s8)):
            if s2 == ''.join(reversed(s2)):
                print(s10, s8, s2)
                return True
    return False


def main():
    i = 10
    while True:
        if check_num(i):
            break
        i += 1
    print(i)


if __name__ == '__main__':
    main()
