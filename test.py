import unittest
import functions as f
import ClassBuilder as CB

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_build_control_list(self):
        expected = {'Agility': 1, 'Bulk': 1,
                    'Deduction': 1, 'Endurance': 1,
                    'Faith': 1, 'Instinct': 1,
                    'Recall': 1, 'Resolve': 1,
                    'Speed': 1, 'Tone': 1,
                    'Understanding': 1, 'Urge': 1}
        actual = f.build_control_list()
        self.assertEqual(expected, actual)


    def test_Character_Stats(self):
        expected = {'Agility': 1, 'Bulk': 1,
                    'Deduction': 1, 'Endurance': 1,
                    'Faith': 1, 'Instinct': 1,
                    'Recall': 1, 'Resolve': 1,
                    'Speed': 1, 'Tone': 1,
                    'Understanding': 1, 'Urge': 1}
        actual = CB.Character().Stats
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
