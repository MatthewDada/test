class car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

car1 = car("blue", 20000)
car2 = car("red", 30000)

print(f"The first car is {car1.colour} and it runs {car1.mileage} miles")
print(f"The second car is {car2.colour} and it runs {car2.mileage} miles")

class citizen:
    def __init__(self, name, age, state_of_origin, BVN, phone_no):
        self.name = name
        self.age = age
        self.state_of_origin = state_of_origin
        self.BVN = BVN
        self.phone_no = phone_no

citizen1 = citizen("Hardy", 22, "Ogun", 2896239102, 907975159)
citizen2 = citizen("Chizom", 30, "Imo", 4984720108, 813427193)

print(f"{citizen1.name} is a student at Code hub and he is {citizen1.age} years old and he comes from "
f"{citizen1.state_of_origin} state. His BVN number is {citizen1.BVN} and his phone number is +234{citizen1.phone_no}")

print(f"{citizen2.name} is the tutor at Code hub and he is {citizen2.age} years old and he comes from "
f"{citizen1.state_of_origin} state. His BVN number is {citizen1.BVN} and his phone number is +234{citizen1.phone_no}")