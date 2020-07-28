# you must install html5lib,requests,bs4 libraries to run this code

import requests
from bs4 import BeautifulSoup
#program will only run if you paste the link of page 2 of (all reviews) section in url variable below only for flipkart

page_list=[1,2,3,4,5,6,7,8,9,10] #list to change pages. add more numbers to the list to increase pages from which data is needed to be extracted

ratings=[] #to add ratings of users to a list
comments=[] #to add comments of a user to a list
for pages in page_list: #to change pages for taking out comments and ratings for different pages
    # to change page no with url .below is url variable mentioned above
    url='https://www.flipkart.com/mivi-zero-portable-bluetooth-speaker/product-reviews/itm91dbdd04d0eb6?pid=ACCFNHGXQYSJGFKB&lid=LSTACCFNHGXQYSJGFKBJZZEQI&marketplace=FLIPKART&page=' + str(pages)
    # below r is used as a variable to request website
    r=requests.get(url)
    #below html_content is used to request a website for its html code
    html_content=r.content
    #below code is used to arrange html content in a good order
    soup=BeautifulSoup(html_content,'html.parser')
    #below loop is used to get all the content about ratings using html div tag and css class
    for rate in soup.find_all('div',{'class' :['hGSR34 E_uFuv','hGSR34 _1nLEql E_uFuv']}):
        #print(rate.get_text().strip())
        #used to add ratings to a list
        ratings.append(rate.get_text())
        
        #below loop is used to get all the comment content using html div tag and css class
    for comment in soup.find_all('div',class_='qwjRop'):
        #below code is used to clear the read more span html tag so that unnecessary read more text is not added in list
        comment.span.clear()
        #print(comment.get_text().strip())
        #below code is used to add comments to comments list
        comments.append(comment.get_text().strip())


#print(soup) #can be used to print all html in arranged manner
#print(ratings) #can be used to print all ratings
#print(comments) #can be used to print all comments


