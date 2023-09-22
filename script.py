import urllib.request
import schedule
import time

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def job():
    url = 'https://webservices.mirea.ru/upload/iblock/603/t0wpe4tzyecbhx1wse7mpuv4ovhdnlr8/IKTST_4_k_osen_23.xlsx'
    filename = 'file.zip'
    download_file(url, filename)

# Расписание выполнения задачи каждый день в 12:00
schedule.every().day.at("23:59").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)