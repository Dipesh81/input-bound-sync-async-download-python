import time
import requests

def download_file(name, url):
    print(f"{name} started downloading...")
    response = requests.get(url)
    size = len(response.content)
    print(f"{name} finished downloading, size: {size} bytes")

start_time = time.time()

urls = [
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_500_kB.pdf",
    "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_1MB.pdf"
]

for i, url in enumerate(urls):
    download_file(f"Task {i+1}", url)

end_time = time.time()
print("Total time for synchronous download:", end_time - start_time, 2, "seconds")
