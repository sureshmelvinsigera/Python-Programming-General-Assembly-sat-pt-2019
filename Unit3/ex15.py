class Cake:
    set_oven_temperature_celsius = 180

    def __init__(self, cupcake_type):
        self.type = cupcake_type
        print("I'm going create ", self.type, " cupcake")


chocolate_cupcake = Cake("chocolate")
apple_pie = Cake("applepie")
