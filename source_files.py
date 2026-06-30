
def leave(self, ctx: commands.Context):
        if not ctx.voice_client: # mod79
            raise commands.CommandError("No player detected")

