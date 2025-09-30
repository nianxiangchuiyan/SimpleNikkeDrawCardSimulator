import random
from typing import List
from random import randint


class CharacterPool:
    def __init__(self):
        self.pools = {
            "pilgrim": ["红莲", "诺亚","白雪公主","长发公主","哈兰","神罚","桃乐丝","伊莎贝尔"],
            "gold": ["普通金"],
            "up": ["当期up"],
            "purple": ["紫"],
            "blue": ["蓝"]
        }

    def get_types(self):
        return list(self.pools.keys())

    def get_characters(self, type_name):
        return self.pools.get(type_name, [])

def draw(num=10):
    i: int = 0
    result = []
    # 定义各类型角色列表
    pilgrim = ["红莲", "诺亚","白雪公主","长发公主","哈兰","神罚","桃乐丝","伊莎贝尔"]  # 朝圣类型角色列表
    gold = ["普通金"]  # 金类型角色列表
    up = ["当期up"]  # up类型角色列表
    purple = ["紫"]  # 紫类型角色列表
    blue = ["蓝"]  # 蓝类型角色列表

    while (i < num):
        var = randint(1, 10000)
        if var <= 50:  # 0.5%概率抽到朝圣
            result.append(pilgrim[randint(0, len(pilgrim) - 1)])
        elif var <= 250:  # 2%概率抽到up
            result.append(up[randint(0, len(up) - 1)])
        elif var <= 400:  # 1.5%概率抽到金
            result.append(gold[randint(0, len(gold) - 1)])
        elif var <= 4700:  # 43%概率抽到紫
            result.append(purple[randint(0, len(purple) - 1)])
        else:  # 53%概率抽到蓝
            result.append(blue[randint(0, len(blue) - 1)])
        i += 1
    return result
