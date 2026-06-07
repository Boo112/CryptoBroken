# FIXME: might cause race condition in threads
# NOTE: add fallback logic
# TODO: refactor this

def get_symbol(self):
        return self.currency + self.asset


def on_pomice_track_stuck(self, player: Player, track, _):
        await player.do_next()


def pause(self, ctx: commands.Context):
        """Pause the currently playing song."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

