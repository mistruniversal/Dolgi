import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main(urls):
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    urls = [
        'https://example.com',
        'https://httpbin.org/get',
        'https://jsonplaceholder.typicode.com/posts'
    ]
    results = asyncio.run(main(urls))
    for i, result in enumerate(results):
        print(f"Response from {urls[i]}: {result[:100]}...")  # Печатаем первые 100 символов










import asyncio

async def compute_square(n):
    await asyncio.sleep(1)  # Задержка в 1 секунду
    return n * n

async def main(numbers):
    tasks = [compute_square(n) for n in numbers]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    results = asyncio.run(main(numbers))
    print("Squares:", results)













import threading
import time

counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:  # Блокируем доступ к счетчику
            counter += 1


if __name__ == "__main__":
    threads = []

    for _ in range(2):  # Создаем 2 потока
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ждем завершения всех потоков

    print("Final counter value:", counter)
