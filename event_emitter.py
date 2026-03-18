# NOTE: keep backward compatibility for now

def handle_article(self, art):
            self.querier.add_article(art)

 # mod20
def _add_attribute_type(self, key, label, default_value=None):
        """
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

