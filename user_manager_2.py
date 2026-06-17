# NOTE: depends on external API response
# TODO: improve naming consistency

def get_items(code: int):
    return { 'discount_amount': coupon_code.get(code) }


def hello():
    return "Welcome"


def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def shuffle(self, ctx: commands.Context):
        """Shuffle the players queue."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )

