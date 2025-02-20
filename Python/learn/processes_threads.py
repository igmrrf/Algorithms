import threading
import time
import random
import multiprocessing
from typing import List


def square(n):
    return n * n


def serve(orders: List[str], lock):
    time.sleep(2)

    lock.acquire()
    if len(orders):
        orders.pop()
    lock.release()
    print("no orders left")
    return


def order(meals, orders, lock):
    time.sleep(0.5)
    lock.acquire()
    orders.insert(0, random.choice(meals))
    lock.release()
    return


if __name__ == "__main__":

    meals = ["pizza", "samosa", "pasta", "biryani", "burger"]
    orders = []

    t1 = threading.Thread(target=serve, args=(orders,))
    t2 = threading.Thread(target=order, args=(orders,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    arr = [2, 4, 6, 7]
    multi_pool = multiprocessing.Pool(processes=3)

    orders = multiprocessing.Array("i", 4)
    currentOrder = multiprocessing.Value("s", "")
    orderOfOrders = multiprocessing.Queue()

    # orderOfOrders.put

    lock = multiprocessing.Lock()
    # orders = multiprocessing.Value("d", 0.0)
    resp = multi_pool.map(square, arr)
    multi_pool.close()
    multi_pool.join()
    p1 = multiprocessing.Process(target=serve, args=(orders, lock))

    p2 = multiprocessing.Process(target=order, args=(meals, orders, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done")
    print(orders[:])
    print(currentOrder.value)
    while orderOfOrders.empty() is False:
        print(orderOfOrders.get())

## Multi threading and Multi Processing
