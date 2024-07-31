# coding: utf-8
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

    def test_convert_date_range_filter_to_solr_format(self):
        begin_date = '2024-01-01'
        end_date = '2024-06-01'
        results = utils.convert_date_range_filter_to_solr_format(begin_date=begin_date, end_date=end_date)

        self.assertEqual(results, '["2024-01-01T00:00:00Z" TO "2024-06-01T00:00:00Z"]')
