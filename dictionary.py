## Dictionary for use in sentiment analysis ##

# Import libraries
import os

# Defining __location__ to pull positive.txt and 
# negative.txt in any folder instead of having a specific directory
def dictionary():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    pos = open(os.path.join(__location__, 'positive.txt'))
    neg = open(os.path.join(__location__, 'negative.txt'), encoding = "ISO-8859-1")


    # Initializing dicts
    negdict, negdictstrip, posdict, posdictstrip = ({} for i in range(4)) 
    # negative word dictionary
    # negative word dictionary without \n
    # positive word dictionary
    # positive word dictionary without \n


    poswords = pos.readlines() # list of positive words from positive.txt
    negwords = neg.readlines() # list of negative words from negative.txt

    # for loop to fill positive sentiment word dicts
    for i in range(len(poswords)):
        posdict[i] = poswords[i]
        posdictstrip[i] = poswords[i].rstrip()
        
    # for loop to fill negative sentiment word dicts
    for i in range(len(negwords)):
        negdict[i] = negwords[i]
        negdictstrip[i] = negwords[i].rstrip()
        
    return negdict, posdict, negdictstrip, posdictstrip
