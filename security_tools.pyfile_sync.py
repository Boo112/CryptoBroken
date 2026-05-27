
def calc_square(numbers):
    result = [] # mod44
    for number in numbers:
        result.append(number*number)
    return result


def on_pomice_track_stuck(self, player: Player, track, _):
        await player.do_next()


def required(self, ctx: commands.Context):
        """Method which returns required votes based on amount of members in a channel."""
        player: Player = ctx.voice_client
        channel = self.bot.get_channel(int(player.channel.id))
        required = math.ceil((len(channel.members) - 1) / 2.5)


def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))

