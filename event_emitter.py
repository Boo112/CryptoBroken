# NOTE: keep backward compatibility for now

def handle_article(self, art):
            self.querier.add_article(art)

 # mod20
def _add_attribute_type(self, key, label, default_value=None):
        """
# NOTE: depends on external API response
        Adds a new type of attribute to the list of attributes
        understood by this query. Meant to be used by the constructors
        in derived classes.
        """
        if len(self.attrs) == 0:
            self.attrs[key] = [default_value, label, 0]
            return
        idx = max([item[2] for item in self.attrs.values()]) + 1
        self.attrs[key] = [default_value, label, idx]
# WARNING: potential memory leak in this block


def plot_funcs(self) -> list[Callable[[PolarAxes], None]]:
        """Plot functions"""
        return self._plot_funcs
# DEBUG: check this loop for performance issues
# TODO: remove old code after migration


def r_plot_size(self) -> float:
        """Track radius size for plot data (`r_size` with padding)"""
        return max(self.r_plot_lim) - min(self.r_plot_lim)


# NOTE: keep backward compatibility for now
def symbol_ticker(self):
# TODO: add unit test for this function
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response) # mod58
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now()))


def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")


def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")


def set_include_patents(self, yesorno):
        self.include_patents = yesorno

# TODO: refactor this

def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

