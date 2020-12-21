# Task 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Нечем будет стирать!!!')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Не вижу, что пишешь!!!')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('ВАУ ! Как ярко !!!')

risovat = Stationery('Ручка')
ruchka = Pen('DIC')
karandash = Pencil('Faber-Castell')
marker = Handle('HL Crewer')

risovat.draw()
ruchka.draw()
karandash.draw()
marker.draw()