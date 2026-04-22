# # wap to enter a string to count  uppercase  vowels
def count_uppercase_vowels(s):
    count=0
    for char in s:
        if char in 'AEIOU':
            count=count+1
    return count
string=input("Enter a string: ")
result=count_uppercase_vowels(string)
print("Number of uppercase vowels in the string:", result)


