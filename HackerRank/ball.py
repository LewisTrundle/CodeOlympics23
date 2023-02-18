# n=100
# a=1
# b=2
def boxes(n,a,b):
    if n<100 or n>200:
        return
    if a <1 or b >100:
        return
    removeCount = n - a
    addCount = removeCount + b
    return addCount

userInput = input("Enter in the form N A B")
n,a,b = [int(i) for i in userInput.split(' ')]

print(boxes(n,a,b))