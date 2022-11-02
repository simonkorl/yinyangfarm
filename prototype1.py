import random
class YinYang:
    '''
    basic class for yin yang state
    '''
    def __init__(self):
        self.state = 0 # 0 for yin and 1 for yang
    def set(self, s):
        if s == "yang":
            self.state = 1
        elif s == "yin":
            self.state = 0
        else:
            self.state = 1 if s else 0
    def swap(self):
        self.state = 1 - self.state
    def is_yin(self):
        return self.state == 0
    def is_yang(self):
        return self.state == 1

class Character:
    '''
    basic class of character
    '''
    def __init__(self, atk=1, dfs=1, hp=10):
        self.atk = atk
        self.dfs = dfs
        self.hp = hp
        self.skills = {}

class Operator(Character):
    '''
    Character which player can use
    '''
    def __init__(self):
        self.base_atk = 1
        self.base_dfs = 1
        self.base_hp = 10

        self.level = 1
        self.equips = {}
        self.skills = {}
        Character.__init__(self.base_atk, self.base_dfs, self.base_hp)

class Farm:
    '''
    '''
    def __init__(self):
        self.repo = {} # repository of characters
        self.resources = {0: 0} # a collection of all the possible resources stored in the farm
        self.production = {0: 0} # a collection of levels of production facilities
        self.production_table = {
            0: {
                0: lambda x: x + 1,
                1: lambda x: x + 2,
                2: lambda x: x + 3,
                3: lambda x: x + 4
            }
        }
        self.blue_script = {
            0: {
                0: 1,
                1: 3,
                2: 5,
                3: 8,
            }
        }
        self.items = {"0": None} # a collection of all possible items

    def build(self):
        print("try to build")
        # for key in self.production.keys():
        #     if has_enough_resource():
        #         consume()
        #         upgrade()

    def heal(self):
        print("try to heal operators")
        pass
    
    def produce(self):
        print("produce resources")
        for key in self.production.keys():
            if self.resources.get(key) is not None:
                self.production_table[key][self.production[key]](self.resources[key])

def time_pass(farm, yinyang):
    print("Current time is: ", "Day" if yinyang.is_yang() else "Night")
    if yinyang.is_yang():
        # go to the night
        farm.heal()
        farm.produce()
    elif yinyang.is_yin():
        # go to the day
        farm.build()
    yinyang.swap()
    print("time change to %s from %s" % ("Day" if yinyang.is_yang() else "Night", "Night" if yinyang.is_yang() else "Day"))

if __name__ == "__main__":
    yinyang = YinYang()
    yinyang.set(1)
    farm = Farm()

    for i in range(3):
        time_pass(farm, yinyang)
