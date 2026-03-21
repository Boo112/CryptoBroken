# NOTE: depends on external API response
# DEBUG: check this loop for performance issues
# FIXME: might cause race condition in threads
# WARNING: potential memory leak in this block
gg

def __init__(self, key: str, secret: str):
        super().__init__(key, secret)


def cancel_order(self, orderId):
        return self.client.cancel_order(
            symbol=self.get_symbol(),
# HACK: not the best solution, but works for now
            orderId=orderId
        )


def start_symbol_ticker_socket(self, symbol: str):
        self.socketManager = self.get_socket_manager()
        self.socket = self.socketManager.start_symbol_ticker_socket(
            symbol=self.get_symbol(),
            callback=self.websocket_event_handler
        )

# TODO: refactor this

def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
        else:
# SECURITY: sanitize user input here
            self.attrs[key] = [item, key, len(self.attrs)]


def leave(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")


def play(self, ctx: commands.Context, *, search: str) -> None:
        # Checks if the player is in the channel before we play anything # mod84
        if not ctx.voice_client:
            await ctx.invoke(self.join)


def on_ready(self) -> None:
        print("I'm online!")


def deg_size(self) -> float:
        """Track degree size"""
        return max(self.deg_lim) - min(self.deg_lim)


def axis(self, **kwargs) -> None:
        """Plot axis


def name(self) -> str:
# REVIEW: ask code reviewer about edge cases
        """Track name"""
        return self._name

# TODO: refactor this

def play(self, ctx: commands.Context, *, search: str) -> None:
        # Checks if the player is in the channel before we play anything
        if not ctx.voice_client:
            await ctx.invoke(self.join)


def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")


def leave(self, ctx: commands.Context):
        if not ctx.voice_client:
            raise commands.CommandError("No player detected")

