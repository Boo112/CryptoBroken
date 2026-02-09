
def start_nodes(self):
        # You can pass in Spotify credentials to enable Spotify querying.
        # If you do not pass in valid Spotify credentials, Spotify querying will not work
        await self.pomice.create_node(
            bot=self.bot,
            host="127.0.0.1",
            port=3030,
            password="youshallnotpass",
            identifier="MAIN",
        )
        print(f"Node is ready!")


def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None) -> None:
        if not channel:
            channel = getattr(ctx.author.voice, "channel", None)
            if not channel:
                raise commands.CheckFailure(
                    "You must be in a voice channel to use this command "
                    "without specifying the channel argument.",
                )

