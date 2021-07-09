import os
str = ""

words = []
numbers = []
numbers_raised = []
numbers_max = 0

str = input("Input your string: ")

for w in str.split():
    if w.isdigit():
        numbers.append(int(w))
    else:
        words.append(w)
str = " ".join(words)

print("\nOnly words:\n   ", str)

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:-1] + words[i][-1].upper()
str = " ".join(words)

print("\nUpdated string with uppercase letters:\n   ", str)

numbers_max = max(numbers)
print("\nJust numbers:", numbers)
print("The max number:", numbers_max)

print("Raised to index:")
for i in range(len(numbers)):
    if numbers[i] != numbers_max:
        print("   ", numbers[i], "**", i, "=", numbers[i] ** i)
        numbers_raised.append(numbers[i] ** i)
    else:
        print("   ", numbers[i], "is max(without changes).")


print("\nResult:", numbers_raised)

os.system("pause")
