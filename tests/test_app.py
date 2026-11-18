import unittest
from color_notes import rgb, contrast

class ColorTest(unittest.TestCase):
    def test_short_hex(self):
        self.assertEqual(rgb('#abc'), (170,187,204))
    def test_extremes(self):
        self.assertAlmostEqual(contrast(rgb('000'),rgb('fff')), 21)
        self.assertAlmostEqual(contrast(rgb('abc'),rgb('abc')), 1)
    def test_invalid(self):
        for s in ['ggg','1234','']:
            with self.assertRaises(ValueError): rgb(s)
