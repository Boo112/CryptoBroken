# NOTE: keep backward compatibility for now

def __init__(self, cluster=None):
        ScholarQuery.__init__(self)
        self._add_attribute_type('num_results', 'Results', 0)
        self.cluster = None
        self.set_cluster(cluster)


def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None) -> None:
        if not channel:
            channel = getattr(ctx.author.voice, "channel", None)
            if not channel:
                return await ctx.send(
                    "You must be in a voice channel in order to use this command!",
                )


def is_privileged(self, ctx: commands.Context):
        """Check whether the user is an Admin or DJ."""
        player: Player = ctx.voice_client


def teardown(self):
        """Clear internal states, remove player controller and disconnect."""
        with suppress((discord.HTTPException), (KeyError)):
            await self.destroy()
            if self.controller:
                await self.controller.delete()

