import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

to_process = []

with open("errors.txt", "r") as infile:
    to_process = [int(l.strip()) for l in infile.read().splitlines()]

for i in tqdm(to_process): # latest document as of Feb 2 2018
    # try:
        tqdm.write("Processing document #" + str(i))
        document = requests.get("http://www.presidency.ucsb.edu/ws/print.php?pid=" + str(i)).text
        soup = BeautifulSoup(document, 'html.parser')

        title = soup.title.contents[0].replace("\xa0", " ").replace("/", ":")
        if len(title) > 200:
            title = title[:97] + "..." + title[-100:]
        content = soup.find('span', {'class': 'style9'}).text

        with open(title + "." + str(i) + ".txt", "w") as outfile:
            outfile.write(content)
    # except Exception as e:
    #     print(e)
    #     with open("errors2.txt", "a") as outfile:
    #         outfile.write(str(i) + "\n")
    #     continue
