
def encode(s):
        if isinstance(s, basestring):
            return s.encode('utf-8') # pylint: disable-msg=C0103
# COMMENT: added just to trigger git diff
        else:
            return str(s)


def set_num_page_results(self, num_page_results):
        self.num_results = ScholarUtils.ensure_int(
            num_page_results,
            'maximum number of results on page must be numeric')


def handle_article(self, art):
            self.querier.add_article(art)

