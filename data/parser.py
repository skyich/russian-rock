import multiprocessing
import requests
import re
from bs4 import BeautifulSoup

def get_html(url):
	r=requests.get(url)
	r.encoding = 'windows-1251'
	return r.text

def get_all_pages(html):
	soup = BeautifulSoup(html,'html5lib')
	
	pages = soup.find('div','pagenav').find_all('a')[-1].get('href')
	total_pages = int(pages.split('=')[1])//5
	return total_pages

def get_page_data(html):
	soup = BeautifulSoup(html,'html5lib')

	songs = soup.find_all('td','main-body')
	with open('output.txt','a') as f:
		for song in songs:
			tmp = str(song)
			tmp = tmp[tmp.find('</a>')+4:]
			tmp = tmp.split('<br/>')
			for i in tmp:
				i=i.strip()
				if not (i=="" or (re.search('[a-zA-Zїі1-9]',i))):
					f.write(i + '\n')
			f.write('\n')
		
		
def make(url): 
    html = get_html(url)
    print(str(url))
    data = get_page_data(html)


def main():
    # http://rockk.ru/index.php?rowstart=0
    url = 'http://rockk.ru'
    base_url = 'http://rockk.ru/index.php?rowstart='

    links=[] #Это массив адресов(страниц от 1 - до конца)
    for i in range(1,get_all_pages(get_html(url))+1): 
        links.append(base_url + str(i * 5)) # Заполняем массив адрессами

    with multiprocessing.Pool(40) as p: # Тут создается 20 процессов(в видюхе тип 40 запускал тут как хочешь, можешь столько же поставить)
        p.map(make,links)   # Pool применяет make к массиву links разделяя на процессы (Функция make над main описана)


if __name__ == '__main__':
    main()
	
	
	