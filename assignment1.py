class Car:

    def __init__(self, make, model, year, color, top_speed):
       
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.top_speed = top_speed
        self.current_speed = 0

    def accelerate(self, speed_increase):
        """Increases the current speed of the car."""
        self.current_speed += speed_increase
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
            print(f"Reached maximum speed: {self.top_speed} km/h")

    def brake(self, speed_decrease):
        """Decreases the current speed of the car."""
        self.current_speed -= speed_decrease
        if self.current_speed < 0:
            self.current_speed = 0

    def display_info(self):
        """Displays the car's information."""
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Top Speed: {self.top_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")

