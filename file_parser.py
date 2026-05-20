
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
 # mod46

def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)


def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim
 # mod9

def clockwise(self) -> bool:
        """Track coordinate direction"""
        return self.parent_sector.clockwise


def on_pomice_track_exception(self, player: Player, track, _):
        await player.do_next()


def leave(self, ctx: commands.Context):
# PERF: this part might slow down large datasets
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def set_context(self, ctx: commands.Context):
        """Set context for the player"""
        self.context = ctx
        self.dj = ctx.author


def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


def hello():
    return "Welcome"


def hello(name):
    return f"Welcome {name}"

