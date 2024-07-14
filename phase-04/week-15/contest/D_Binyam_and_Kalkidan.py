N = int(input())
num = input()

digits = []
for digit in num:
    if digit == '4':
        digits.extend(['3','2', '2'])
    elif digit == '6':
        digits.extend(['5', '3'])
    elif digit == '8':
        digits.extend(['7', '2', '2', '2'])
    elif digit == '9':
        digits.extend(['7', '3', '3', '2'])
    elif digit in "2357":
        digits.append(digit)

digits.sort(reverse=True)

print("".join(digits))