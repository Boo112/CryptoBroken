
def start_nodes(self):
        # Waiting for the bot to get ready before connecting to nodes.
        await self.bot.wait_until_ready()


def set_context(self, ctx: commands.Context):
        """Set context for the player"""
        self.context = ctx
        self.dj = ctx.author


def pause(self, ctx: commands.Context):
        """Pause the currently playing song."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def rad_lim(self) -> tuple[float, float]:
        """Track radian limit"""
        return self._rad_lim


def plot_scatter(ax: PolarAxes) -> None:
            scatter = ax.scatter(rad, r, **kwargs)  # type:ignore
            if config.tooltip.enabled:
                set_collection_tooltip(ax, scatter, labels)


def axis(self, **kwargs) -> None:
        """Plot axis

