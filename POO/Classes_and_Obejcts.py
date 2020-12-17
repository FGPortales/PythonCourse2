class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weigh = weight

    def introduce_self(self):
        print("My name is {} and my favourite color is {} and my wight is {}".format(
            self.name, self.color, self.weigh))


class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


if __name__ == '__main__':
    r1 = Robot("Tom", "red", 30)
    r2 = Robot("Jerry", "blue", 40)
    p1 = Person("Alice", "aggressive", False)
    p2 = Person("Becky", "talkative", True)
    # p1 owns r2
    p1.robot_owned = r2
    p2.robot_owned = r1
    p1.robot_owned.introduce_self()
