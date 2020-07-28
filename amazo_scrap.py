# you must install html5lib,requests,bs4 libraries to run this code

import requests
from bs4 import BeautifulSoup
#program will only run if you paste the link of page 2 of (see all reviews from India) section in url variable below only for amazon

page_list=[1,2,3,4,5,6,7,8,9,10] #list to change pages. add more numbers to the list to increase pages from which data is needed to be extracted


ratings=[] #to add ratings of users to a list
comments=[] #to add comments of a user to a list
for pages in page_list: #to change pages for taking out comments and ratings for different pages
    # to change page no with url .below is url variable mentioned above
    url='https://www.amazon.in/JBL-500BT-Powerful-Wireless-Headphones/product-reviews/B07HGG85HL/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(pages)
    # below r is used as a variable to request website
    r=requests.get(url)
    #below html_content is used to request a website for its html code
    html_content=r.content
    #below code is used to arrange html content in a good order
    soup=BeautifulSoup(html_content,'html.parser')
    
        
        
            
        
    #below loop is used to get all the comment content using html span tag and css class
    for comment in soup.find_all('span',attrs={'class':['a-size-base review-text review-text-content']}):
        #print(comment.get_text().strip())
        #below code is used to add comments to comments list
        comments.append(comment.get_text().strip())

#print(soup) #code for testing

#print(comments) #code for testing

#print(ratings) #code for testing
