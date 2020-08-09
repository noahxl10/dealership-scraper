
## Module 'top_three' includes a function, 'totalreviewscore', that 
# takes inputs from the 'scraper' modules 
# and calculates the top three most positive reviews

# Function 'printtop3' prints the top 3 post positive reviews in order of severity


def totalreviewscore(reviewlist, ratings, breakdown, pos_words):

    ratings_max = 0 # initalization
    index_1 = []
    # For loop to find max of ratings to set generalmax baseline
    # Sort then indexing didn't work
    for i in range(len(ratings)):
        if (ratings[i] > ratings_max) or (ratings[i] == ratings_max): 
            #find all maxes to index third highest value
            ratings_max = ratings[i]
            index_1.append(ratings[i])
    
    generalmax = index_1[-3] # set general max = to ratings_max

    index_2 = []
    for i in range(len(reviewlist)):
        if (ratings[i] > generalmax) or (ratings[i] == generalmax):
            generalmax = ratings[i]
            index_2.append(i)

    index_3, index_4, index_5, index_6, value_index = ([] for i in range(5)) #initialize best values index

    maxwords = 0 # initialize comparison max positive words variable
    for i in index_2: #find individual breakdowns to remove scores that are 5 but dont score others well

        poswords = pos_words[i]

        index_3.append(breakdown[i])

        index_4.append(len(poswords))
        val = breakdown[i] + len(poswords)
        index_5.append(val)

    sumval = 0
    for i in range(len(index_2)):
        if (index_5[i] > sumval) or (index_5[i] == sumval):
            sumval = index_5[i]
            index_6.append(index_5[i])
            value_index.append(index_2[i])

    top_reviews = [value_index[-3], value_index[-2], value_index[-1]]
    top_scores = [index_6[-3], index_6[-2], index_6[-1]]

    return top_reviews, top_scores


def printtop3(top_reviews, top_scores, allreviews):
    revieworder =  []
    for i in top_reviews:
        revieworder.append(allreviews[i])

    revieworder.reverse()
    return revieworder