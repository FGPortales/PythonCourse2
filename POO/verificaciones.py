class Main:
    def __init__(self, name):
        self.name = name

    def my_function(self):
        print("Estoy dentro de my_function, {}".format(self.name))


if __name__ == '__main__':
    Main('Freddy').my_function()
