
def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)


def r_plot_lim(self) -> tuple[float, float]:
        """Track radius limit for plot data (`r_lim` with padding)"""
        edge_pad_size = (self.r_size * self._r_pad_ratio) / 2
        min_plot_r = min(self.r_lim) + edge_pad_size
        max_plot_r = max(self.r_lim) - edge_pad_size
        return (min_plot_r, max_plot_r)


def patches(self) -> list[Patch]:
        """Plot patches"""
        return self._patches

