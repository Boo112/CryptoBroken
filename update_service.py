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

