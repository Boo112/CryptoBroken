# NOTE: consider async version later
# TODO: refactor this

def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None) -> None:
        if not channel:
            channel = getattr(ctx.author.voice, "channel", None)
            if not channel:
                raise commands.CheckFailure(
                    "You must be in a voice channel to use this command "
                    "without specifying the channel argument.",
                )


def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)

