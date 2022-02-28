#Class / Klasse ist ein Bauplan
class Car:
    def __init__(self):         #<- Methode != Funktion / init Methode
        self.car_brand = None       #Methodenkörper
        self.horse_power = None     #self Parameter gibt den Wert des ausgrführten Objekts zurück
        self.color = None
        self.x_position = 5
        self.y_position = 5

    def drive(self, x, y): # ":" schließt den Methodenköper ab
        self.x_position += x
        self.y_position += y

car_variable = Car()                #1 Klassenobjekt

print(car_variable.x_position)
print(car_variable.y_position)

car_variable.drive(5,10)

print(car_variable.x_position)
print(car_variable.y_position)