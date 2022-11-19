import unittest
import time
from lab5.main import do_rabin_karp


class TestDoRabinKarp(unittest.TestCase):

    def test1(self):
        self.text = "(Do I wanna know?) If this feelin' flows both ways?"\
                    "(Sad to see you go) Was sorta hopin' that you'd stay"
        self.pattern = "Do"
        self.match_idx = [1]
        start = time.time()
        self.assertEqual(do_rabin_karp(self.pattern, self.text), self.match_idx)
        print("test1: ", time.time() - start)

    def test2(self):
        self.text = "(Baby, we both know) That the nights were mainly made"
        self.pattern = "I"
        self.match_idx = []
        start = time.time()
        self.assertEqual(do_rabin_karp(self.pattern, self.text), self.match_idx)
        print("test2: ", time.time() - start)

    def test3(self):
        self.text = "For sayin' things that you can't say tomorrow day"\
                    "Crawlin' back to you." \
                    "Ever thought of callin' when" \
                    "You've had a few?" \
                    "'Cause I always do" \
                    "Maybe I'm too" \
                    "Busy bein' yours" \
                    "To fall for somebody new" \
                    "Now, I've thought it through" \
                    "Crawlin' back to you"
        self.pattern = "yours"
        self.match_idx = [157]
        start = time.time()
        self.assertEqual(do_rabin_karp(self.pattern, self.text), self.match_idx)
        print("test3: ", time.time() - start)


if __name__ == '__main__':
    unittest.main()

