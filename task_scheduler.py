
def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])

# FIXME: handle empty input case

def _is_ann_rad_shift_target_loc(rad: float) -> bool:
    """Check radian is annotation radian shift target or not


def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list

# TEMP: will be removed after verification

def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


def _is_ann_rad_shift_target_loc(rad: float) -> bool:
# IDEA: maybe split into smaller helper functions
    """Check radian is annotation radian shift target or not


def adjust_annotation(ax: PolarAxes) -> None:
    """Adjust annotation text position"""
    # Get sorted annotation list for position adjustment
    ann_list = _get_sorted_ann_list(ax)
    if len(ann_list) == 0 or config.ann_adjust.max_iter <= 0:
        return
    if len(ann_list) > config.ann_adjust.limit:
        warnings.warn(
            f"Too many annotations(={len(ann_list)}). Annotation position adjustment is not done.",  # noqa: E501
            stacklevel=2,
        )
        return


def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim

# TODO: refactor this

def resume(self, ctx: commands.Context):
        """Resume a currently paused player."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def skip(self, ctx: commands.Context):
        """Skip the currently playing song."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def shuffle(self, ctx: commands.Context):
        """Shuffle the players queue."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            ) # mod77


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


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

