# scraper.py includes functions that scrape the website dealerrater.com
# to find the most positive reviews for a given dealership


# Import modules
import requests # to request website data
from bs4 import BeautifulSoup # to parse HTML and find content
from dictionary import dictionary


# Import local dictionary of positive and negative words
negdict, posdict, negdictstrip, posdictstrip = dictionary.dictionary()


# 'pages' uses string manipulation to take an input and find the first 5 pages of reviews
def pages(URL, numpages): #takes URL, numpages, returns pagelist of numpages URL's of reviews

    pagelist = []

    for i in range(len(URL)):
        if URL[i] == 'e' and URL[i+1] == '1':
            var = i+1
    for j in range(numpages):
        before = URL[0:(var)]
        after = URL[(var+1):]
        pagenum = str(j+1)
        page = before + pagenum + after
        #print(pagenum)
        pagelist.append(page)

    return pagelist


# 'reviewlist' uses the BeautifulSoup module to webscrape the given dealership's reviews
# to create a list of all reviews
def reviewlist(pagelist):

    reviewlist = []
    for i in range(len(pagelist)):
        
        URL = pagelist[i]
        page = requests.get(URL)
        status = page.status_code #if 200, page is accessible
        contents = page.text
        soup = BeautifulSoup(contents, 'html.parser')
        
        main = soup.find('div', class_='col-xs-12 pad-top-lg mobile-hide')

        #finds specific reviews 2nd review starts at 2...index of reviews
        review = main.find_all('div', recursive=False) 
        

        for j in range(len(review)):
            k = j+1
            if k > 10:  #if k is greater than the number of reviews on page
                break
            else:
                review = main.find_all('div', recursive=False)[k]
                body = review.find_all('p')[0]
                string = body.text
                string2 = string
                reviewlist.append(string2)

    return reviewlist


# 'generalrating' uses the BeautifulSoup module to webscrape the given dealership's reviews
# to create a list of the reviews general ratings out of 5 stars
def generalrating(pagelist):
    
    rating_list = []

    for i in range(len(pagelist)):
        
        URL = pagelist[i]
        page = requests.get(URL)
        status = page.status_code #if 200, page is accessible
        contents = page.text
        soup = BeautifulSoup(contents, 'html.parser')
        
        main = soup.find('div', class_='col-xs-12 pad-top-lg mobile-hide')

        #finds specific reviews 2nd review starts at 2...index of reviews
        review = main.find_all('div', recursive=False) 

        for j in range(len(review)):
            k = j+1
            if k > 10:  #if k is greater than the number of reviews on page
                break
            else:
                review = main.find_all('div', recursive=False)[k]
                rating_1 = review.find_all('div')[4]
                rating_2 = rating_1['class']

                #[2] is the class review rating
                rating_3 = rating_2[2]  #turning the rating class into a string
                score = float(rating_3[7] + '.' + rating_3[8]) # score is review score out of 5
                #index goes from 1-11 : 10 reviews per page

                rating_list.append(score)
            
    return rating_list



# 'specificrating' uses the BeautifulSoup module to webscrape the given dealership's reviews
# to create a list of the reviews breakdown-ratings out of 5 stars and then averages them
def specificratings(pagelist):
    breakdownlist = []
    for i in range(len(pagelist)):
        
        #range(len(pagelist)):
        URL = pagelist[i]
        page = requests.get(URL)
        status = page.status_code #if 200, page is accessible
        contents = page.text
        soup = BeautifulSoup(contents, 'html.parser')
        
        main = soup.find('div', class_='col-xs-12 pad-top-lg mobile-hide')

        #finds specific reviews 2nd review starts at 2...index of reviews
        review = main.find_all('div', recursive=False) 
        for j in range(len(review)):
            k = j+1
            if k > 10:  #if k is greater than the number of reviews on page
                break
            else:
                #finds specific reviews 2nd review starts at 2...index of reviews

                review = main.find_all('div', recursive=False)[k]
                rating_1 = review.find_all('div')[10] #rating breakdown

                breakdownindex = [2, 5, 8, 11, 14] # index of location of specific breakdown scores
                    # 2 'Customer Service
                    # 5 'Quality of work
                    # 8 'Friendliness
                    # 11 is Pricing
                    # 14 is overall excperience

                avglist = []

                for l in breakdownindex: # 5 is the number of specific ratings
                    rating_2 = rating_1.find_all('div')[0] 

                    #finds individual rating sets
                    rating_3 = rating_2.find_all('div')[l]
                    
                    rating_4 = rating_3['class']
                    rating_5 = rating_4[1]
                    score = float(rating_5[7] + '.' + rating_5[8]) # score is review score out of 5

                    avglist.append(score)
                
                average = sum(avglist) / len(avglist)
                breakdownlist.append(average)

    return breakdownlist


# 'positivewords' compares every word in every review to a dictionary of positive-sentiment words to 
# create a list of the number of positve words in each review
def positivewords(reviewlist):
    
    #initialize lists
    sentimentscore, pos_words = ([] for i in range(2))
    
    for j in range(len(reviewlist)):

        #initialize variables
        pos_score = 0
        rsp = []

        ind_review = reviewlist[j]
        splitwords = ind_review.split(' ')  #individual review list

        for i in range(len(splitwords)):
            for k in range(len(posdict)):

                if (splitwords[i] == posdict[k]) or (splitwords[i] == posdictstrip[k]):

                    pos_score +=1
                    rsp.append(splitwords[i])

        if pos_score == 0:
            rsp.append(0)

        pos_words.append(rsp)

        sentimentscore.append(pos_score)

    return pos_words