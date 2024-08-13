# OOP
# class NameOfClass:
#     class_attribute = value # Class Object attribute
#
#     def __init__(self,param1, param2):
#         self.param1 = param1  # attributes
#          self.param2 = param2
#
#     def method(self):
#         # code
#
#     @classmethod
#     def cls_method(cls, param1, param2):
#         # code
#
#     @staticmethod
#     def stc_method(param1, parm2):
#        # code

class PlayerCharacter:
    membership = True  # Class Object attribute

    def __init__(self, name, age):
        if self.membership:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        return f"my name is {self.name}"

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Cindy", 50)
player2 = PlayerCharacter("Tom", 21)
player2.attack = "damage 100"
player1.attack = "damage 88"
player1.hide = "go hide"
player3 = PlayerCharacter.adding_things(2, 3)
print(player1.name, player1.age, player1.attack, player1.shout(), player1.hide)
print(player2.name, player2.age, player2.attack, player2.shout())
print(player3.name, player3.age)
