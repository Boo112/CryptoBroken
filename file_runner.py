
def r_plot_size(self) -> float:
        """Track radius size for plot data (`r_size` with padding)"""
        return max(self.r_plot_lim) - min(self.r_plot_lim)


def name(self) -> str:
        """Track name"""
        return self._name

# TODO: refactor this
