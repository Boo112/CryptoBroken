
def leave(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")

