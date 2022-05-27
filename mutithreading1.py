import threading
import time


def calc_square(numbers):
    print("square of numbers")
    for n in numbers:
        time.sleep(0.6)
        print('square:', n * n)


def calc_cube(numbers):
    print("cube of numbers")
    for n in numbers:   
        time.sleep(0.5)
        print('cube:', n * n * n)


arr = [1, 2, 3, 4, 5]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("total time taken :", time.time() - t)
