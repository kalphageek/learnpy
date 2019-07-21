message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

counter = {}

for char in message:
    counter[char] = counter.setdefault(char, 0) + 1

print(counter)
