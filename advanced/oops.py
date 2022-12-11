# classmethod,
# staticmethod,
# decorators

"""
function overloading
function overriding
"""


class pet:
    def sound(self, pet_type, pet_name):
        if pet_type.lower() == "dog":
            return f"Your {pet_name} will bark"
        elif pet_type.lower() == "cat":
            return f"Your {pet_name} will meow"


class pet1:
    def sound(self, pet_type, pet_name):
        if pet_type.lower() == "dog":
            return f"Your {pet_name} will meow"
        elif pet_type.lower() == "cat":
            return f"Your {pet_name} will meow"


class pet_in_different_universe(pet, pet1):
    def pet1_sound(self, pet_type, pet_name):
        return pet1.sound(self, pet_type, pet_name)

    # def sec_func(self, pet_type, pet_name):
    #     return super().sound(pet_type, pet_name)

    # def sound(self, pet_type, pet_name):
    #     return "I am overriding method"
    # def sound(self, pet_type, pet_name):
    #     super_return = super().sound(pet_type, pet_name)
    #     res = {}
    #     res.setdefault("currrent_universe", super_return)
    #     if pet_type.lower() == "dog":
    #         res.setdefault("other_universe", f"Your {pet_name} will meow")
    #     elif pet_type.lower() == "cat":
    #         res.setdefault("other_universe", "Your {pet_name} will bark")
    #     return res
    pass


strange_pet = pet_in_different_universe()
# print(strange_pet.sec_func("dog", "Jimmy"))
print(strange_pet.sound("dog", "Jimmy"))
