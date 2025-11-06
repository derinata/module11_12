class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled = 0

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.traveled += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, reg, max_speed, battery_kwh):
        super().__init__(reg, max_speed)
        self.battery_kwh = battery_kwh

class GasolineCar(Car):
    def __init__(self, reg, max_speed, tank_liters):
        super().__init__(reg, max_speed)
        self.tank_liters = tank_liters

if __name__ == "__main__":
    e = ElectricCar("ABC-15", 180, 52.5)
    g = GasolineCar("ACD-123", 165, 32.3)

    # select speeds
    e.accelerate(150)  # set electric car speed to 150 km/h
    g.accelerate(120)  # set gasoline car speed to 120 km/h

    # drive for three hours
    e.drive(3)
    g.drive(3)

    print(f"{e.reg} traveled: {e.traveled} km")
    print(f"{g.reg} traveled: {g.traveled} km")