# 1. Create a python class called circle with constructor which will take an list as argument for the task.
# The list is [10,501,22,37,100,999,87,351]

class Circle:
    def __init__(self, data_list):
        self.data_list = data_list

circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])
print(circle_instance.data_list)


# 2. Create a proper member variables inside the task if when and use them when necessary.For example for this task create class private variable named pi=3.141

class Circle:
    __pi = 3.141

    def __init__(self, data_list):
        self.data_list = data_list

    def calculate_area(self, radius):
        return Circle.__pi * radius ** 2

# Example usage:
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

for radius in circle_instance.data_list:
    area = circle_instance.calculate_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")


# 3. From the given list create two class methods area and perimeter which will be going to calculate area and radius.
class Circle:
    __pi = 3.141

    def __init__(self, data_list):
        self.data_list = data_list

    @classmethod
    def calculate_area(cls, radius):
        return cls.__pi * radius ** 2

    @classmethod
    def calculate_perimeter(cls, perimeter):
        return perimeter-2 * cls.__pi

# Example usage:
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

for radius in circle_instance.data_list:
    area = Circle.calculate_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")

for perimeter in circle_instance.data_list:
    radius = Circle.calculate_perimeter(perimeter)
    print(f"The radius of a circle is {radius:.2f}")

# 4. Convert the UML diagram to python class and its methods by visiting the given link.
class Tv:
    def __init__(self, brand, inches, price):
        self.brand = brand
        self.inches = inches
        self.price = price
        self.channel = 1
        self.volume = 50

    def increase_volume(self):
        self.volume = min(self.volume + 1, 100)

    def decrease_volume(self):
        self.volume = max(self.volume - 1, 0)

    def set_channel(self, chnl):
        if 1 <= chnl <= 50:
            self.channel = chnl

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} {self.inches}\" TV - Channel {self.channel}, Volume {self.volume}, Price ${self.price}"


class Led(Tv):
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, inches, price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"{super().status()}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Backlight: Yes"


class Plasma(Tv):
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, inches, price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"{super().status()}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Backlight: No"


# Create instances of TVs
bass_class = Tv("Panasonic", 32, 35000)
led_tv = Led("Panasonic", 42, 35000, "1.2 inches", "64 watts on average", "1 lakh hour", "120 Hz")
plasma_tv = Plasma("Panasonic", 42, 55000, "1 inches", "195 watts on average", "20,000 to 60,000 hours", "upto 600 Hz")

# Print TV details
print(bass_class.status())
print(led_tv.display_details())
print(plasma_tv.display_details())
