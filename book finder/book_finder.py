from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#this program will get the book links from http://gen.lib.rus.ec 

# input_data = str(input('>>>'))
input_data = 'python'



ip = 'http://93.174.95.29'# default ip

def open(url):
    #thisl function will open the link , read the file and return the file as object
    opened = False
    while not opened:
        try:
            page = urlopen(url)
            opened = True
            return page
        except:
            opened = False
    
    html = page.read()
    page.close()
    
    return html


def grab_data(input_data):
    url = f'http://gen.lib.rus.ec/search.php?req={input_data}&open=0&res=100&view=simple&phrase=1&column=def'
    html = open(url)

    pg_soup = bs(html, 'html.parser')
    table = pg_soup.findAll('tr',{'valign':'top'})
    table = table[1:2] #grab all table containes book
    books = []#final book details in dictionary
    books_data = []#with html tags
    books_raw_data = []#book details in list

    for row in table:
        li=[]
        for column in row:
            if not column == '\n':
                li.append(column)

        books_data.append(li[0:10])


    for book_data in books_data:

        pg_link = book_data[9].a['href']
        html = open(pg_link)
        pg_soup = bs(html, 'html.parser')
        link_data = pg_soup.findAll('td',{'id':'info'})
        link = link_data[0].h2.a['href']

        id = book_data[0].text
        auther = book_data[1].text
        title = book_data[2].text
        publisher = book_data[3].text
        year = book_data[4].text
        pages = book_data[5].text
        language = book_data[6].text
        size = book_data[7].text
        extension = book_data[8].text
        link = ip+link

        li = [id,auther,title,publisher,year, pages, language,size, extension, link]

        dic = {
            'ID' : id,
            'Auther' : auther,
            'Book Title' : title,
            'Publisher' : publisher,
            'Year' : year,
            'Pages' : pages,
            'Language' : language,
            'Size' : size,
            'Extension' : extension,
            'Link' : link
        }
        books.append(dic)
        books_raw_data.append(li)

    # print(books)
    # print('')
    # print(books_raw_data)

    return books

# grab = grab_data(input_data)

# print(grab)