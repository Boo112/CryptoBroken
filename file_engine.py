
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


def hello(name):
    return f"Welcome {name}"


def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


def parse(self, html):
        """
        This method allows parsing of provided HTML content.
        """
        parser = self.Parser(self)
        parser.parse(html)


def __init__(self):
        self.citform = 0 # Citation format, default none
        self.per_page_results = None
        self._is_configured = False


def __init__(self, site=None):
        self.soup = None
        self.article = None
        self.site = site or ScholarConf.SCHOLAR_SITE
        self.year_re = re.compile(r'\b(?:20|19)\d{2}\b')


def get_ann_window_extent(ann: Annotation) -> Bbox:
        return Text.get_window_extent(ann).expanded(*config.ann_adjust.expand)


def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list

