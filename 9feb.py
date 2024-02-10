
numbers = [4, -4, 6, -5, 1, -1]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} x')
    else:
        print(f'{position} {number}')