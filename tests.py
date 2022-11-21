import scoring
import unittest


class Test_Scorer(unittest.TestCase):
    def test_add(self):
        scorer = scoring.Scorer()
        result = scorer.add(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
