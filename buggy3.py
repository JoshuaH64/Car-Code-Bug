
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} engine started")

if __name__ == "__main__":
    c = Car("Toyota", "Corolla")
    c.start_engine()
    