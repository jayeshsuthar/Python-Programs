def DecToBin(n):
    if n>1:
        DecToBin(n//2)

    print(n%2,end="")

if __name__ == '__main__':
    DecToBin(8)
    print("\r")
    DecToBin(18)
    DecToBin(4)
    print("\r")
    DecToBin(2)
