import random
from typing import List


class CharacterPool:
    def __init__(self):
        self.pools = {
            "pilgrim": ["红莲", "诺亚", "白雪公主", "长发公主", "哈兰", "神罚", "桃乐丝", "伊莎贝尔"],
            "gold": ["麦斯威尔", "舒格", "艾可希雅", "爱丽丝", "艾玛", "尤妮", "普丽瓦蒂",
                    "普琳玛", "尤莉亚", "西格娜", "波莉", "米兰达", "布丽德", "索林", "迪塞尔",
                    "桑迪", "银华", "德雷克", "克拉乌", "梅里", "艾德米", "吉萝婷", "鲁德米拉",
                    "杨", "艾菲涅尔", "阿莉亚", "沃纶姆", "诺伊斯", "富克旺", "梅登", "丽塔",
                    "诺薇儿", "朵拉", "露菲", "尤尔夏", "米尔克", "佩珀", "贝斯蒂", "海伦",
                    "豺狼", "毒蛇", "饼干", "马斯特"],

            "up": ["当期up"],
            "purple": ["N102","米哈拉","艾瑟尔","拉毗","尼恩","德尔塔","阿尼斯","贝洛卡","米卡"],
            "blue": ["产品08","产品12","产品23","士兵E.G.","士兵F.A.","士兵O.W.","iDoll花","iDoll海","iDoll太阳"]
        }

    def get_types(self):
        return list(self.pools.keys())

    def get_characters(self, type_name):
        return self.pools.get(type_name, [])


# 抽卡权重配置：(类型名, 权重)
DRAW_WEIGHTS = [
    ("pilgrim", 50),
    ("up", 200),
    ("gold", 150),
    ("purple", 4300),
    ("blue", 5300)
]


def draw(num=10) -> List[str]:
    if not isinstance(num, int) or num <= 0:
        raise ValueError("抽卡次数必须是正整数")

    pool_manager = CharacterPool()
    results = []

    total_weight = sum(weight for _, weight in DRAW_WEIGHTS)

    try:
        for _ in range(num):
            rand_val = random.randint(1, total_weight)
            current_sum = 0
            selected_type = None

            for char_type, weight in DRAW_WEIGHTS:
                current_sum += weight
                if rand_val <= current_sum:
                    selected_type = char_type
                    break

            characters = pool_manager.get_characters(selected_type)
            if characters:
                results.append(random.choice(characters))
            else:
                raise RuntimeError(f"角色池 '{selected_type}' 为空")
    except Exception as e:
        raise RuntimeError("抽卡过程出错") from e

    return results
