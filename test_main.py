from random import randint
from unittest import TestCase

def draw(num = 10):
    i:int = 0
    while(i<num) :
        var = randint(0,100)
        result = []
        match var:
            case 1,2 : result.append("朝圣")
            case 3,4 : result.append("金")
            case _ :result.append("再接再厉")
    return result

result = draw()
print(result)