# Create a class that will have attribute of a car.
# Call methods defined for our car object

class Car:
    color = 'green'
    number_of_doors = 5
    speed = 0

    def paint_car(self, new_color):
        self.color = new_color

    def accelerate(self, val_acc, time):
        self.speed += val_acc * time
        if self.speed > 300_000_000:
            raise ValueError('We can`t exceed the speed of light')

    def decelerate(self, val_acc, time):
        self.speed -= val_acc * time
        if self.speed < 0:
            self.speed = 0  # set the speed to 0 when negative
            raise ValueError('Car is stopped, speed can no longer be reduced')

    def read_speed(self):
        km_per_h = (3600 / 1000) * self.speed
        return km_per_h


if __name__ == '__main__':
    car = Car()

    car.paint_car('red')
    print('The new care color is:', car.color)

    car.accelerate(30, 10)  # Accelerate at 30 m/s2 (~3G) for 10 seconds
    print('Current speed is:', car.speed, 'm/s or')
    print('Current speed is:', car.read_speed(), 'km/h')

    car.decelerate(20, 10)
    print('Current speed is:', car.speed, 'm/s or')
    print('Current speed is:', car.read_speed(), 'km/h')

    car.decelerate(11, 10)
