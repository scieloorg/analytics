# coding: utf-8
import os
import unittest

from analytics import utils

class UtilsTest(unittest.TestCase):

    def test_clean_string_1(self):

        result = utils.clean_string(u"Teste String, 1")

        self.assertEqual(result, u"teste string")

    def test_clean_string_2(self):

        result = utils.clean_string(u"Teste1")

        self.assertEqual(result, u"teste")

    def test_clean_string_3(self):

        result = utils.clean_string("Teste1")

        self.assertEqual(result, u"teste")