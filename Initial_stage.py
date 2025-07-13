# Initial stage of writing data to the class

class Info:
    def __init__(self, first_name, last_name,email, passward, status = "active"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passward = passward
        self.status = status

    def display(self):
        print(f"The first name: {self.first_name}")
        print(f"The last name: {self.last_name}")
        print(f"The email: {self.email}")
        print(f"The passward: {self.passward}")
        print(f"The status: {self.status}")
def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter the email: ")
    passward = input("Enter the passward: ")
    return Info(first_name, last_name,email, passward)

user1 = create_user()

print("\nUser details:")
user1.display()
