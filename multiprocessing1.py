import multiprocessing
import time


def calc_square(numbers):
    print("square of numbers")
    for n in numbers:
        time.sleep(5)
        print('square:', n * n)


def calc_cube(numbers):
    print("cube of numbers")
    for n in numbers:
        time.sleep(5)
        print('cube:', n * n * n)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

# t = time.time()

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done!")
