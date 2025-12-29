import asyncio
import aiohttp
import time

async def download_file(name, url):
    print(f"{name} started downloading...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            size = len(data)
            print(f"{name} finished downloading, size: {size} bytes")

async def main():
    start_time = time.time()

    urls = [
        "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_500_kB.pdf",
        "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_1MB.pdf"
    ]

    tasks = [download_file(f"Task {i+1}", url) for i, url in enumerate(urls)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print("Total time for asynchronous download:", end_time - start_time, 2, "seconds")

asyncio.run(main())
