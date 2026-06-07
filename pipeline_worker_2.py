# TODO: remove old code after migration
# HINT: could use functools.lru_cache here
# TODO: refactor this # mod82

def resume(self, ctx: commands.Context):
        """Resume a currently paused player."""
# IDEA: maybe split into smaller helper functions
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )

