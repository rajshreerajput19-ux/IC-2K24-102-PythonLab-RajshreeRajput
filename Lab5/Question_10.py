# Question 10: Multiple Inheritance and MRO

class Superhero:
    def __init__(self, name, movie=False, superpowers=None):
        self.name = name
        self.movie = movie
        self.superpowers = superpowers

    def say(self, message):
        print("Superhero says:", message)


class Bat:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly

    def say(self, message):
        print("Bat says:", message)


class Batman(Superhero, Bat):

    def __init__(self):
        Superhero.__init__(
            self,
            "anonymous",
            movie=True,
            superpowers=["Wealthy"]
        )

        Bat.__init__(self, can_fly=False)

        self.name = "Sad Affleck"


# Create Batman object
sup = Batman()

# Display MRO
print(Batman.__mro__)

# Call say() method
sup.say("I agree")

# Display object details
print(sup.name)
print(sup.can_fly)
input("Press Enter to close the program...")