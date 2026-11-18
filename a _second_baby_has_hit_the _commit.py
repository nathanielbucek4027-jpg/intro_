
from datetime import date


class Baby:

    def __init__(self, baby_name, babys_birthdate=None,
                 baby_height=20, baby_weight=130):

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

    def scream(self):
        self.mood = "mad"
        print(self.name, "is screaming!")

    def burp(self):
        self.mood = "happy"
        print(self.name, "burped and is happy!")

    def poop(self):
        self.weight -= 5
        self.mood = "content"
        print(self.name, "pooped and lost 5 ounces.")

    def pee(self):
        self.weight -= 4
        self.mood = "content"
        print(self.name, "peed and lost 4 ounces.")

    def eat(self, food="vegetables"):
        self.weight += 11
        self.eat_counter += 1
        self.feeding_counter += 1

        print(self.name, "ate", food)

        food = food.lower()

        if food == "fruit" or food == "goodies":
            self.laugh()

        elif food == "vegetables":
            self.cry()

        elif food == "cereal":
            self.sleep()

        else:
            self.mood = "content"

        # Every third eat causes poop
        if self.eat_counter % 3 == 0:
            self.poop()

        # Every third total feeding causes burp
        if self.feeding_counter % 3 == 0:
            self.burp()

    def drink(self):
        self.weight += 8
        self.drink_counter += 1
        self.feeding_counter += 1
        self.mood = "content"

        print(self.name, "had a drink.")

        # Every third drink causes pee
        if self.drink_counter % 3 == 0:
            self.pee()

        # Every third total feeding causes burp
        if self.feeding_counter % 3 == 0:
            self.burp()

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


# Create two Baby objects
starting_baby = Baby("Johnson")
second_baby = Baby("Alicia", baby_weight=140)


# PART 1 TESTS

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
starting_baby.laugh()

print("Johnson's mood:", starting_baby.mood)
print("Alicia's mood:", second_baby.mood)


print("\n--- TEST 5: FINAL STATUS ---")
starting_baby.display_status()
second_baby.display_status()


# PART 2 CANONICAL TESTS

print("\n--- TEST A: THREE EATS ---")

baby_a = Baby("Test Baby A")

baby_a.eat()
baby_a.eat()
baby_a.eat()

baby_a.display_status()


print("\n--- TEST B: THREE DRINKS ---")

baby_b = Baby("Test Baby B")

baby_b.drink()
baby_b.drink()
baby_b.drink()

baby_b.display_status()


print("\n--- TEST C: MIXED FEEDINGS ---")

baby_c = Baby("Test Baby C")

baby_c.eat("fruit")
baby_c.drink()
baby_c.eat("cereal")

baby_c.display_status()
