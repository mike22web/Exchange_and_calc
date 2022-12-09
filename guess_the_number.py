import random

print('Welcome to the game "Guess the number"')
number = random.randint(1, 100)


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


left = 0
right = 101
middle = (left + right) // 2
counter = 1
print("Well, try to guess")

while True:
    range_numbers = f'Our number is greater than {left} and less than {right}'
    print(range_numbers)
    digit = input(f"enter a number from {left+1} to {right-1}: ")
    if is_valid(digit):
        num = int(digit)
        if num == number:
            print(f"Congratulations, you guessed the number with {counter} attempts")
            break
        elif number < num:
            if (num - number) <= 5:
                print(f"almost guessed it, but the hidden number is less than {num}")
                right = num
                counter += 1
                continue
            else:
                print(f"no, the hidden number is less than {num}")
                right = num
                counter += 1
                continue
        elif number > num:
            if (number - num) <= 5:
                print(f"almost guessed it, but the hidden number is more than {num}")
                left = num
                counter += 1
                continue
            else:
                print(f"no, the hidden number is more than {num}")
                left = num
                counter += 1
                continue
    else:
        print("Error, so nothing will happen")
        continue
