t = open("D:\\Text.txt", 'r').read()

lines = []
with open("D:\\Text.txt") as t:
    lines = t.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')
