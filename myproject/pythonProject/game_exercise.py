class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"{self.num_arrows} arrows remaining")

    def run(self):
        print("run really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hybrid_borg1 = HybridBorg("deadshot", 200, 100)
wizard1 = Wizard("Gandalf", 500)
archer1 = Archer("Legolas", 50)
print(hybrid_borg1.name, hybrid_borg1.attack(), hybrid_borg1.run(), hybrid_borg1.check_arrows(), hybrid_borg1.sign_in())
print(wizard1.sign_in(), wizard1.name, wizard1.attack())
print(archer1.sign_in(), archer1.name, archer1.check_arrows())
