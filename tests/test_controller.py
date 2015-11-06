# coding: utf-8
import os
import unittest

from analytics import controller

def dummyclient(data):

    return data

class ControllerTest(unittest.TestCase):

    def setUp(self):

        self._stats = controller.Stats('localhost:11600', 'localhost:11600', 'localhost:11600', 'localhost:11600')

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
                "fi2": 0.14285714285714285,
                "fi3": 0.1553398058252427,
                "fi0": 0.0,
                "fi1": 0.07692307692307693,
                "citable_docs5": 36.0,
                "fi4": 0.1736111111111111,
                "fi5": 0.2,
                "citable_docs3": 40.0,
                "citable_docs2": 24.0,
                "citable_docs1": 39.0,
                "citable_docs0": 21,
                "citable_docs": 21,
                "citable_docs4": 41.0,
                "citing_count5": 11.0,
                "citing_count4": 9.0,
                "citing_count1": 3.0,
                "citing_count0": 0.0,
                "citing_count3": 7.0,
                "citing_count2": 6.0
            },
            "2014": {
                "fi2": 0.3125,
                "fi3": 0.3142857142857143,
                "fi0": 0.10256410256410256,
                "fi1": 0.375,
                "citable_docs5": 0.0,
                "fi4": 0.36879432624113473,
                "fi5": 0.4397163120567376,
                "citable_docs3": 41.0,
                "citable_docs2": 40.0,
                "citable_docs1": 24.0,
                "citable_docs0": 39,
                "citable_docs": 39,
                "citable_docs4": 36.0,
                "citing_count5": 10.0,
                "citing_count4": 19.0,
                "citing_count1": 9.0,
                "citing_count0": 4.0,
                "citing_count3": 13.0,
                "citing_count2": 11.0
            },
            "2011": {
                "fi2": 0.4444444444444444,
                "fi3": 0.8888888888888888,
                "fi0": 0.0,
                "fi1": 0.16666666666666666,
                "citable_docs5": 0.0,
                "fi4": 1.25,
                "fi5": 1.7777777777777777,
                "citable_docs3": 0.0,
                "citable_docs2": 0.0,
                "citable_docs1": 36.0,
                "citable_docs0": 41,
                "citable_docs": 41,
                "citable_docs4": 0.0,
                "citing_count5": 19.0,
                "citing_count4": 13.0,
                "citing_count1": 6.0,
                "citing_count0": 0.0,
                "citing_count3": 16.0,
                "citing_count2": 10.0
            },
            "2010": {
                "fi2": 0,
                "fi3": 0,
                "fi0": 0.027777777777777776,
                "fi1": 0,
                "citable_docs5": 0.0,
                "fi4": 0,
                "fi5": 0,
                "citable_docs3": 0.0,
                "citable_docs2": 0.0,
                "citable_docs1": 0.0,
                "citable_docs0": 36,
                "citable_docs": 36,
                "citable_docs4": 0.0,
                "citing_count5": 8.0,
                "citing_count4": 17.0,
                "citing_count1": 5.0,
                "citing_count0": 1.0,
                "citing_count3": 14.0,
                "citing_count2": 8.0
            },
            "2013": {
                "fi2": 0.13580246913580246,
                "fi3": 0.29914529914529914,
                "fi0": 0.0,
                "fi1": 0.1,
                "citable_docs5": 0.0,
                "fi4": 0.48717948717948717,
                "fi5": 0.6239316239316239,
                "citable_docs3": 36.0,
                "citable_docs2": 41.0,
                "citable_docs1": 40.0,
                "citable_docs0": 24,
                "citable_docs": 24,
                "citable_docs4": 0.0,
                "citing_count5": 16.0,
                "citing_count4": 22.0,
                "citing_count1": 4.0,
                "citing_count0": 0.0,
                "citing_count3": 24.0,
                "citing_count2": 7.0
            },
            "2012": {
                "fi2": 0.2077922077922078,
                "fi3": 0.4155844155844156,
                "fi0": 0.05,
                "fi1": 0.04878048780487805,
                "citable_docs5": 0.0,
                "fi4": 0.6233766233766234,
                "fi5": 0.9090909090909091,
                "citable_docs3": 0.0,
                "citable_docs2": 36.0,
                "citable_docs1": 41.0,
                "citable_docs0": 40,
                "citable_docs": 40,
                "citable_docs4": 0.0,
                "citing_count5": 22.0,
                "citing_count4": 16.0,
                "citing_count1": 2.0,
                "citing_count0": 2.0,
                "citing_count3": 16.0,
                "citing_count2": 14.0
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

    def test_citation_self_citation(self):
        self_citations = {
            "series": [
                {
                    "data": [
                        20,
                        22,
                        33,
                        21
                    ],
                    "name": "self_citations"
                }
            ],
            "categories": [
                "2000",
                "2001",
                "2002",
                "2003"
            ]
        }

        citations = {
            "series": [
                {
                    "data": [
                        269,
                        445,
                        869,
                        558
                    ],
                    "name": "citations"
                }
            ],
            "categories": [
                "1999",
                "2000",
                "2001",
                "2002"
            ]
        }

        expected = {
            "series": [
                {
                    "data": [
                        269,
                        445,
                        869,
                        558,
                        0
                    ],
                    "name": "citations"
                },
                {
                    "data": [
                        0,
                        20,
                        22,
                        33,
                        21
                    ],
                    "name": "self_citations"
                }
            ],
            "categories": [
                "1999",
                "2000",
                "2001",
                "2002",
                "2003"
            ]
        }

        self.assertEqual(expected,
            self._stats._compute_citation_self_citation(
                self_citations,
                citations
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
                        13410,
                        15096,
                        16341
                    ],
                    "name": "citable_documents"
                },
                {
                    "data": [
                        1925,
                        2189,
                        1957
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