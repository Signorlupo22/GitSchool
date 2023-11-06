import requests
import bs4 as bs
import os.path
import threading

from validate_email import validate_email


cookies = {
    'cookie_consent': '7',
    'webrole': 'gen',
    'webidentity': 'G7393021W',
    'LAST_REQUESTED_TARGET': 'cvv',
    'PHPSESSID': 'qfdqu2b7tggpdgvifsa6dph0adu1cuno',
}

headers = {
    'authority': 'web.spaggiari.eu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,it;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'cookie_consent=7; webrole=gen; webidentity=G7393021W; LAST_REQUESTED_TARGET=cvv; PHPSESSID=qfdqu2b7tggpdgvifsa6dph0adu1cuno',
    'dnt': '1',
    'referer': 'https://web.spaggiari.eu/acc/app/default/me.php?v=people',
    'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


domain = 'iiseinaudiscarpa.edu.it' 
filename = "/Users/thomasfavero/Desktop/nomi.txt"
# ... (your headers and cookies here)

def setMail(mail):
    name = ""
    for elemento in mail:
        name += elemento + " "
    try:
        # controlla se l'email esiste già nel file
        if os.path.isfile(filename):
            with open(filename, "a") as f_check:
                f_check.write(name+ "\n")
    except Exception as e:
        print("Errore durante la scrittura del file:", e)


def process_id(id):
    for i in range(25000):
        print(i)
        response = requests.get(
            'https://web.spaggiari.eu/acc/app/default/me.php?v=people_detail&account_id=S' + str(id + i) + '&fs=:fullscreen:',
            cookies=cookies,
            headers=headers,
        )

        soup = bs.BeautifulSoup(response.text, 'html.parser')
        name = soup.find('div', class_='open_sans_extrabold font_size_20 graytext').text.split(' ')
        if len(name) != 0 and name[0] != "":
            print(soup.find('div', class_='open_sans_extrabold font_size_20 graytext').text)
            setMail(name)

start_id = 1
num_threads = 400  # You can adjust the number of threads as needed

# Create and start threads to process IDs in parallel
threads = []
for i in range(num_threads):
    thread_id = start_id + i * 45000
    thread = threading.Thread(target=process_id, args=(thread_id,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
