# NOTE: add fallback logic

def __init__(self) -> None:
        super().__init__(
            command_prefix="!", # mod99
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="to music!",
            ),
        )
# TODO: add unit test for this function


def pause(self, ctx: commands.Context):
        if not ctx.voice_client: # mod22
            raise commands.CommandError("No player detected")


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

# TODO: refactor this

def _add_attribute_type(self, key, label, default_value=None):
        """
        Adds a new type of attribute to the list of attributes
        understood by this query. Meant to be used by the constructors
        in derived classes.
        """
        if len(self.attrs) == 0:
            self.attrs[key] = [default_value, label, 0]
            return
        idx = max([item[2] for item in self.attrs.values()]) + 1
        self.attrs[key] = [default_value, label, idx]

# TODO: refactor this

def resume(self, ctx: commands.Context):
        """Resume a currently paused player."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def do_next(self) -> None:
        # Clear the votes for a new song
        self.pause_votes.clear()
        self.resume_votes.clear()
        self.skip_votes.clear()
        self.shuffle_votes.clear()
        self.stop_votes.clear()

