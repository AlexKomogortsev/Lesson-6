# Task 1


class TraffiсLight:
    from time import sleep
    cnt = 0 # переменная cnt добавлена, чтобы светофор не работал бесконечно

    def __init__(self, colour):
        self.__colour = colour


    def running(cls):
        while cls.cnt < 9:
            while cls.__colour == 'КРАСНЫЙ':
                print(f'Горит {cls.__colour} свет, ждите!')
                for i in range(7, 0, -1):
                    print(f'{i}')
                    cls.sleep(0.5)
                cls.__colour = 'ЖЕЛТЫЙ'
                cls.cnt += 1
            while cls.__colour == "ЖЕЛТЫЙ":
                print(f'Горит {cls.__colour} свет, готовьтесь!')
                for i in range(2, 0, -1):
                    print(f'{i}')
                    cls.sleep(0.5)
                cls.__colour = 'ЗЕЛЕНЫЙ'
                cls.cnt += 1
            while cls.__colour == "ЗЕЛЕНЫЙ":
                print(f'Горит {cls.__colour} свет, двигайте!')
                for i in range(5, 0, -1):
                    print(f'{i}')
                    cls.sleep(0.5)
                cls.__colour = 'КРАСНЫЙ'
                cls.cnt += 1
            if cls.__colour != 'КРАСНЫЙ' and cls.__colour != "ЖЕЛТЫЙ" and cls.__colour != "ЗЕЛЕНЫЙ":
                print('СВЕТОФОР ИМЕЕТ ТОЛЬКО ТРИ ЦВЕТА !!!')
                break


tl = TraffiсLight(input('Укажите какой свет горит в данный момент, не используя буквы Ё: ').upper())
tl.running()
