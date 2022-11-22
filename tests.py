import scoring
import unittest


class Test_Scorer(unittest.TestCase):
    def test_add(self):
        scorer = scoring.Scorer()
        result = scorer.add(2, 3)
        self.assertEqual(result, 5)

    def test_parse(self):
        scorer = scoring.Scorer()
        parsed_input = scorer.parse("(1, 3, 3, 2, 5) fullhouse")
        self.assertEqual(parsed_input, (['1', '3', '3', '2', '5'], 'fullhouse'))

if __name__ == '__main__':
    unittest.main()
