### TEST SUITE ###

# Instructions:
# 1) Run the files
# 2) Check output. If 'OK' all modules are good. 

## IMPORT UNITTEST ##
import unittest 

# Import local modules to test #
from scraper import scraper
from reviews import top_three
from dictionary import dictionary

class TestBackend(unittest.TestCase):
    def setUp(self):

        # First Dealership Test Case: Blue Knob Auto
        self.URL_1 = 'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page1/?filter=ALL_REVIEWS'
        self.pagelist_1 = ['https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page1/?filter=ALL_REVIEWS', 
        'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page2/?filter=ALL_REVIEWS', 
        'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page3/?filter=ALL_REVIEWS', 
        'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page4/?filter=ALL_REVIEWS',
        'https://www.dealerrater.com/dealer/Blue-Knob-Auto-review-20337/page5/?filter=ALL_REVIEWS'
        ]

        # Second Dealership Test Case: Best Chevrolet
        self.URL_2 = 'https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page1/?filter=ALL_REVIEWS'
        self.pagelist_2 = ['https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page1/?filter=ALL_REVIEWS',
        'https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page2/?filter=ALL_REVIEWS',
        'https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page3/?filter=ALL_REVIEWS',
        'https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page4/?filter=ALL_REVIEWS',
        'https://www.dealerrater.com/dealer/Best-Chevrolet-review-1698/page5/?filter=ALL_REVIEWS'
        ]

        self.fakereviews = ['good\n', '', '', '', 'happy\n', '', '', '', '', '', '', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', '', 'good good.', '', '', '', '', '', '', '', '', '', '', '', '', '', 
        '', '', '', '', '', '', '', '', '']
    def tearDown(self):
        pass

    def test_dictionary(self):
        #test to see if dicts are being filled
        neg_dict, pos_dict, neg_dict_strip, pos_dict_strip = dictionary.dictionary()

        self.assertGreater(len(neg_dict), 100)
        self.assertGreater(len(pos_dict), 100)

    def test_pages(self): 
        
        self.assertEqual(len(scraper.pages(self.URL_1, 5)), 5)
        self.assertEqual(len(scraper.pages(self.URL_2, 3)), 3)

    def test_reviewlist(self):

        self.assertGreater(len(scraper.reviewlist(self.pagelist_1)), 40)
        self.assertGreater(len(scraper.reviewlist(self.pagelist_2)), 40)

    def test_generalrating(self):
        self.assertEqual(len(scraper.generalrating(self.pagelist_1)), 50)
        self.assertEqual(len(scraper.generalrating(self.pagelist_2)), 50)

    def test_specificratings(self):
        # Testing to see if the first review on page 1 for Blue Knob Auto 
        # specific rating breakdown equals an average of 1.0
        self.assertEqual((scraper.specificratings(self.pagelist_1))[0], 1.0)

        # Testing to see if the 6th review on page 1 for Best Chevrolet
        # specific rating breakdown equals an average of 5.0
        self.assertEqual((scraper.specificratings(self.pagelist_2))[5], 5.0)

    def test_positivewords(self):
        self.assertEqual(len(scraper.positivewords(self.fakereviews)), 50)

    def test_totalreviewscore(self):
        # Test the totalreviewscore list generation through running through all of the other
        # functions, as it is fully dependent on them.
        URLs = scraper.pages(self.URL_1, 5)
        allreviews = scraper.reviewlist(URLs)
        generalratings = scraper.generalrating(URLs)
        specificratings = scraper.specificratings(URLs)
        numpositivewords = scraper.positivewords(allreviews)

        topreviews, topscores = top_three.totalreviewscore(allreviews,
         generalratings, specificratings, numpositivewords)

        self.assertEqual(len(topreviews), len(topscores))
    def test_printtop3(self):

        URLs = scraper.pages(self.URL_2, 5)
        allreviews = scraper.reviewlist(URLs)
        generalratings = scraper.generalrating(URLs)
        specificratings = scraper.specificratings(URLs)
        numpositivewords = scraper.positivewords(allreviews)

        topreviews, topscores = top_three.totalreviewscore(allreviews,
         generalratings, specificratings, numpositivewords)

        self.assertEqual(len(top_three.printtop3(topreviews, topscores, allreviews)), 3)


# automatically run test suite
if __name__=='__main__':
    unittest.main()