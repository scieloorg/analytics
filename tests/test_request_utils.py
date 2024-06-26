# coding: utf-8
import unittest

from analytics import request_utils


class RequestUtilsTest(unittest.TestCase):
    def test_generate_params_for_solr_top100articles_with_issn(self):
        issn = '0016-7169'
        collection = 'mex'
        year_month_day_range = '["2024-01-01T00:00:00Z" TO "2024-06-01T00:00:00Z"]'

        expected_results = {
            'q': '*:*', 
            'fq':[
                f'key_issn:{issn}',
                f'metric_scope:top100articles',
                f'collection:{collection}',
                f'year_month_day:{year_month_day_range}',
            ],
            'rows': 0,
        }

        obtained_results = request_utils.generate_params_for_solr_top100articles(collection, year_month_day_range, issn)

        self.assertDictEqual(expected_results, obtained_results)


    def test_generate_params_for_solr_top100articles_without_issn(self):
        collection = 'mex'
        year_month_day_range = '["2024-01-01T00:00:00Z" TO "2024-06-01T00:00:00Z"]'

        params = {
            'q': '*:*', 
            'fq':[
                f'metric_scope:top100articles',
                f'collection:{collection}',
                f'year_month_day:{year_month_day_range}',
            ],
            'rows': 0,
        }

        obtained_results = request_utils.generate_params_for_solr_top100articles(collection, year_month_day_range)

        self.assertDictEqual(obtained_results, params)
