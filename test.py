from random import randint


def draw(num = 10):
    i:int = 0
    result = []
    while(i<num) :
        var = randint(1,100)
        if var <=2: result.append("up")
        elif var<=4: result.append("金")
        else :result.append("再接再厉")
        i-=-1
    return result

