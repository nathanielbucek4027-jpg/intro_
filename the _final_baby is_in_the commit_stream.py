
from datetime import date
import time

ACTION_DELAY_SECONDS = 1


class Baby:

    def __init__(self, babies_name, babies_birthdate=None,
                 baby_height=20, baby_weight=130):

        if babies_birthdate is None or babies_birthdate == "":
            babies_birthdate = date.today().isoformat()

        self.name = babies_name
        self.birthdate = babies_birthdate
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
        time.sleep(ACTION_DELAY_SECONDS)

    def scream(self):
        self.mood = "mad"
        print(self.name, "is screaming!")
        time.sleep(ACTION_DELAY_SECONDS)

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

        food = food.strip().lower()

        print(self.name, "ate", food)

        if food == "fruit" or food == "fruits" or food == "goodies":
            self.laugh()

        elif food == "vegetables" or food == "veggies":
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
        print("Babies Name:", self.name)
        print("Babies Birthdate:", self.birthdate)
        print("Baby Height:", self.height, "inches")
        print("Babies Starting weight:", self.starting_weight, "ounces")
        print("Babies Current weight:", self.weight, "ounces")
        print("Weight in pounds:", round(self.weight / 16, 2))
        print("Baby Mood:", self.mood)
        print("Eat counter:", self.eat_counter)
        print("Drink counter:", self.drink_counter)
        print("Feeding counter:", self.feeding_counter)
        print()


def get_positive_number(prompt, default_value, number_type):
    while True:
        user_input = input(prompt).strip()

        if user_input == "":
            return default_value

        try:
            number = number_type(user_input)

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid number. Please try again.")


def main():
    print("--- BABY SETUP ---")

    babies_name = input("Please enter the baby's name: ").strip()

    while babies_name == "":
        print("The baby must have a name.")
        babies_name = input("Please enter the baby's name: ").strip()

    babies_birthdate = input(
        "Enter the baby's birthdate (blank for today): "
    ).strip()

    baby_height = get_positive_number(
        "Enter the baby's height (blank for 20 inches): ",
        20,
        float
    )

    baby_weight = get_positive_number(
        "Enter starting weight (blank for 130 ounces): ",
        130,
        float
    )

    # Create one Baby object
    baby = Baby(
        babies_name,
        babies_birthdate,
        baby_height,
        baby_weight
    )

    print("\nWelcome,", baby.name)
    baby.display_status()

    while True:

        # Check doubled-weight completion condition
        if baby.weight >= baby.starting_weight * 2:
            print("\nThe baby has doubled its starting weight!")
            print("Congratulations! The program is complete.")
            break

        print("\n--- BABY CARE MENU ---")
        print("eat")
        print("drink")
        print("laugh")
        print("cry")
        print("sleep")
        print("scream")
        print("status")
        print("home")

        action = input("Choose an action: ").strip().lower()

        if action == "eat":
            food = input(
                "What should the baby eat? "
                "(vegetables, fruits, goodies, cereal): "
            ).strip().lower()

            if food == "":
                baby.eat()
            else:
                baby.eat(food)

        elif action == "drink":
            baby.drink()

        elif action == "laugh":
            baby.laugh()

        elif action == "cry":
            baby.cry()

        elif action == "sleep":
            baby.sleep()

        elif action == "scream":
            baby.scream()

        elif action == "status":
            baby.display_status()

        elif action == "home":
            print("\nYou chose to go home.")
            break

        else:
            print("Invalid action. Please choose an option from the menu.")

    print("\n--- FINAL BABY STATUS ---")
    baby.display_status()
    print("Goodbye for now!")


if __name__ == "__main__":
    main()
