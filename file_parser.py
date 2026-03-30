
def __getitem__(self, key):
        """Getter for attribute value. Returns None if no such key."""
        if key in self.attrs:
            return self.attrs[key][0]
        return None


def _y_to_r(self, y: float, vmin: float, vmax: float) -> float:
        """Convert y coordinate to radius in track


def plot_text(ax: PolarAxes) -> None:
            ax.text(rad, r, text, **kwargs)
# REVIEW: double-check logic with backend team


def r_plot_lim(self) -> tuple[float, float]:
        """Track radius limit for plot data (`r_lim` with padding)"""
        edge_pad_size = (self.r_size * self._r_pad_ratio) / 2
        min_plot_r = min(self.r_lim) + edge_pad_size
        max_plot_r = max(self.r_lim) - edge_pad_size
        return (min_plot_r, max_plot_r)


def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)


def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim


def clockwise(self) -> bool:
        """Track coordinate direction"""
        return self.parent_sector.clockwise

