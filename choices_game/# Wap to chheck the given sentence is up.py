# Wap to chheck the given sentence is uppercase or not
sen=input("Enter a sentense:")
lowercase=0
uppercase=0
for i in sen:
    if i.islower():
        lowercase+=1
    else:
      uppercase+=1
print(lowercase,uppercase)