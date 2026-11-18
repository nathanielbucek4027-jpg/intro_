
from datetime import date
from unicodedata import name


class Baby:

    def __init__(self, baby_name, babys_birthdate = None, baby_height = 20, baby_weight = 130):

        if babys_birthdate is None:
            babys_birthdate = date.today().isoformat()

        self.name = baby_name
        self.birthdate = babys_birthdate
        self.height = baby_height
        self.starting_weight = baby_weight
        self.weight = baby_weight
        self.mood = "content"
        self.eat_counter = 0
        self.drink_counter = 0
        self.feeding_counter = 0

    def laugh(self):
        self.mood = "happy"
        print(self.name, "is laughing!")

    def cry(self):
        self.mood = "sad"
        print(self.name, "is crying!")

    def sleep(self):
        self.mood = "content"
        print(self.name, "is sleeping peacefully.")

    def display_status(self):
        print("\n--- BABY STATUS ---")
        print()
        print("Name:", self.name)
        print("Birthdate:", self.birthdate)
        print("Height:", self.height, "inches")
        print("Starting weight:", self.starting_weight, "ounces")
        print("Current weight:", self.weight, "ounces")
        print("Weight in pounds:", round(self.weight / 16, 2))
        print("Mood:", self.mood)
        print("Eat count:", self.eat_counter)
        print("Drink count:", self.drink_counter)
        print("Feeding count:", self.feeding_counter)
        print()



starting_baby = Baby("Johnson")
second_baby = Baby("Alicia", weight=140)


print("--- TEST 1: DEFAULT VALUES ---")
starting_baby.display_status()


print("--- TEST 2: CUSTOM WEIGHT ---")
second_baby.display_status()


print("--- TEST 3: MOOD CHANGES ---")

starting_baby.laugh()
print("Mood after laughing:", starting_baby.mood)

starting_baby.cry()
print("Mood after crying:", starting_baby.mood)

second_baby.sleep()
print("Mood after sleeping:", second_baby.mood)


print("\n--- TEST 4: SEPARATE BABY OBJECTS ---")
print()
starting_baby.laugh()

print("Johnson's mood:", starting_baby.mood)
print("Alicia's mood:", second_baby.mood)



print("\n--- TEST 5: FINAL STATUS ---")
print()

starting_baby.display_status()
second_baby.display_status()
