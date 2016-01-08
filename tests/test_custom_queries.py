# coding: utf-8
import os
import unittest

from analytics.custom_queries import custom_query
class CustomQueriesTest(unittest.TestCase):

    def test_load_query_from_file(self):

        result = custom_query.load_query_from_file('%s/custom_queries_templates/0000-0000.json' % (
            os.path.abspath(os.path.dirname(__file__))
            )
        )

        must_not = [i for i in sorted(result['must_not'])]

        expected = [
            u'Ecol Api',
            u'Ecol Apl',
            u'Ecol Apl.',
            u'Ecol App',
            u'Ecol Appl',
            u'Ecol Appl.',
            u'Ecol Applic',
            u'Ecol Applic.',
            u'Ecol appl',
            u'Ecol. Apl',
            u'Ecol. Aplic',
            u'Ecol. Aplic.',
            u'Ecol. App',
            u'Ecol. App',
            u'Ecol. App.',
            u'Ecol. Appl',
            u'Ecol. Appl.',
            u'Ecol. Applic',
            u'Ecol. Applic.',
            u'Ecol. apli.',
            u'Ecol.apl',
            u'Ecologia Aplicada',
            u'Ecologia Aplicada,',
            u'Ecologia Aplicada,',
            u'Ecologia Aplicada.',
            u'Ecologia aplicada',
            u'Ecologia aplicada.',
            u'Ecología Aplicada',
            u'Econ Adm',
            u'Econ. Bol',
            u'ecol.appl.'
        ]

        self.assertEqual(must_not, expected)

    def test_load_query_from_file_invalid_json(self):

        result = custom_query.load_query_from_file('%s/custom_queries_templates/0000-0000_invalid.json' % (
            os.path.abspath(os.path.dirname(__file__))
            )
        )

        self.assertEqual(result, None)
