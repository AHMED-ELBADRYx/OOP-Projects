# Example of protected and private

class Parent:
    def __init__(self):
        self._protected = "I am protected"
        self.__private = "I am private"

class Child(Parent):
    def access_protected(self):
        return self._protected  # easily accessible

    def access_private(self):
        # return self.__private  # this will cause an error
        return self._Parent__private  # accessed via name mangling

# Test
obj = Child()
print(obj.access_protected())  # ✅ works
print(obj.access_private())    # ✅ works but indirectly

# Attempting direct access
print(obj._protected)          # ✅ possible but not recommended
# print(obj.__private)         # ❌ error
print(obj._Parent__private)    # ✅ possible via name mangling
