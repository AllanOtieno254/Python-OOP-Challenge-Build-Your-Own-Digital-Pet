class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 0
        self.happiness = 0
        self.tricks = []

    def eat(self):
        # TODO
        # reduces hunger by 3 points (but not below 0)
        self.hunger = max(0, self.hunger - 3)

        # increases happiness by 1 (but not above 1)
        self.hunger = min(10, self.hunger + 1)

    def sleep(self):
        # TODO
        # increases energy by 5 points (but not above 10).
        self.energy = min(10, self.energy + 5)

    def play(self):
        # TODO
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness +2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play. Please give it food and let it sleep")

    def train(self, trick):
        # TODO
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick} !")

    def show_tricks(self):
        # TODO
        # When the pet has tricks
        if self.tricks:
            print(f"{self.name} knows these tricks: {',' .join(self.tricks)}")
        
        # Pet has no tricks
        else:
            print(f"{self.name} hasn't learned any tricks yet. Please train it.")

    def get_status(self):
        # TODO

        #Print the current status of the pet
        print(f"{self.name}'s Status:")
        print(f" Hunger Levels: {self.hunger}/10")
        print(f" Energy Levels: {self.energy}/10")
        print(f" Happiness Levels: {self.happiness}/10")
        print()

