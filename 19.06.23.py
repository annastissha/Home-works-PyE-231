#Напишите программу с интерфейсом, которая по нажатию кнопки загружает 10 картинок в папку. Проверьте все способы: синхронный, многопоточный, мультипроцессорный, асинхронный.
import tkinter as tk
import requests
import threading
import multiprocessing
import aiohttp
import asyncio


def download_1_image(i):
    url = f"https://picsum.photos/320/240/?image={i}"
    response = requests.get(url)
    image_path = f"temp for hw/image{i}.jpg"
    with open(image_path, "wb") as file:
        file.write(response.content)


####################################

def download_image_sync():
    for i in range(1, 10+1):
        download_1_image(i)

def sync_button():
    download_image_sync()
def window_for_sync():
    window = tk.Tk()
    window.title("Downloading")
    window.geometry("300x150")
    button = tk.Button(window, text="Download Images ", command=sync_button)
    button.pack()
    window.mainloop()
##########################################################

def download_image_thread():
    thread_list = []
    for i in range(1, 10+1):
        thread_list.append(threading.Thread(target=download_1_image, args=(i,), kwargs={}))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    for i in range(1, 10+1):
        download_1_image(i)

def thread_button():
    download_image_thread()
def window_for_thread():
    window = tk.Tk()
    window.title("Downloading")
    window.geometry("300x150")
    button = tk.Button(window, text="Download Images ", command=thread_button)
    button.pack()
    window.mainloop()
##########################################

def download_image_multiprocess():
    process_list = []
    for i in range(1, 10 + 1):
        process_list.append(multiprocessing.Process(target=download_1_image, args=(i,), kwargs={}))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    for i in range(1, 10 + 1):
        download_1_image(i)

def multiprocess_button():
    download_image_multiprocess()

def window_for_multiprocess():
    window = tk.Tk()
    window.title("Downloading")
    window.geometry("300x150")
    button = tk.Button(window, text="Download Images ", command=multiprocess_button)
    button.pack()
    window.mainloop()
#############################################

async def async_download_one_image():
    url = "https://picsum.photos/320/240"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(f"temp for hw/image.jpg", "wb") as opened_file:
                opened_file.write(data)

def async_task():
    async def async_task_inline():
        await asyncio.gather(*[async_download_one_image() for _ in range(1, 10 + 1)])
    asyncio.run(async_task_inline())
def async_button():
    async_task()

def window_for_async():
    window = tk.Tk()
    window.title("Downloading")
    window.geometry("300x150")
    button = tk.Button(window, text="Download Images ", command=async_button)
    button.pack()
    window.mainloop()


if __name__ == '__main__':

    window_for_thread()
