## READ ME ##
Noah Alex
Backend-Test
Version 1.0.0
No License

## INSTALLATION ##

This is also indicated in setup.py

The packages that need to be installed because they are imported in various scripts:

'requests'
'bs4'

*IMPORTANT*
When you open 'backend-test.py', you will have an option to have these packages
installed automatically for you on your system.
It will look like the following:

import os
#os.system("pip install bs4")
#os.system("pip install requests")

Simply, uncomment the os.system commands and when you run the program, they will install
the required packages.

## MAIN USAGE ##
To use the program, open up the file 'backend-test.py' in the general directory. 

The file indicates input instructions for the program. 
They are repeated here:

Instructions:

1) URL input: needs to be in this specific format. Change the dealer name and dealer number. Leave the 
page number as 1. 
2) Leave as is or alter the number of pages  ('numpages') of reviews to find.
3) After done changing inputers, run the program. 
4) For the test suite, open 'test_backend-test.py'


## TEST SUITE PARAMETERS/USAGE ##

I used the following dealerships to test my program:

'Blue Knob Auto' 
and
'Best Chevrolet'

To run the test suite, open up 'test_backend-test.py' in the general directory and run the script. 
It will automatically run through all of the tests.

If all tests run without error, you will recieve an 'OK' output, otherwise the failures will be indicated.


## REVIEW RATING PARAMETERS ##

To calculate which reviews are the most positive of the 5 pages 
searched, I used 3 metrics:

1) Found the general rating that the reviewer gave the dealership and found the top reviews
in that category
2) Found the specific sub-category ratings ('Customer Service', 'Quality of Work', 'Friendliness', 'Pricing', and 'Overall Experience') and averaged them. I decided to 
add this metric on top of the general rating metric because I found several ratings that gave a 5-star rating but gave several of the sub-category ratings a 4 star or less rating. 
3) For the last metric, I used a list of positive and negative words to decide sentiment in the review's body text. For the positive and negative word lists, I used 

   Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA, 

which can be accessed at https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon.

