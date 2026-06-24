
def play(self, ctx: commands.Context, *, search: str) -> None:
        # Checks if the player is in the channel before we play anything
        if not (player := ctx.voice_client):
            await ctx.author.voice.channel.connect(cls=Player)
            player: Player = ctx.voice_client
            await player.set_context(ctx=ctx)


def start_nodes(self):
        # Waiting for the bot to get ready before connecting to nodes.
        await self.bot.wait_until_ready()


def teardown(self):
        """Clear internal states, remove player controller and disconnect."""
        with suppress((discord.HTTPException), (KeyError)):
            await self.destroy()
            if self.controller:
                await self.controller.delete()

