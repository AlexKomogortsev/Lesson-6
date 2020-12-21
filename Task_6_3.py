# Task 3

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        d = self._income
        total = int(d.get('wage')) + int(d.get('bonus'))
        return total




income1 = {
    'wage': 30000,
    'bonus': 5000
}

salary_of_worker = Position(name='Александр', surname='Комогорцев', _income=income1, position='Редактор')
print(f'{salary_of_worker.get_full_name()} имеет ЗП в размере {salary_of_worker.get_total_income()} руб')

