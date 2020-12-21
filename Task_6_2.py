# Task 2

class Road:
    def __init__(self, _length, _width):
        self._length = int(_length)
        self._width = int(_width)

    def mass(self):
        mass_for_m = 25
        thickness = 10
        whole_mass = self._length * self._width * mass_for_m * thickness
        return whole_mass

lenght = input('Введите длину дороги в метрах: ')
width = input('Введите ширину дороги в метрах: ')
asphalt = Road(lenght, width)
print(f'Ваша дорога весит {asphalt.mass() / 1000} тонн')
