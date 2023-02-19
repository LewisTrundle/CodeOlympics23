# X, Y, A, B = 4, 20, 2, 10
X, Y, A, B = 1, 1000000000000000000, 10, 1000000000


def findExp(x,y,a,b):
    exp = 0
    strength = x
    while strength < y:
        # Check if going to the gym will increase STR too much
        if strength * a <= strength + b:
            strength *= a
            if strength > y:
                break
            exp += 1
        # Otherwise, go to the bar to increase STR
        else:
            strength += b
            if strength > y:
                break
            exp += 1
    print(exp)

findExp(X,Y,A,B)