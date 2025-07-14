# Using the staticmethod and classmethod decorators in a class

class Members :
    not_allowed_names = ("satan", "angel", "yhwh")
    users_num = 0
    @staticmethod
    def say_hello() :
        print("Hello in members class")
    @classmethod
    def show_users_count(cls) :
        print(f"We have {cls.users_num} users in our system")
    def __init__(self, f_name, s_name, l_name, gender) :
        self.f_name = f_name
        self.s_name = s_name
        self.l_name = l_name
        self.gender = gender
        Members.users_num += 1

    def full_name(self) :
        if self.f_name in Members.not_allowed_names :
            raise ValueError("Name not allowed")
        else:
            return f"{self.f_name} {self.s_name} {self.l_name}"
    def name_with_title(self) :
        if self.gender == "Male" :
            return f"Hello Mr {self.f_name}"
        elif self.gender == "Female" :
            return f"Hello Miss {self.f_name}"
        else :
            return f"Hello {self.f_name}"
    def get_all_info(self) :
            return f"{self.name_with_title()}, Your full name is: {self.full_name()}"
    def delete_user(self) :
        Members.users_num -= 1
        return f"User {self.f_name} deleted"
        
memb1 = Members("Ahmad", "Abdelnaser", "Elbadry", "Male")
memb2 = Members("Ali", "Omar", "Agwa", "Male")
memb3 = Members("Sarah", "Ahmed", "Medo", "Female")
memb4 = Members("satan", "Yokai", "oni", "mixed") # not allowed name and different gender

Members.say_hello()
print(memb1.full_name())
print(memb1.get_all_info())

print(memb2.full_name())
print(memb2.get_all_info())

print(memb3.full_name())
print(memb3.get_all_info())

print(memb4.delete_user())

Members.show_users_count()
print(f"Members number is: {Members.users_num}")