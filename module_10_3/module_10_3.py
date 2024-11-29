import threading, time, random

class Bank:
    balance  = int
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                amount = random.randint(50, 500)
                self.balance += amount
                print(f'пополнение №: {i}')
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                time.sleep(0.001)

    def take(self):
        for i in range(1, 101):
            amount = random.randint(50, 500)
            with self.lock:
                print(f"Запрос на {amount}")
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'снятие №: {i}')
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()

bk = Bank()

th1 = (threading.Thread(target=Bank.deposit, args=(bk,)))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
