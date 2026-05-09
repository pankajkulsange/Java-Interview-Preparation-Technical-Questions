# String reverse program
str = 'hello'
rev = ''
for i in range(len(str)-1, -1, -1):
    rev += str[i]

print(rev)

reversed_str = str[::-1]
print(reversed_str)