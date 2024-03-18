from multiprocessing import Process
from time import time


def factorize(number):
    start_time = time()
    list_number = []
    divisor = 1  
    
    while divisor <= number:
        if number % divisor == 0:
            list_number.append(divisor)
        divisor += 1
    
    end_time = time()
    result_time = end_time - start_time
    print(f'Час виконання - {result_time}')
    
    return list_number


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    processes = []
    
    for num in numbers:
        pr = Process(target=factorize, args=(num,))
        pr.start()
        processes.append(pr)
        
    for pr in processes:
        pr.join()
    
    for pr in processes:
        print(pr)

#  -------------------------- Test
    a = factorize(128)
    b = factorize(255)
    c = factorize(99999)
    d = factorize(10651060)

    print(a)
    print(b)
    print(c)
    print(d)

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

