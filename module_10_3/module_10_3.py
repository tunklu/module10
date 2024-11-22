import threading

class Bank:
    balance  = int
    lock = threading.Lock()
    def __init__(self):
        pass
    def deposit(self):
        pass
    def take(self):
        pass

bk = Bank()

th1 = (threading.Thread(target=Bank.deposit, args=(bk,)))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
