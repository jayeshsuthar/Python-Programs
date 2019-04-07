class error(Exception):
    pass
class smallError(error):
    pass
class largeError(error):
    pass

number = 10

while True:
    try:
        num = int(input('Enter the number'))
        if num < number:
            raise smallError
            break
        elif num > number:
            raise largeError
            break
    except smallError:
        print('Too small value')
    except largeError:
        print('Large value')
