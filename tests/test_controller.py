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
               "took": 28423,
               "timed_out": False,
               "_shards": {
                  "total": 5,
                  "successful": 5,
                  "failed": 0
               },
               "hits": {
                  "total": 19297,
                  "max_score": 0,
                  "hits": []
               },
               "aggregations": {
                  "publication_year": {
                     "doc_count_error_upper_bound": 0,
                     "sum_other_doc_count": 0,
                     "buckets": [
                        {
                           "key": "2011",
                           "doc_count": 2820,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2007",
                                    "doc_count": 321
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 272
                                 },
                                 {
                                    "key": "2009",
                                    "doc_count": 272
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 233
                                 },
                                 {
                                    "key": "2008",
                                    "doc_count": 233
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 205
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 184
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 170
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 160
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 149
                                 },
                                 {
                                    "key": "2010",
                                    "doc_count": 91
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 85
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 58
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 54
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 38
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 36
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 31
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "2011",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2010",
                           "doc_count": 2633,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2007",
                                    "doc_count": 280
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 269
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 243
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 209
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 206
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 188
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 175
                                 },
                                 {
                                    "key": "2008",
                                    "doc_count": 169
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 154
                                 },
                                 {
                                    "key": "2009",
                                    "doc_count": 111
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 94
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 74
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 62
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 53
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 39
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 36
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 28
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "2010",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1967",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2008",
                           "doc_count": 2396,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2005",
                                    "doc_count": 239
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 232
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 225
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 219
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 213
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 187
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 170
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 141
                                 },
                                 {
                                    "key": "2007",
                                    "doc_count": 103
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 88
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 82
                                 },
                                 {
                                    "key": "2008",
                                    "doc_count": 67
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 59
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 48
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 36
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 35
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 33
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 31
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 26
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1900",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1966",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2009",
                           "doc_count": 2348,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2005",
                                    "doc_count": 237
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 234
                                 },
                                 {
                                    "key": "2007",
                                    "doc_count": 228
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 211
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 202
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 177
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 175
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 141
                                 },
                                 {
                                    "key": "2008",
                                    "doc_count": 112
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 92
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 72
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 63
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 44
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 43
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 39
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 36
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 28
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "2009",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1947",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1948",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1967",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "2010",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2007",
                           "doc_count": 1753,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 207
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 179
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 171
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 161
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 142
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 139
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 93
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 93
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 85
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 64
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 58
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 45
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 42
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 38
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 33
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 28
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "2007",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1000",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2006",
                           "doc_count": 1334,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 166
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 148
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 142
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 116
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 110
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 105
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 76
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 75
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 58
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 48
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 42
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2005",
                           "doc_count": 1103,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 150
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 130
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 119
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 93
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 88
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 66
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 65
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 55
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 53
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 42
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 40
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1954",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2004",
                           "doc_count": 921,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 141
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 107
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 90
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 88
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 68
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 56
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 47
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 40
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 37
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 17
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2003",
                           "doc_count": 679,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 135
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 77
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 61
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 47
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 44
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 31
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 17
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2002",
                           "doc_count": 509,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2000",
                                    "doc_count": 80
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 48
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 40
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 39
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 37
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1977",
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
                                    "key": "1974",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2001",
                           "doc_count": 438,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1997",
                                    "doc_count": 47
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 35
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 29
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2012",
                           "doc_count": 435,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "2008",
                                    "doc_count": 51
                                 },
                                 {
                                    "key": "2007",
                                    "doc_count": 45
                                 },
                                 {
                                    "key": "2005",
                                    "doc_count": 43
                                 },
                                 {
                                    "key": "2002",
                                    "doc_count": 38
                                 },
                                 {
                                    "key": "2009",
                                    "doc_count": 37
                                 },
                                 {
                                    "key": "2006",
                                    "doc_count": 34
                                 },
                                 {
                                    "key": "2004",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "2010",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "2003",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "2001",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "2011",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "2012",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "2000",
                           "doc_count": 405,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1993",
                                    "doc_count": 40
                                 },
                                 {
                                    "key": "2000",
                                    "doc_count": 35
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 32
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 30
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 26
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 20
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1999",
                           "doc_count": 279,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1993",
                                    "doc_count": 36
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 25
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 23
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 17
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1999",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1967",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1998",
                           "doc_count": 271,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1993",
                                    "doc_count": 34
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 27
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1998",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1997",
                           "doc_count": 266,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1991",
                                    "doc_count": 31
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 28
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 22
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 18
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 17
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 16
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1997",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1967",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1996",
                           "doc_count": 207,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1993",
                                    "doc_count": 31
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 17
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1967",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1995",
                           "doc_count": 168,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1993",
                                    "doc_count": 24
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 21
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 15
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1995",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1996",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1993",
                           "doc_count": 150,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1991",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 13
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 9
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1968",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1977",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1970",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1994",
                           "doc_count": 139,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1990",
                                    "doc_count": 19
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1993",
                                    "doc_count": 14
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 12
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 11
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 10
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 8
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1982",
                                    "doc_count": 6
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1992",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1972",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1974",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1975",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1994",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1969",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1979",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1992",
                           "doc_count": 31,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1987",
                                    "doc_count": 7
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 5
                                 },
                                 {
                                    "key": "1984",
                                    "doc_count": 4
                                 },
                                 {
                                    "key": "1989",
                                    "doc_count": 3
                                 },
                                 {
                                    "key": "1981",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1971",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1976",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1978",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1983",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1985",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1986",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1991",
                           "doc_count": 6,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1989",
                                    "doc_count": 2
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1987",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1990",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1991",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1987",
                           "doc_count": 2,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1973",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1980",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1990",
                           "doc_count": 2,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1986",
                                    "doc_count": 1
                                 },
                                 {
                                    "key": "1988",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1988",
                           "doc_count": 1,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1985",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        },
                        {
                           "key": "1989",
                           "doc_count": 1,
                           "reference_publication_year": {
                              "doc_count_error_upper_bound": 0,
                              "sum_other_doc_count": 0,
                              "buckets": [
                                 {
                                    "key": "1987",
                                    "doc_count": 1
                                 }
                              ]
                           }
                        }
                     ]
                  }
               }
            }

        citable_docs = {
            "series": [
                {
                    "data": [
                        19,
                        13,
                        25,
                        22,
                        24,
                        40,
                        40,
                        39,
                        47,
                        32,
                        52,
                        50,
                        39,
                        44,
                        60,
                        27,
                        31,
                        41,
                        48,
                        35,
                        43,
                        42,
                        53,
                        57,
                        53,
                        57,
                        52,
                        54,
                        53,
                        69,
                        83,
                        78,
                        66,
                        103,
                        80,
                        110,
                        104,
                        131,
                        141,
                        176,
                        173,
                        178,
                        165,
                        136,
                        144,
                        139,
                        153,
                        101,
                        75
                    ],
                    "name": "citable_documents"
                },
                {
                    "data": [
                        5,
                        4,
                        3,
                        5,
                        8,
                        8,
                        3,
                        10,
                        13,
                        14,
                        5,
                        6,
                        9,
                        12,
                        10,
                        12,
                        26,
                        25,
                        16,
                        33,
                        23,
                        39,
                        27,
                        24,
                        25,
                        14,
                        20,
                        21,
                        24,
                        15,
                        13,
                        10,
                        22,
                        21,
                        10,
                        23,
                        20,
                        23,
                        6,
                        37,
                        15,
                        9,
                        18,
                        16,
                        10,
                        14,
                        25,
                        9,
                        10
                    ],
                    "name": "not_citable_documents"
                }
            ],
            "categories": [
                "1967",
                "1968",
                "1969",
                "1970",
                "1971",
                "1972",
                "1973",
                "1974",
                "1975",
                "1976",
                "1977",
                "1978",
                "1979",
                "1980",
                "1981",
                "1982",
                "1983",
                "1984",
                "1985",
                "1986",
                "1987",
                "1988",
                "1989",
                "1990",
                "1991",
                "1992",
                "1993",
                "1994",
                "1995",
                "1996",
                "1997",
                "1998",
                "1999",
                "2000",
                "2001",
                "2002",
                "2003",
                "2004",
                "2005",
                "2006",
                "2007",
                "2008",
                "2009",
                "2010",
                "2011",
                "2012",
                "2013",
                "2014",
                "2015"
            ]
        }
        result = self._stats._compute_impact_factor(pub_citing_years, citable_docs)

        expected = {'2003': {'fi2': 0.4, 'fi3': 0.7201365187713311, 'fi1': 0.2909090909090909, 'fi4': 0.7186629526462396, 'citable_docs3': 103.0, 'citable_docs2': 80.0, 'citable_docs1': 110.0, 'citable_docs': 104, 'citable_docs4': 66.0, 'citing_count4': 47.0, 'citing_count1': 32.0, 'citing_count3': 135.0, 'citing_count2': 44.0}, '1997': {'fi2': 0.2540983606557377, 'fi3': 0.2727272727272727, 'fi1': 0.18840579710144928, 'fi4': 0.3333333333333333, 'citable_docs3': 54.0, 'citable_docs2': 53.0, 'citable_docs1': 69.0, 'citable_docs': 83, 'citable_docs4': 52.0, 'citing_count4': 28.0, 'citing_count1': 13.0, 'citing_count3': 17.0, 'citing_count2': 18.0}, '1986': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 31.0, 'citable_docs2': 41.0, 'citable_docs1': 48.0, 'citable_docs': 35, 'citable_docs4': 27.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1987': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 41.0, 'citable_docs2': 48.0, 'citable_docs1': 35.0, 'citable_docs': 43, 'citable_docs4': 31.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1984': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 60.0, 'citable_docs2': 27.0, 'citable_docs1': 31.0, 'citable_docs': 41, 'citable_docs4': 44.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1985': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 27.0, 'citable_docs2': 31.0, 'citable_docs1': 41.0, 'citable_docs': 48, 'citable_docs4': 60.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1968': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 0.0, 'citable_docs2': 0.0, 'citable_docs1': 19.0, 'citable_docs': 13, 'citable_docs4': 0.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1969': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 0.0, 'citable_docs2': 19.0, 'citable_docs1': 13.0, 'citable_docs': 25, 'citable_docs4': 0.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1980': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 52.0, 'citable_docs2': 50.0, 'citable_docs1': 39.0, 'citable_docs': 44, 'citable_docs4': 32.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1981': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 50.0, 'citable_docs2': 39.0, 'citable_docs1': 44.0, 'citable_docs': 60, 'citable_docs4': 52.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1967': {'fi2': 0, 'fi3': 0, 'fi1': 0, 'fi4': 0, 'citable_docs3': 0.0, 'citable_docs2': 0.0, 'citable_docs1': 0.0, 'citable_docs': 19, 'citable_docs4': 0.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1988': {'fi2': 0.0, 'fi3': 0.007936507936507936, 'fi1': 0.0, 'fi4': 0.005988023952095809, 'citable_docs3': 48.0, 'citable_docs2': 35.0, 'citable_docs1': 43.0, 'citable_docs': 42, 'citable_docs4': 41.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 1.0, 'citing_count2': 0.0}, '1989': {'fi2': 0.011764705882352941, 'fi3': 0.008333333333333333, 'fi1': 0.0, 'fi4': 0.005952380952380952, 'citable_docs3': 35.0, 'citable_docs2': 43.0, 'citable_docs1': 42.0, 'citable_docs': 53, 'citable_docs4': 48.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 1.0}, '1996': {'fi2': 0.21495327102803738, 'fi3': 0.33962264150943394, 'fi1': 0.2830188679245283, 'fi4': 0.30092592592592593, 'citable_docs3': 52.0, 'citable_docs2': 54.0, 'citable_docs1': 53.0, 'citable_docs': 69, 'citable_docs4': 57.0, 'citing_count4': 11.0, 'citing_count1': 15.0, 'citing_count3': 31.0, 'citing_count2': 8.0}, '2014': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 144.0, 'citable_docs2': 139.0, 'citable_docs1': 153.0, 'citable_docs': 101, 'citable_docs4': 136.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '2011': {'fi2': 1.2059800664451827, 'fi3': 1.244258872651357, 'fi1': 0.6691176470588235, 'fi4': 1.406441717791411, 'citable_docs3': 178.0, 'citable_docs2': 165.0, 'citable_docs1': 136.0, 'citable_docs': 144, 'citable_docs4': 173.0, 'citing_count4': 321.0, 'citing_count1': 91.0, 'citing_count3': 233.0, 'citing_count2': 272.0}, '2010': {'fi2': 0.8163265306122449, 'fi3': 1.0852713178294573, 'fi1': 0.6727272727272727, 'fi4': 1.1979768786127167, 'citable_docs3': 173.0, 'citable_docs2': 178.0, 'citable_docs1': 165.0, 'citable_docs': 136, 'citable_docs4': 176.0, 'citing_count4': 269.0, 'citing_count1': 111.0, 'citing_count3': 280.0, 'citing_count2': 169.0}, '2013': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 136.0, 'citable_docs2': 144.0, 'citable_docs1': 139.0, 'citable_docs': 153, 'citable_docs4': 165.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '2012': {'fi2': 0.09285714285714286, 'fi3': 0.14157303370786517, 'fi1': 0.05555555555555555, 'fi4': 0.18298555377207062, 'citable_docs3': 165.0, 'citable_docs2': 136.0, 'citable_docs1': 144.0, 'citable_docs': 139, 'citable_docs4': 178.0, 'citing_count4': 51.0, 'citing_count1': 8.0, 'citing_count3': 37.0, 'citing_count2': 18.0}, '2005': {'fi2': 0.6212765957446809, 'fi3': 0.7681159420289855, 'fi1': 0.40458015267175573, 'fi4': 0.9294117647058824, 'citable_docs3': 110.0, 'citable_docs2': 104.0, 'citable_docs1': 131.0, 'citable_docs': 141, 'citable_docs4': 80.0, 'citing_count4': 130.0, 'citing_count1': 53.0, 'citing_count3': 119.0, 'citing_count2': 93.0}, '2015': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 139.0, 'citable_docs2': 153.0, 'citable_docs1': 101.0, 'citable_docs': 75, 'citable_docs4': 144.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1982': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 39.0, 'citable_docs2': 44.0, 'citable_docs1': 60.0, 'citable_docs': 27, 'citable_docs4': 50.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1983': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 44.0, 'citable_docs2': 60.0, 'citable_docs1': 27.0, 'citable_docs': 31, 'citable_docs4': 39.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1991': {'fi2': 0.02727272727272727, 'fi3': 0.019736842105263157, 'fi1': 0.017543859649122806, 'fi4': 0.020512820512820513, 'citable_docs3': 42.0, 'citable_docs2': 53.0, 'citable_docs1': 57.0, 'citable_docs': 53, 'citable_docs4': 43.0, 'citing_count4': 1.0, 'citing_count1': 1.0, 'citing_count3': 0.0, 'citing_count2': 2.0}, '1990': {'fi2': 0.010526315789473684, 'fi3': 0.007246376811594203, 'fi1': 0.0, 'fi4': 0.011560693641618497, 'citable_docs3': 43.0, 'citable_docs2': 42.0, 'citable_docs1': 53.0, 'citable_docs': 57, 'citable_docs4': 35.0, 'citing_count4': 1.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 1.0}, '1993': {'fi2': 0.2, 'fi3': 0.20359281437125748, 'fi1': 0.14035087719298245, 'fi4': 0.20454545454545456, 'citable_docs3': 57.0, 'citable_docs2': 53.0, 'citable_docs1': 57.0, 'citable_docs': 52, 'citable_docs4': 53.0, 'citing_count4': 11.0, 'citing_count1': 8.0, 'citing_count3': 12.0, 'citing_count2': 14.0}, '1992': {'fi2': 0.03636363636363636, 'fi3': 0.04294478527607362, 'fi1': 0.03773584905660377, 'fi4': 0.05853658536585366, 'citable_docs3': 53.0, 'citable_docs2': 57.0, 'citable_docs1': 53.0, 'citable_docs': 57, 'citable_docs4': 42.0, 'citing_count4': 5.0, 'citing_count1': 2.0, 'citing_count3': 3.0, 'citing_count2': 2.0}, '1995': {'fi2': 0.3490566037735849, 'fi3': 0.27607361963190186, 'fi1': 0.24074074074074073, 'fi4': 0.2638888888888889, 'citable_docs3': 57.0, 'citable_docs2': 52.0, 'citable_docs1': 54.0, 'citable_docs': 53, 'citable_docs4': 53.0, 'citing_count4': 12.0, 'citing_count1': 13.0, 'citing_count3': 8.0, 'citing_count2': 24.0}, '1994': {'fi2': 0.1651376146788991, 'fi3': 0.17901234567901234, 'fi1': 0.2692307692307692, 'fi4': 0.2191780821917808, 'citable_docs3': 53.0, 'citable_docs2': 57.0, 'citable_docs1': 52.0, 'citable_docs': 54, 'citable_docs4': 57.0, 'citing_count4': 19.0, 'citing_count1': 14.0, 'citing_count3': 11.0, 'citing_count2': 4.0}, '1979': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 32.0, 'citable_docs2': 52.0, 'citable_docs1': 50.0, 'citable_docs': 39, 'citable_docs4': 47.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1978': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 47.0, 'citable_docs2': 32.0, 'citable_docs1': 52.0, 'citable_docs': 50, 'citable_docs4': 39.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1977': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 39.0, 'citable_docs2': 47.0, 'citable_docs1': 32.0, 'citable_docs': 52, 'citable_docs4': 40.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1976': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 40.0, 'citable_docs2': 39.0, 'citable_docs1': 47.0, 'citable_docs': 32, 'citable_docs4': 40.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1975': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 40.0, 'citable_docs2': 40.0, 'citable_docs1': 39.0, 'citable_docs': 47, 'citable_docs4': 24.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1974': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 24.0, 'citable_docs2': 40.0, 'citable_docs1': 40.0, 'citable_docs': 39, 'citable_docs4': 22.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1973': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 22.0, 'citable_docs2': 24.0, 'citable_docs1': 40.0, 'citable_docs': 40, 'citable_docs4': 25.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1972': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 25.0, 'citable_docs2': 22.0, 'citable_docs1': 24.0, 'citable_docs': 40, 'citable_docs4': 13.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1971': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 13.0, 'citable_docs2': 25.0, 'citable_docs1': 22.0, 'citable_docs': 24, 'citable_docs4': 19.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '1970': {'fi2': 0.0, 'fi3': 0.0, 'fi1': 0.0, 'fi4': 0.0, 'citable_docs3': 19.0, 'citable_docs2': 13.0, 'citable_docs1': 25.0, 'citable_docs': 22, 'citable_docs4': 0.0, 'citing_count4': 0.0, 'citing_count1': 0.0, 'citing_count3': 0.0, 'citing_count2': 0.0}, '2002': {'fi2': 0.5956284153005464, 'fi3': 0.5943775100401606, 'fi1': 0.3625, 'fi4': 0.5749235474006116, 'citable_docs3': 66.0, 'citable_docs2': 103.0, 'citable_docs1': 80.0, 'citable_docs': 110, 'citable_docs4': 78.0, 'citing_count4': 40.0, 'citing_count1': 29.0, 'citing_count3': 39.0, 'citing_count2': 80.0}, '1999': {'fi2': 0.22981366459627328, 'fi3': 0.2565217391304348, 'fi1': 0.16666666666666666, 'fi4': 0.2968197879858657, 'citable_docs3': 69.0, 'citable_docs2': 83.0, 'citable_docs1': 78.0, 'citable_docs': 66, 'citable_docs4': 53.0, 'citing_count4': 25.0, 'citing_count1': 13.0, 'citing_count3': 22.0, 'citing_count2': 24.0}, '2000': {'fi2': 0.2638888888888889, 'fi3': 0.30837004405286345, 'fi1': 0.18181818181818182, 'fi4': 0.33783783783783783, 'citable_docs3': 83.0, 'citable_docs2': 78.0, 'citable_docs1': 66.0, 'citable_docs': 103, 'citable_docs4': 69.0, 'citing_count4': 30.0, 'citing_count1': 12.0, 'citing_count3': 32.0, 'citing_count2': 26.0}, '2001': {'fi2': 0.3076923076923077, 'fi3': 0.3522267206477733, 'fi1': 0.24271844660194175, 'fi4': 0.40606060606060607, 'citable_docs3': 78.0, 'citable_docs2': 66.0, 'citable_docs1': 103.0, 'citable_docs': 80, 'citable_docs4': 83.0, 'citing_count4': 47.0, 'citing_count1': 25.0, 'citing_count3': 35.0, 'citing_count2': 27.0}, '2006': {'fi2': 0.7022058823529411, 'fi3': 0.8856382978723404, 'fi1': 0.5319148936170213, 'fi4': 0.9897119341563786, 'citable_docs3': 104.0, 'citable_docs2': 131.0, 'citable_docs1': 141.0, 'citable_docs': 176, 'citable_docs4': 110.0, 'citing_count4': 148.0, 'citing_count1': 75.0, 'citing_count3': 142.0, 'citing_count2': 116.0}, '2007': {'fi2': 0.8012618296529969, 'fi3': 0.9486607142857143, 'fi1': 0.5284090909090909, 'fi4': 1.0217391304347827, 'citable_docs3': 131.0, 'citable_docs2': 141.0, 'citable_docs1': 176.0, 'citable_docs': 173, 'citable_docs4': 104.0, 'citing_count4': 139.0, 'citing_count1': 93.0, 'citing_count3': 171.0, 'citing_count2': 161.0}, '2004': {'fi2': 0.5841121495327103, 'fi3': 0.7312925170068028, 'fi1': 0.3557692307692308, 'fi4': 0.8967254408060453, 'citable_docs3': 80.0, 'citable_docs2': 110.0, 'citable_docs1': 104.0, 'citable_docs': 131, 'citable_docs4': 103.0, 'citing_count4': 141.0, 'citing_count1': 37.0, 'citing_count3': 90.0, 'citing_count2': 88.0}, '1998': {'fi2': 0.26973684210526316, 'fi3': 0.2682926829268293, 'fi1': 0.1686746987951807, 'fi4': 0.3166023166023166, 'citable_docs3': 53.0, 'citable_docs2': 69.0, 'citable_docs1': 83.0, 'citable_docs': 78, 'citable_docs4': 54.0, 'citing_count4': 27.0, 'citing_count1': 14.0, 'citing_count3': 14.0, 'citing_count2': 27.0}, '2008': {'fi2': 0.9054441260744985, 'fi3': 1.1326530612244898, 'fi1': 0.5953757225433526, 'fi4': 1.2673107890499196, 'citable_docs3': 141.0, 'citable_docs2': 176.0, 'citable_docs1': 173.0, 'citable_docs': 178, 'citable_docs4': 131.0, 'citing_count4': 232.0, 'citing_count1': 103.0, 'citing_count3': 239.0, 'citing_count2': 213.0}, '2009': {'fi2': 0.9686609686609686, 'fi3': 1.0891840607210626, 'fi1': 0.6292134831460674, 'fi4': 1.214071856287425, 'citable_docs3': 176.0, 'citable_docs2': 173.0, 'citable_docs1': 178.0, 'citable_docs': 165, 'citable_docs4': 141.0, 'citing_count4': 237.0, 'citing_count1': 112.0, 'citing_count3': 234.0, 'citing_count2': 228.0}}

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