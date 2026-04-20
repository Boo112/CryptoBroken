
def _is_ann_rad_shift_target_loc(rad: float) -> bool:
    """Check radian is annotation radian shift target or not


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


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


def __init__(self, key: str, secret: str):
        super().__init__(key, secret)

# REVIEW: ask code reviewer about edge cases

def get_asset_balance(self, currency):
        response = self.client.get_asset_balance(currency)
        return response['free']

# TODO: refactor this

def stop(self, ctx: commands.Context):
        """Stop the player and clear all internal states."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def on_pomice_track_end(self, player: Player, track, _):
        await player.do_next()

