# coding: utf-8
import os
import unittest

from analytics import controller

def dummyclient(data):

    return data

class ControllerTest(unittest.TestCase):

    def setUp(self):

        self._stats = controller.Stats('localhost:11600', 'localhost:11600', 'localhost:11600', 'localhost:11600')

    def test_must_not_custom_query(self):
        result = [i for i in self._stats.bibliometrics.must_not_custom_query('0000-0000')]

        sorted_must_not = sorted([i['match']['reference_source_cleaned'] for i in result])

        expected = [
            u'ecol api',
            u'ecol apl',
            u'ecol apli',
            u'ecol aplic',
            u'ecol app',
            u'ecol appl',
            u'ecol applic',
            u'ecolapl',
            u'ecolappl',
            u'ecologia aplicada',
            u'econ adm',
            u'econ bol'
        ]

        self.assertEqual(sorted_must_not, expected)

    def test_fuzzy_custom_query(self):
        result = [i for i in self._stats.bibliometrics.fuzzy_custom_query(
            '0000-0000',
            ['teste1', 'teste2']
        )]


        sorted_fuzzy = []

        for item in result:
            sorted_fuzzy.append(
                u'_'.join([
                    item['fuzzy']['reference_source_cleaned']['value'],
                    str(item['fuzzy']['reference_source_cleaned']['max_expansions']),
                    str(item['fuzzy']['reference_source_cleaned']['fuzziness'])
                ])
            )

        expected = [
            u'econ aplic_50_3',
            u'economia aplicada_50_3',
            u'teste_50_3',
            u'teste_50_3'
        ]

        self.assertEqual(sorted(sorted_fuzzy), expected)

    def test_compute_impact_factor(self):

        pub_citing_years = {
            "hits": {
                "hits": [],
                "total": 1825,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 9059,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2008",
                                        "doc_count": 22
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 19
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 18
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 17
                                    },
                                    {
                                        "key": "2007",
                                        "doc_count": 17
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 15
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 15
                                    },
                                    {
                                        "key": "2011",
                                        "doc_count": 13
                                    },
                                    {
                                        "key": "2012",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2013",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2014",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1978",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1981",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2014",
                            "doc_count": 237
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2006",
                                        "doc_count": 30
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 24
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 22
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 18
                                    },
                                    {
                                        "key": "2007",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 14
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 13
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2011",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2012",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1976",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1978",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2013",
                            "doc_count": 230
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2006",
                                        "doc_count": 19
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 13
                                    },
                                    {
                                        "key": "2007",
                                        "doc_count": 13
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 9
                                    },
                                    {
                                      "key": "2001",
                                      "doc_count": 8
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1976",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1963",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1978",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1991",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2011",
                            "doc_count": 210
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2006",
                                        "doc_count": 17
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 15
                                    },
                                    {
                                        "key": "2007",
                                        "doc_count": 14
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 12
                                    },
                                    {
                                      "key": "2004",
                                      "doc_count": 11
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1983",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1981",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1982",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1948",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1954",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1979",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1984",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1991",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2010",
                            "doc_count": 193
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2007",
                                        "doc_count": 22
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 19
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 14
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 12
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 12
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2011",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2012",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1983",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1984",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2012",
                            "doc_count": 193
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2007",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 12
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1955",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1968",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1978",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1987",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 1
                                    }
                                ],
                               "doc_count_error_upper_bound": 0,
                               "sum_other_doc_count": 0
                           },
                           "key": "2009",
                           "doc_count": 143
                       },
                       {
                           "reference_publication_year": {
                               "buckets": [
                                    {
                                        "key": "2007",
                                        "doc_count": 16
                                    },
                                    {
                                        "key": "2010",
                                        "doc_count": 11
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 10
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2009",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2011",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2012",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "2013",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2008",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2014",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2015",
                            "doc_count": 126
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "2001",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 6
                                    },
                                    {
                                       "key": "2002",
                                       "doc_count": 6
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1989",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1979",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2007",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2008",
                            "doc_count": 84
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1999",
                                        "doc_count": 8
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1991",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2006",
                            "doc_count": 69
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2005",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1983",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2006",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2007",
                            "doc_count": 68
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2005",
                            "doc_count": 57
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1988",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2004",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1978",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1981",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2003",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2004",
                            "doc_count": 55
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 7
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "2000",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2003",
                            "doc_count": 44
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1995",
                                        "doc_count": 9
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1990",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1989",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "2002",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2002",
                            "doc_count": 35
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 5
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2000",
                            "doc_count": 24
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 6
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1999",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "2001",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1998",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "2001",
                            "doc_count": 21
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1996",
                                        "doc_count": 4
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1992",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1989",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1991",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1994",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1999",
                            "doc_count": 15
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1990",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1996",
                                        "doc_count": 3
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1997",
                                        "doc_count": 2
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1998",
                            "doc_count": 10
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1988",
                                        "doc_count": 2
                                    },
                                    {
                                        "key": "1991",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1995",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1996",
                            "doc_count": 5
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1984",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1988",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1989",
                            "doc_count": 2
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    },
                                    {
                                        "key": "1993",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1997",
                            "doc_count": 2
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1987",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1987",
                            "doc_count": 1
                        },
                        {
                            "reference_publication_year": {
                                "buckets": [
                                    {
                                        "key": "1986",
                                        "doc_count": 1
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "key": "1992",
                            "doc_count": 1
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        citable_docs = {
            "hits": {
                "hits": [],
                "total": 220,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 276,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "citable_documents": {
                                "doc_count": 21
                            },
                            "not_citable_documents": {
                                "doc_count": 2
                            },
                            "key": "2015",
                            "doc_count": 23
                        },
                        {
                            "citable_documents": {
                                "doc_count": 39
                            },
                            "not_citable_documents": {
                                "doc_count": 5
                            },
                            "key": "2014",
                            "doc_count": 44
                        },
                        {
                            "citable_documents": {
                                "doc_count": 24
                            },
                            "not_citable_documents": {
                                "doc_count": 9
                            },
                            "key": "2013",
                            "doc_count": 33
                        },
                        {
                            "citable_documents": {
                                "doc_count": 40
                            },
                            "not_citable_documents": {
                                "doc_count": 2
                            },
                            "key": "2012",
                            "doc_count": 42
                        },
                        {
                            "citable_documents": {
                                "doc_count": 41
                            },
                            "not_citable_documents": {
                                "doc_count": 1
                          },
                          "key": "2011",
                          "doc_count": 42
                        },
                        {
                            "citable_documents": {
                                "doc_count": 36
                            },
                            "not_citable_documents": {
                                "doc_count": 0
                            },
                            "key": "2010",
                            "doc_count": 36
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }


        result = self._stats._compute_impact_factor(pub_citing_years, citable_docs)

        expected = {
            "2015": {
                "fi": [
                    0.0,
                    0.07692307692307693,
                    0.14285714285714285,
                    0.1553398058252427,
                    0.1736111111111111,
                    0.2,
                ],
                "fi_citations": [
                    0.0,
                    3.0,
                    6.0,
                    7.0,
                    9.0,
                    11.0,
                ],
                "fi_documents": [
                    21,
                    39.0,
                    24.0,
                    40.0,
                    41.0,
                    36.0,
                ],
                "citable_docs": 21
            },
            "2014": {
                "fi": [
                    0.10256410256410256,
                    0.375,
                    0.3125,
                    0.3142857142857143,
                    0.36879432624113473,
                    0.4397163120567376
                ],
                "fi_citations": [
                    4.0,
                    9.0,
                    11.0,
                    13.0,
                    19.0,
                    10.0
                ],
                "fi_documents": [
                    39,
                    24.0,
                    40.0,
                    41.0,
                    36.0,
                    0.0
                ],
                "citable_docs": 39
            },
            "2011": {
                "fi": [
                    0.0,
                    0.16666666666666666,
                    0.4444444444444444,
                    0.8888888888888888,
                    1.25,
                    1.7777777777777777
                ],
                "fi_citations": [
                    0.0,
                    6.0,
                    10.0,
                    16.0,
                    13.0,
                    19.0
                ],
                "fi_documents": [
                    41,
                    36.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "citable_docs": 41
            },
            "2010": {
                "fi": [
                    0.027777777777777776,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "fi_citations": [
                    1.0,
                    5.0,
                    8.0,
                    14.0,
                    17.0,
                    8.0
                ],
                "fi_documents": [
                    36,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "citable_docs": 36
            },
            "2013": {
                "fi": [
                    0.0,
                    0.1,
                    0.13580246913580246,
                    0.29914529914529914,
                    0.48717948717948717,
                    0.6239316239316239,
                ],
                "fi_citations": [
                    0.0,
                    4.0,
                    7.0,
                    24.0,
                    22.0,
                    16.0,
                ],
                "fi_documents": [
                    24,
                    40.0,
                    41.0,
                    36.0,
                    0.0,
                    0.0
                ],
                "citable_docs": 24
            },
            "2012": {
                "fi": [
                    0.05,
                    0.04878048780487805,
                    0.2077922077922078,
                    0.4155844155844156,
                    0.6233766233766234,
                    0.9090909090909091
                ],
                "fi_citations": [
                    2.0,
                    2.0,
                    14.0,
                    16.0,
                    16.0,
                    22.0
                ],
                "fi_documents": [
                    40,
                    41.0,
                    36.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "citable_docs": 40
            }  
        }

        self.assertEqual(expected, result)

    def test_compute_citing_forms(self):

        query_result = {
            "hits": {
                "hits": [],
                "total": 14561,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 38818,
            "aggregations": {
                "reference_source": {
                    "buckets": [
                        {
                            "key": u"Rev Saúde Pública",
                            "doc_count": 8217
                        },
                        {
                            "key": u"Revista de Saúde Pública",
                            "doc_count": 3120
                        },
                        {
                            "key": u"Rev. Saúde Pública",
                            "doc_count": 1639
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = [
            {
                "source": u"Rev Saúde Pública",
                "count": 8217
            },
            {
                "source": u"Revista de Saúde Pública",
                "count": 3120
            },
            {
                "source": u"Rev. Saúde Pública",
                "count": 1639
            }
        ]

        result = self._stats.bibliometrics._compute_citing_forms(query_result)

        self.assertEqual(expected, result)

    def test_compute_received_citations(self):

        query_result = {
            "hits": {
                "hits": [],
                "total": 14549,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 29198,
            "aggregations": {
                "source": {
                    "buckets": [
                        {
                            "key": u"Cadernos de Saúde Pública",
                            "doc_count": 3607
                        },
                        {
                            "key": u"Revista de Saúde Pública",
                            "doc_count": 1714
                        },
                        {
                            "key": u"Ciência & Saúde Coletiva",
                            "doc_count": 935
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = [
            {
                "source": u"Cadernos de Saúde Pública",
                "count": 3607
            },
            {
                "source": u"Revista de Saúde Pública",
                "count": 1714
            },
            {
                "source": u"Ciência & Saúde Coletiva",
                "count": 935
            }
        ]

        result = self._stats.bibliometrics._compute_received_citations(query_result)

        self.assertEqual(expected, result)

    def test_compute_granted_citations(self):

        query_result = {
            "hits": {
                "hits": [],
                "total": 67602,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 4715,
            "aggregations": {
                "reference_source": {
                    "buckets": [
                        {
                            "key": u"Rev. Saúde públ.",
                            "doc_count": 1371
                        },
                        {
                            "key": u"Rev Saúde Pública",
                            "doc_count": 898
                        },
                        {
                            "key": u"Lancet",
                            "doc_count": 823
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = [
            {
                "source": u"Rev. Saúde públ.",
                "count": 1371
            },
            {
                "source": u"Rev Saúde Pública",
                "count": 898
            },
            {
                "source": u"Lancet",
                "count": 823
            }
        ]

        result = self._stats.bibliometrics._compute_granted_citations(query_result)

        self.assertEqual(expected, result)

    def test_compute_self_citations(self):
        query_result = {
            "hits": {
                "hits": [],
                "total": 1714,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 13686,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "key": "1993",
                            "doc_count": 119
                        },
                        {
                            "key": "1994",
                            "doc_count": 83
                        },
                        {
                            "key": "1995",
                            "doc_count": 111
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }        

        expected = {
            "series": [
                {
                    "data": [
                        119,
                        83,
                        111
                    ],
                    "name": "self_citations"
                }
            ],
            "categories": [
                "1993",
                "1994",
                "1995"
            ]
        }

        result = self._stats.bibliometrics._compute_self_citations(query_result)

        self.assertEqual(expected, result)

    def test_compute_received_self_and_granted_citation_chart(self):

        self_citations = {
            "hits": {
                "hits": [],
                "total": 8676,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 98,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "key": "2012",
                            "doc_count": 616
                        },
                        {
                            "key": "2013",
                            "doc_count": 594
                        },
                        {
                            "key": "2014",
                            "doc_count": 1102
                        },
                        {
                            "key": "2015",
                            "doc_count": 584
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        granted_citations = {
            "hits": {
                "hits": [],
                "total": 5912,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 6,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "citations": {
                                "value": 8696.0
                            },
                            "key": "2014",
                            "doc_count": 316
                        },
                        {
                            "citations": {
                                "value": 8614.0
                            },
                            "key": "2013",
                            "doc_count": 306
                        },
                        {
                            "citations": {
                                "value": 7423.0
                            },
                            "key": "2012",
                            "doc_count": 273
                        },
                        {
                            "citations": {
                                "value": 5574.0
                            },
                            "key": "2015",
                            "doc_count": 188
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        received_citations = {
            "hits": {
                "hits": [],
                "total": 44045,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 2018,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "key": "2014",
                            "doc_count": 6645
                        },
                        {
                            "key": "2013",
                            "doc_count": 5030
                        },
                        {
                            "key": "2012",
                            "doc_count": 4684
                        },
                        {
                            "key": "2015",
                            "doc_count": 3984
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = {
            "series": [
                {
                    "data": [
                        7423.0,
                        8614.0,
                        8696.0,
                        5574.0
                    ],
                    "name": "granted_citation"
                },
                {
                    "data": [
                        4684,
                        5030,
                        6645,
                        3984
                    ],
                    "name": "received_citation"
                },
                {
                    "data": [
                        616,
                        594,
                        1102,
                        584
                    ],
                    "name": "self_citation"
                }
            ],
            "categories": [
                "2012",
                "2013",
                "2014",
                "2015"
            ]
        }

        self.assertEqual(expected,
            self._stats._compute_received_self_and_granted_citation_chart(
                self_citations,
                granted_citations,
                received_citations
            )
        )

    def test_collection_size_documents(self):
        query_result = {
            "hits": {
                "hits": [],
                "total": 297733,
                "max_score": 0.0
            },
            "took": 9,
            "timed_out": False,
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = {
            "total": 297733
        }

        result = self._stats.publication._compute_collection_size(query_result, 'documents')

        self.assertEqual(expected, result)

    def test_collection_size_issn(self):
        query_result = {
            "took": 11,
            "timed_out": False,
            "_shards": {
                "total": 5,
                "successful": 5,
                "failed": 0
            },
            "hits": {
                "total": 297733,
                "max_score": 0,
                "hits": []
            },
            "aggregations": {
                "issn": {
                    "value": 344
                }
            }
        }

        expected = {
            "total": 344
        }

        result = self._stats.publication._compute_collection_size(query_result, 'issn')

        self.assertEqual(expected, result)

    def test_collection_size_issue(self):
        query_result = {
            "took": 11,
            "timed_out": False,
            "_shards": {
                "total": 5,
                "successful": 5,
                "failed": 0
            },
            "hits": {
                "total": 297733,
                "max_score": 0,
                "hits": []
            },
            "aggregations": {
                "issue": {
                    "value": 3440
                }
            }
        }

        expected = {
            "total": 3440
        }

        result = self._stats.publication._compute_collection_size(query_result, 'issue')

        self.assertEqual(expected, result)

    def test_collection_size_none(self):
        query_result = {
            "took": 11,
            "timed_out": False,
            "_shards": {
                "total": 5,
                "successful": 5,
                "failed": 0
            },
            "hits": {
                "total": 297733,
                "max_score": 0,
                "hits": []
            }
        }

        result = self._stats.publication._compute_collection_size(query_result, 'issn')

        self.assertEqual(None, result)

    def test_publishing_citable_documents(self):
        query_result = {
            "hits": {
                "hits": [],
                "total": 295525,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 7,
            "aggregations": {
                "publication_year": {
                    "buckets": [
                        {
                            "citable_documents": {
                                "doc_count": 16341
                            },
                            "not_citable_documents": {
                                "doc_count": 1957
                            },
                            "key": "2008",
                            "doc_count": 18298
                        },
                        {
                            "citable_documents": {
                                "doc_count": 15096
                            },
                            "not_citable_documents": {
                                "doc_count": 2189
                            },
                            "key": "2007",
                            "doc_count": 17285
                        },
                        {
                            "citable_documents": {
                                "doc_count": 13410
                            },
                            "not_citable_documents": {
                                "doc_count": 1925
                            },
                            "key": "2006",
                            "doc_count": 15335
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 101636
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = {
            "series": [
                {
                    "data": [
                        {"y": 13410, "percentage": 87.44701662862732},
                        {"y": 15096, "percentage": 87.33584032398034},
                        {"y": 16341, "percentage": 89.30484205924145}
                    ],
                    "name": "citable_documents"
                },
                {
                    "data": [
                        {"y": 1925, "percentage": 12.552983371372678},
                        {"y": 2189, "percentage": 12.66415967601967},
                        {"y": 1957, "percentage": 10.695157940758552}
                    ],
                    "name": "not_citable_documents"
                }
            ],
            "categories": [
                "2006",
                "2007",
                "2008"
            ]
        }

        result = self._stats.publication._compute_citable_documents(query_result)\

        self.assertEqual(expected, result)

    def test_publishing_general(self):
        query_result = {
            "hits": {
                "hits": [],
                "total": 345,
                "max_score": 0.0
            },
            "timed_out": False,
            "took": 3,
            "aggregations": {
                "subject_areas": {
                    "buckets": [
                        {
                            "key": "Health Sciences",
                            "doc_count": 113
                        },
                        {
                            "key": "Human Sciences",
                            "doc_count": 95
                        },
                        {
                            "key": "Agricultural Sciences",
                            "doc_count": 46
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "_shards": {
                "successful": 5,
                "failed": 0,
                "total": 5
            }
        }

        expected = {
            "series": [
                {
                    "data": [
                        113,
                        95,
                        46
                    ],
                    "name": "documents"
                }
            ],
            "categories": [
                "Health Sciences",
                "Human Sciences",
                "Agricultural Sciences"
            ]
        }

        result = self._stats.publication._compute_general(query_result, 'subject_areas')

        self.assertEqual(expected, result)

    def test_access_list_journals(self):
        query_result = {
            "timed_out": False,
            "hits": {
                "hits": [],
                "max_score": 0.0,
                "total": 9096505
            },
            "_shards": {
                "failed": 0,
                "successful": 5,
                "total": 5
            },
            "took": 1356,
            "aggregations": {
                "issn": {
                    "sum_other_doc_count": 0,
                    "buckets": [
                        {
                            "1": {
                                "value": 14133618.0
                            },
                            "doc_count": 86040,
                            "key": "0104-1169",
                            "journal_title": {
                                "sum_other_doc_count": 0,
                                "buckets": [
                                    {
                                        "doc_count": 86040,
                                        "access_html": {
                                            "value": 6378338.0
                                        },
                                        "access_pdf": {
                                            "value": 7189379.0
                                        },
                                        "access_total": {
                                            "value": 14133618.0
                                        },
                                        "access_abstract": {
                                            "value": 553883.0
                                        },
                                        "key": "Revista Latino-Americana de Enfermagem",
                                        "access_epdf": {
                                            "value": 12018.0
                                        }
                                    }
                                ],
                                "doc_count_error_upper_bound": 0
                            }
                        },
                        {
                            "1": {
                                "value": 13225925.0
                            },
                            "doc_count": 193783,
                            "key": "0102-311X",
                            "journal_title": {
                                "sum_other_doc_count": 0,
                                "buckets": [
                                    {
                                        "doc_count": 193783,
                                        "access_html": {
                                            "value": 7019935.0
                                        },
                                        "access_pdf": {
                                            "value": 5444060.0
                                        },
                                        "access_total": {
                                            "value": 13225925.0
                                        },
                                        "access_abstract": {
                                            "value": 751424.0
                                        },
                                        "key": "Cadernos de Sa\u00fade P\u00fablica",
                                        "access_epdf": {
                                            "value": 10506.0
                                        }
                                    }
                                ],
                                "doc_count_error_upper_bound": 0
                            }
                        }
                    ],
                    "doc_count_error_upper_bound": 0
                }
            }
        }

        expected = [
            {
                "html": 6378338,
                "pdf": 7189379,
                "epdf": 12018,
                "issn": "0104-1169",
                "title": "Revista Latino-Americana de Enfermagem",
                "abstract": 553883,
                "total": 14133618
            },
            {
                "html": 7019935,
                "pdf": 5444060,
                "epdf": 10506,
                "issn": "0102-311X",
                "title": "Cadernos de Sa\u00fade P\u00fablica",
                "abstract": 751424,
                "total": 13225925
            }
        ]

        result = self._stats.access._compute_list_journals(query_result)

        self.assertEqual(expected, result)

    def test_access_list_issues(self):
        query_result = {
            "hits": {
                "hits": [],
                "max_score": 0.0,
                "total": 9096505
            },
            "aggregations": {
                "issue": {
                    "buckets": [
                        {
                            "issue_title": {
                                "buckets": [
                                    {
                                        "doc_count": 540,
                                        "access_epdf": {
                                            "value": 1272.0
                                        },
                                        "access_total": {
                                            "value": 780479.0
                                        },
                                        "access_abstract": {
                                            "value": 346.0
                                        },
                                        "access_pdf": {
                                            "value": 80145.0
                                        },
                                        "key": "Rev. Bras. Psiquiatr., n.22 v. suppl 2, 2000",
                                        "access_html": {
                                            "value": 698716.0
                                        }
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "doc_count": 540,
                            "key": "S1516-444620000006",
                            "1": {
                                "value": 780479.0
                            }
                        },
                        {
                            "issue_title": {
                                "buckets": [
                                    {
                                        "doc_count": 537,
                                        "access_epdf": {
                                            "value": 448.0
                                        },
                                        "access_total": {
                                            "value": 607590.0
                                        },
                                        "access_abstract": {
                                            "value": 5323.0
                                        },
                                        "access_pdf": {
                                            "value": 139714.0
                                        },
                                        "key": "S\u00e3o Paulo Perspec., n.14 v.2, 2000",
                                        "access_html": {
                                            "value": 462105.0
                                        }
                                    }
                                ],
                                "doc_count_error_upper_bound": 0,
                                "sum_other_doc_count": 0
                            },
                            "doc_count": 537,
                            "key": "S0102-883920000002",
                            "1": {
                                "value": 607590.0
                            }
                        }
                    ],
                    "doc_count_error_upper_bound": -1,
                    "sum_other_doc_count": 9003586
                }
            },
            "_shards": {
                "successful": 5,
                "total": 5,
                "failed": 0
            },
            "timed_out": False,
            "took": 2867
        }

        expected = [
            {
                "total": 780479,
                "abstract": 346,
                "title": "Rev. Bras. Psiquiatr., n.22 v. suppl 2, 2000",
                "issue": "S1516-444620000006",
                "pdf": 80145,
                "epdf": 1272,
                "html": 698716
            },
            {
                "total": 607590,
                "abstract": 5323,
                "title": "S\u00e3o Paulo Perspec., n.14 v.2, 2000",
                "issue": "S0102-883920000002",
                "pdf": 139714,
                "epdf": 448,
                "html": 462105
            }
        ]

        result = self._stats.access._compute_list_issues(query_result)

        self.assertEqual(expected, result)

    def test_access_list_articles(self):
        query_result = {
            "hits": {
                "hits": [],
                "total": 8988926,
                "max_score": 0.0
            },
            "aggregations": {
                "pid": {
                    "buckets": [
                        {
                            "1": {
                                "value": 362909.0
                            },
                            "document_title": {
                                "buckets": [
                                    {
                                        "access_total": {
                                            "value": 362909.0
                                        },
                                        "doc_count": 36,
                                        "access_epdf": {
                                            "value": 57.0
                                        },
                                        "access_html": {
                                            "value": 66582.0
                                        },
                                        "access_pdf": {
                                            "value": 295969.0
                                        },
                                        "key": "S\u00edfilis: diagn\u00f3stico, tratamento e controle",
                                        "access_abstract": {
                                            "value": 301.0
                                        }
                                    }
                                ],
                                "sum_other_doc_count": 0,
                                "doc_count_error_upper_bound": 0
                            },
                            "key": "S0365-05962006000200002",
                            "doc_count": 36
                        },
                        {
                            "1": {
                                "value": 280553.0
                            },
                            "document_title": {
                                "buckets": [
                                    {
                                        "access_total": {
                                            "value": 280553.0
                                        },
                                        "doc_count": 36,
                                        "access_epdf": {
                                            "value": 42.0
                                        },
                                        "access_html": {
                                            "value": 47265.0
                                        },
                                        "access_pdf": {
                                            "value": 231820.0
                                        },
                                        "key": "Educa\u00e7\u00e3o ambiental, cidadania e sustentabilidade",
                                        "access_abstract": {
                                            "value": 1426.0
                                        }
                                    }
                                ],
                                "sum_other_doc_count": 0,
                                "doc_count_error_upper_bound": 0
                            },
                            "key": "S0100-15742003000100008",
                            "doc_count": 36
                        }
                    ],
                    "sum_other_doc_count": 8985357,
                    "doc_count_error_upper_bound": -1
                }
            },
            "took": 11594,
            "_shards": {
                "total": 5,
                "failed": 0,
                "successful": 5
            },
            "timed_out": False
        }

        expected = [
            {
                "total": 362909,
                "pdf": 295969,
                "epdf": 57,
                "pid": "S0365-05962006000200002",
                "abstract": 301,
                "html": 66582,
                "title": "S\u00edfilis: diagn\u00f3stico, tratamento e controle"
            },
            {
                "total": 280553,
                "pdf": 231820,
                "epdf": 42,
                "pid": "S0100-15742003000100008",
                "abstract": 1426,
                "html": 47265,
                "title": "Educa\u00e7\u00e3o ambiental, cidadania e sustentabilidade"
            }
        ]

        result = self._stats.access._compute_list_articles(query_result)

        self.assertEqual(expected, result)

    def test_access_by_month_and_year(self):
        query_result = {
            "_shards": {
                "failed": 0,
                "successful": 5,
                "total": 5
            },
            "took": 1076,
            "hits": {
                "max_score": 0.0,
                "hits": [],
                "total": 9096505
            },
            "timed_out": False,
            "aggregations": {
                "access_date": {
                    "sum_other_doc_count": 0,
                    "buckets": [
                        {
                            "doc_count": 217165,
                            "access_html": {
                                "value": 10618450.0
                            },
                            "key": 1349049600000,
                            "key_as_string": "2012-10-01T00:00:00.000Z",
                            "access_abstract": {
                                "value": 622582.0
                            },
                            "access_pdf": {
                                "value": 7826804.0
                            },
                            "access_epdf": {
                                "value": 0.0
                            }
                        },
                        {
                            "doc_count": 218929,
                            "access_html": {
                                "value": 10179396.0
                            },
                            "key": 1351728000000,
                            "key_as_string": "2012-11-01T00:00:00.000Z",
                            "access_abstract": {
                                "value": 558493.0
                            },
                            "access_pdf": {
                                "value": 7363352.0
                            },
                            "access_epdf": {
                                "value": 0.0
                            }
                        }
                    ],
                    "doc_count_error_upper_bound": 0
                }
            }
        }

        expected = {
            "categories": [
                "2012-10",
                "2012-11"
            ],
            "series": [
                {
                    "data": [
                        10618450,
                        10179396
                    ],
                    "name": "html"
                },
                {
                    "data": [
                        7826804,
                        7363352
                    ],
                    "name": "pdf"
                },
                {
                    "data": [
                        622582,
                        558493
                    ],
                    "name": "abstract"
                },
                {
                    "data": [
                        0,
                        0
                    ],
                    "name": "epdf"
                }
            ]
        }

        result = self._stats.access._compute_access_by_month_and_year(query_result)

        self.assertEqual(expected, result)

    def test_access_lifetime(self):

        query_result = {
            "aggregations": {
                "access_year": {
                    "sum_other_doc_count": 0,
                    "buckets": [
                        {
                            "publication_year": {
                                "sum_other_doc_count": 108463,
                                "buckets": [
                                    {
                                        "access_total": {
                                            "value": 20562877.0
                                        },
                                        "key": "2010",
                                        "doc_count": 249529
                                    },
                                    {
                                        "access_total": {
                                            "value": 19525384.0
                                        },
                                        "key": "2011",
                                        "doc_count": 263691
                                    }
                                ],
                                "doc_count_error_upper_bound": 0
                            },
                            "access_total": {
                                "value": 235613185.0
                            },
                            "key": "2014",
                            "doc_count": 3140466
                        },
                        {
                            "publication_year": {
                                "sum_other_doc_count": 86601,
                                "buckets": [
                                    {
                                        "access_total": {
                                            "value": 19635186.0
                                        },
                                        "key": "2010",
                                        "doc_count": 247910
                                    },
                                    {
                                        "access_total": {
                                            "value": 18294439.0
                                        },
                                        "key": "2011",
                                        "doc_count": 262403
                                    }
                                ],
                                "doc_count_error_upper_bound": 0
                            },
                            "access_total": {
                                "value": 208556239.0
                            },
                            "key": "2013",
                            "doc_count": 2837727
                        }
                    ],
                    "doc_count_error_upper_bound": 0
                }
            },
            "timed_out": False,
            "hits": {
                "hits": [],
                "total": 9096505,
                "max_score": 0.0
            },
            "took": 1274,
            "_shards": {
                "successful": 5,
                "total": 5,
                "failed": 0
            }
        }

        expected = [
            {
                "series": [
                    {
                        "name": "2014",
                        "data": [
                            20562877,
                            19525384
                        ]
                    }
                ],
                "categories": [
                    "2010",
                    "2011"
                ]
            },
            {
                "series": [
                    {
                        "name": "2013",
                        "data": [
                            19635186,
                            18294439
                        ]
                    }
                ],
                "categories": [
                    "2010",
                    "2011"
                ]
            }
        ]

        result = self._stats.access._compute_access_lifetime(query_result)

        self.assertEqual(expected, result)

    def test_access_by_document_type(self):

        query_result = {
            "aggregations": {
                "document_type": {
                    "buckets": [
                        {
                            "key": "research-article",
                            "doc_count": 7685721,
                            "access_total": {
                                "value": 580877253.0
                            }
                        },
                        {
                            "key": "editorial",
                            "doc_count": 314218,
                            "access_total": {
                                "value": 12498337.0
                            }
                        },
                        {
                            "key": "review-article",
                            "doc_count": 284110,
                            "access_total": {
                                "value": 32075009.0
                            }
                        }
                    ],
                    "doc_count_error_upper_bound": 0,
                    "sum_other_doc_count": 0
                }
            },
            "took": 670,
            "_shards": {
                "failed": 0,
                "total": 5,
                "successful": 5
            },
            "hits": {
                "total": 9096505,
                "max_score": 0.0,
                "hits": []
            },
            "timed_out": False
        }

        expected = {
            "series": [
                {
                    "data": [
                        {
                            "name": "research-article",
                            "y": 580877253.0
                        },
                        {
                            "name": "editorial",
                            "y": 12498337.0
                        },
                        {
                            "name": "review-article",
                            "y": 32075009.0
                        }
                    ],
                    "name": "Document Type"
                }
            ]
        }

        result = self._stats.access._compute_access_by_document_type(query_result)

        self.assertEqual(expected, result)