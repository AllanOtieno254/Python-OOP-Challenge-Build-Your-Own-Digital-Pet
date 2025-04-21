from pet import Pet

#Name of the pet
my_pet = Pet("Simba")

#Get Pet's status
my_pet.get_status()

#Give the pet food and put it to sleep
my_pet.eat()
my_pet.sleep()

#Play with the pet
my_pet.play()

#Train the pet
my_pet.train("roll over")
my_pet.train("jump")
my_pet.train("sit")

#Get status of pet after food, sleep and play
my_pet.get_status()

#Show the trick the pet has learned
my_pet.show_tricks()
