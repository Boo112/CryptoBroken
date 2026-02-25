
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

# TODO: refactor this

def cancel_order(self, orderId):
        return self.client.cancel_order(
            symbol=self.get_symbol(),
            orderId=orderId
        )


def start_symbol_ticker_socket(self, symbol: str):
        self.socketManager = self.get_socket_manager()
        self.socket = self.socketManager.start_symbol_ticker_socket(
            symbol=self.get_symbol(),
            callback=self.websocket_event_handler
        )


def __str__(self) -> str:
        min_deg_lim, max_deg_lim = min(self.deg_lim), max(self.deg_lim)
        min_r_lim, max_r_lim = min(self.r_lim), max(self.r_lim)
        return textwrap.dedent(
            f"""
            # Track = '{self.name}' (Parent Sector = '{self.parent_sector.name}')
            # Size = {self.size} ({self.start} - {self.end})
            # Degree Size = {self.deg_size:.2f} ({min_deg_lim:.2f} - {max_deg_lim:.2f})
            # Radius Size = {self.r_size:.2f} ({min_r_lim:.2f} - {max_r_lim:.2f})
            """
        )[1:]


def plot_text(ax: PolarAxes) -> None:
            ax.text(rad, r, text, **kwargs)

