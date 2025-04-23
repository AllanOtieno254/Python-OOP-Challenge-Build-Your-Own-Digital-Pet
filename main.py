# main.py

from pet import Pet

def main():
    print("🐾 Welcome to the Digital Pet Simulator!")
    name = input("👋 What is your pet's name? ")
    pet_type = input("🐕 What type of pet is it? (e.g., dog, cat, dragon): ")
    pet = Pet(name, pet_type)

    while True:
        print("\n✨ What would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Teach a new trick")
        print("5. Show learned tricks")
        print("6. Check pet status")
        print("7. Exit the game")

        choice = input("👉 Enter your choice (1–7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("🎯 What trick would you like to teach? ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"👋 Goodbye! {pet.name} will miss you! 🐾")
            break
        else:
            print("❗ Invalid input. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()