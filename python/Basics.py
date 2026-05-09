# String reverse program
str = 'hello'
rev = ''
for i in range(len(str)-1, -1, -1):
    rev += str[i]

print(rev)

reversed_str = str[::-1]
print(reversed_str)

# string is  palindrome or not
# str1 = "madam" # palindrome string
str1 = "Pankaj" #non palindrome string
rev_str1 = ""
for i in range(len(str1)-1, -1, -1):
    rev_str1 += str1[i]
if str1 == rev_str1:
    print("Palindrome")
else:
    print("Not a Palindrome")
# build in method
if str1 == str[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")