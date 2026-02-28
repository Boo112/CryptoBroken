
def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="to music!",
            ),
        )


def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")

