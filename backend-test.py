
## INSTALL PACKAGES NEEDED ## 
# uncomment 'os.system' if you desire to have the packages required 
# for this program installed automatically
import os
os.system("pip install bs4")
os.system("pip install requests")



# Import local modules
from scraper import scraper
from reviews import top_three


#### Instructions ####

# 1) URL input: needs to be in this specific format. Change the dealer name and dealer number. Leave the 
# page number as 1. 
# 2) Leave as is or alter the number of pages  ('numpages') of reviews to find.
# 3) After done changing inputers, run the program. 
# 4) For the test suite, open up the directory 'test' and open 'test_backend-test.py'


#### INPUT #####


URL = 'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page1/?filter=ALL_REVIEWS'

numpages = 5  



## RUNNING MODULES ##

# OUTPUT WILL BE THE TOP THREE REVIEWS IN ORDER OF 'SEVERITY' # 

URLs = scraper.pages(URL, numpages)

allreviews = scraper.reviewlist(URLs)

generalratings = scraper.generalrating(URLs)

specificratings = scraper.specificratings(URLs)

numpositivewords = scraper.positivewords(allreviews)

topreviews, topscores = top_three.totalreviewscore(allreviews, generalratings, specificratings, numpositivewords)

revieworder = top_three.printtop3(topreviews, topscores, allreviews)

print('In order of most-positive reviiews: \n \n')
for i in range(len(revieworder)):
    print('Review',(i+1), 'is: \n', revieworder[i], '\n\n\n\n\n\n\n')




