from threading import Thread, Lock
from time import sleep

class Knight(Thread):
    enemies_count = 100
    lock = Lock()
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_fought = 0

    def run(self):
        enemies_left = Knight.enemies_count
        with Knight.lock:
            print(f"{self.name}, на нас напали!")

        while enemies_left > 0:
            enemies_left -= self.power
            self.days_fought += 1
            if enemies_left < 0:
                enemies_left = 0

            with Knight.lock:
                print(f"{self.name}, сражается {self.days_fought} день(дня)..., осталось {enemies_left} воинов.")
            sleep(1)

        with Knight.lock:
            print(f"{self.name} одержал победу спустя {self.days_fought} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()