from concurrent.futures import ThreadPoolExecutor
import threading
import time


def factorial(n):
    """Calculate the factorial of a number."""
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def factorial_thread(number):
    """Calculate the factorial with a thread."""
    t = threading.Thread(target=factorial, args=(number,))
    start_time = time.time()
    t.start()
    t.join()
    print(t.name, "Spending time:", time.time() - start_time)


def factorial_thread_pool_executor(executor_class, number):
    """Calculate the factorial with a thread pool."""
    executor = executor_class()
    start_time = time.time()
    future = executor.submit(factorial, number)
    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=future.result(),
        executor=executor_class.__name__,
        spent_time=time.time() - start_time
    ))


if __name__ == '__main__':
    factorial_thread(1_000_000)
    factorial_thread_pool_executor(ThreadPoolExecutor, 1_000_000)

    factorial_thread(100_000_000)
    factorial_thread_pool_executor(ThreadPoolExecutor, 100_000_000)

    factorial_thread(500_000_000)
    factorial_thread_pool_executor(ThreadPoolExecutor, 500_000_000)
