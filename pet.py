class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """
        Reduce hunger by 3 (min 0), increase happiness by 1 (max 10).
        Eating makes the pet happier.
        """
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... {old_hunger} ➡ {self.hunger}, Happiness +1")

    def sleep(self):
        """
        Increase energy by 5 (max 10).
        Sleep only affects energy.
        """
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... Energy: {old_energy} ➡ {self.energy}")

    def play(self):
        """
        Play reduces energy by 2, increases happiness by 2, increases hunger by 1.
        If energy is too low, the pet cannot play.
        """
        if self.energy < 2:
            print(f" {self.name} is too tired to play. Let them sleep first!")
            return
        
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing... Energy -2, Happiness +2, Hunger +1")

    def train(self, trick):
        """
        Teach the pet a new trick and store it if not already learned.
        """
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: '{trick}'!")
        else:
            print(f"{self.name} already knows '{trick}'.")

    def show_tricks(self):
        """
        Display all learned tricks.
        """
        if self.tricks:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """
        Show current status of the pet with emojis and stats.
        """
        print("\n📊 " f"{self.name}'s current status:")
        print(f"Name: {self.name} 🐶")
        print(f"Type: {self.pet_type}")
        print(f"Hunger:     {self.hunger} {'🍽️' * self.hunger}")
        print(f"Energy:     {self.energy} {'⚡' * self.energy}")
        print(f"Happiness:  {self.happiness} {'😊' * self.happiness}")
        print(f"Tricks:     {', '.join(self.tricks) if self.tricks else 'None'}")
        print("💖" * 20)