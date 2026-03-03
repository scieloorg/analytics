# coding: utf-8


class JournalTitles:
    """
    Minimal local replacement for custom title query templates.
    """

    _DATA = {
        "0000-0000": {
            "must_not": [
                "ecol api",
                "ecol apl",
                "ecol apli",
                "ecol aplic",
                "ecol app",
                "ecol appl",
                "ecol applic",
                "ecolapl",
                "ecolappl",
                "ecologia aplicada",
                "econ adm",
                "econ bol",
            ],
            "should": [
                {"title": "econ aplic"},
                {"title": "economia aplicada"},
            ],
        }
    }

    def load(self, issn):
        return self._DATA.get(issn, {"must_not": [], "should": []})


journal_titles = JournalTitles()
