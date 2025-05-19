# Write a simulator, as in the previous project, but add a Boolean gender
#  field and a floating-point strength field to each animal, using an Animal
#  class as a base class. If two animals of the same type try to collide, then
#  they only create a new instance of that type of animal if they are of differ-
# ent genders. Otherwise, if two animals of the same type and gender try to
#  collide, then only the one of larger strength survives.
import random


class Animal:

    def __init__(self):
        self.gender = random.choice([0, 1])
        self.strength = random.choice([0, 100.0])


class Fish(Animal):
    def __repr__(self):
        return 'F' if self.gender else 'f'


class Bear(Animal):
    def __repr__(self):
        return 'B' if self.gender else 'b'


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
            # 二熊时
            if len(bears) == 2:
                # 性别不同，在空位产生新的熊
                if bears[0][1].gender != bears[1][1].gender:
                    new = random.choice(empty)
                    change.append((new, Bear()))
                    empty.remove(new)
                # 性别相同，保留较强壮的
                else:
                    bear = bears[0][1] if bears[0][1].strength > bears[1][1].strength else bears[1][1]
                    change.append((bears[0][0], None))
                    change.append((bears[1][0], None))
                    change.append((target, bear))
            # 一熊时，仅移动熊
            elif len(bears) == 1:
                change.append((bears[0][0], None))
                change.append((target, Bear()))
        # 仅同类相遇时
        elif len(set(type(a) for _, a in candi)) == 1:
            gen = set()
            stre = []
            for org, ani in candi:
                gen.add(ani.gender)
                stre.append(ani.strength)
            # 全为同性时，保留最强壮的
            if len(gen) == 1:
                max_idx = stre.index(max(stre))
                for org, _ in candi:
                    change.append((org, None))
                change.append((target, candi[max_idx][1]))
            # 性别不同时
            # 此处代码不完整，只考虑了一雄一雌的情况，实际还应该存在二雄一雌或者一雄二雌的情况
            else:
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
