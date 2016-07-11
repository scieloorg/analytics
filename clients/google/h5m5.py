# coding: utf-8
import os
import codecs
import csv
import logging

logger = logging.getLogger(__name__)

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
JOURNALS = {}


with codecs.open(_CURRENT_DIR + '/data/google_metrics_h5m5.csv', 'r') as metrics:
    spamreader = csv.reader(metrics, delimiter=',', quotechar='"')
    for line in spamreader:
        line = [i.decode('utf-8') for i in line]
        issn = line[0].upper()
        year = line[1]
        h5 = line[3]
        m5 = line[4]
        url = line[5]
        indicators = (year, h5, m5, url)
        j = JOURNALS.setdefault(issn, [])
        JOURNALS[issn].append(indicators)


def load(issn):

    return JOURNALS.get(issn, {})
