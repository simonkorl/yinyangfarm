import logging
import random
logging.basicConfig(level=logging.INFO)
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

def has_enough_resources(resources: dict, recipe: dict) -> bool:
    for key in recipe:
        if key not in resources:
            return False
        elif resources[key] < recipe[key]:
            return False
    return True

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
                0: {0: 1}, # level: resources
                1: {0: 3},
                2: {0: 5},
                3: {0: 8}, # max
            } # facility
        }
        self.items = {"0": None} # a collection of all possible items

    def build(self, key):
        '''
        a base building function
        can build and upgrade facilities
        '''
        logging.info("try to build")
        if key in self.production:
            level = self.production[key]
            if level >= len(self.blue_script[key]) - 1:
                logging.info(f"maximum level: {key}({level})")
                return
            if has_enough_resources(self.resources, self.blue_script[key][self.production[key]]):
                logging.info(f"upgrade facility: {key} ({self.production[key]} -> {self.production[key] + 1})")
                self.production[key] = self.production[key] + 1
            else:
                logging.warning("don't have enough resources")
        elif key in self.blue_script:
            # try to build the facility
            if has_enough_resources(self.resources, self.blue_script[key][0]):
                logging.info("build facility: %s (nil -> 0)" % (key))
                self.production[key] = 0
        else:
            logging.warning("don't have the facility or the blue script: {key}")
        # for key in self.production.keys():
        #     if has_enough_resource():
        #         consume()
        #         upgrade()

    def heal(self):
        logging.info("try to heal operators")
    
    def produce(self):
        logging.info("produce resources")
        old_res = self.resources.copy()
        for key in self.production.keys():
            if self.resources.get(key) is not None:
                self.resources[key] = self.production_table[key][self.production[key]](self.resources[key])
        logging.info(f"{old_res} => {self.resources}")

def change_phase(farm, yinyang):
    if yinyang.is_yang():
        # go to the night
        farm.heal()
        farm.produce()
    elif yinyang.is_yin():
        # go to the day
        farm.build(0)
    yinyang.swap()
    print("time change from %s to %s" % ("Day" if yinyang.is_yang() else "Night", "Night" if yinyang.is_yang() else "Day"))
    return yinyang.is_yang()

if __name__ == "__main__":
    yinyang = YinYang()
    yinyang.set(1)
    farm = Farm()
    days = 1
    while True:
        # begin phase
        yinyang_symbol = "+" if yinyang.is_yang() else "-"
        print("=== Day (%d)%s Current time is: %s%s ===" % (days, yinyang_symbol, "Light" if yinyang.is_yang() else "Night", yinyang_symbol))
        command = input("input command (1: change phase, 2: check resources): ")
        match command:
            case "1":
                change_phase(farm, yinyang)
                if yinyang.is_yang():
                    days += 1
            case "2":
                print(farm.resources)
            case _:
                print("invalid command")
        
