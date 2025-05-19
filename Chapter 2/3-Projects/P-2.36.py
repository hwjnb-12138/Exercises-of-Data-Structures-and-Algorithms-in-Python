# Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish.
# The ecosystem consists of a river, which is modeled as a relatively large list. Each element of
# the list should be a Bear object, a Fish object, or None. In each time step, based on a random
# process, each animal either attempts to move into an adjacent list location or stay where it is.
# If two animals of the same type are about to collide in the same cell, then they stay where they are,
# but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously
#  None) location in the list. If a bear and a fish collide, however, then the fish dies (i.e., it disappears).
# 这个问题存在一些错误：1、没有考虑三只动物相遇的情况；2、同类相遇时产生新的实例随机放置在先前的空位，但先前的空位可能在一次移动后被其他动物占据了。
import random


class Fish:
    def __repr__(self):
        return 'F'


class Bear:
    def __repr__(self):
        return 'B'


class River:
    def __init__(self, size, bear_num, fish_num):
        self.size = size
        self.eco = [None] * size
        tmp = list(range(self.size))
        random.shuffle(tmp)
        for i in tmp[:bear_num]:
            self.eco[i] = Bear()
        for i in tmp[bear_num:bear_num+fish_num]:
            self.eco[i] = Fish()

    def move_record(self):
        move = []
        for idx, animal in enumerate(self.eco):
            if animal is None:
                continue
            # 随机选择移动方式
            direction = random.choice([-1, 0, 1])
            # 计算移动后的坐标
            target = idx + direction
            # 处理超出边界或保持不动的情况
            if target < 0 or target >= self.size or direction == 0:
                target = idx
            move.append((idx, animal, target))
        return move

    def handle_conflict(self, move):
        target_dic = {}
        change = []
        for idx, animal, target in move:
            target_dic.setdefault(target, []).append((idx, animal))
        for idc, candi in target_dic.items():
            # 没有冲突
            if len(candi) == 1:
                # 需要移动
                if idc != candi[0][0]:
                    change.append((idc, candi[0][1]))
                    change.append((candi[0][0], None))
            else:
                self.collision(idc, candi, change)
        return change

    def collision(self, target, candi, change):
        bears = [a for a in candi if isinstance(a[1], Bear)]
        fishes = [a for a in candi if isinstance(a[1], Fish)]
        # 先前的空位
        empty = [i for i in range(self.size) if self.eco[i] is None]

        # 当一个位置同时存在熊和鱼时（一熊一鱼、二熊一鱼、一熊二鱼）
        if bears and fishes:
            # 所有鱼消失
            for idx, _ in fishes:
                change.append((idx, None))
            # 二熊时，在空位产生新的熊
            if len(bears) == 2:
                new = random.choice(empty)
                change.append((new, Bear()))
                empty.remove(new)
            # 一熊时，仅移动熊
            elif len(bears) == 1:
                change.append((bears[0][0], None))
                change.append((target, Bear()))
        # 仅同类相遇时
        elif len(set(type(a) for _, a in candi)) == 1:
            new = random.choice(empty)
            change.append((new, candi[0][1]))
            empty.remove(new)

    def simulate(self):
        move_plans = self.move_record()
        change = self.handle_conflict(move_plans)
        for pos, animal in change:
            self.eco[pos] = animal

    def display(self):
        print("|" + "|".join(f"{'   ' if x is None else str(x):^3}" for x in self.eco) + "|")


if __name__ == "__main__":
    river = River(15, 3, 3)
    print("初始河流状态：")
    river.display()

    for _ in range(3):
        river.simulate()
        print(f"\n第 {_ + 1} 个时间步后：")
        river.display()
