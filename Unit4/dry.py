class Vehicle:
    model = 2019

    def __init__(self, c):
        print('creating the Vehicle ')
        self.price = c


    def start(self):
        print('Starting the Vehicle')

    def stop(self):
        print('Stopping the Vehicle')

    def apply_breaks(self):
        print('Applying the breaks')


mycar = Vehicle(2000)
mycar.start()
print(mycar.model)

youcar = Vehicle(50000)
youcar.apply_breaks()
print(youcar.model)
