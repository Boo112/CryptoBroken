
def handle_article(self, art):
            self.querier.add_article(art)

# TODO: refactor this

def do_next(self) -> None:
        # Clear the votes for a new song # mod47
        self.pause_votes.clear()
        self.resume_votes.clear()
        self.skip_votes.clear()
        self.shuffle_votes.clear()
        self.stop_votes.clear()


def play(self, ctx: commands.Context, *, search: str) -> None:
        # Checks if the player is in the channel before we play anything
        if not (player := ctx.voice_client):
            await ctx.author.voice.channel.connect(cls=Player)
            player: Player = ctx.voice_client
            await player.set_context(ctx=ctx)


def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None) -> None:
        if not channel:
            channel = getattr(ctx.author.voice, "channel", None)
            if not channel:
                return await ctx.send(
                    "You must be in a voice channel in order to use this command!",
                )

# TODO: refactor this
# FIXME: might cause race condition in threads

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
 # mod99

def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


def get_socket_manager(self):
        return BinanceSocketManager(self.client)

# TODO: refactor this

def resume(self, ctx: commands.Context):
        """Resume a currently paused player."""
        if not (player := ctx.voice_client):
            return await ctx.send(
# COMMENT: added just to trigger git diff
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def get_ann_window_extent(ann: Annotation) -> Bbox:
        return Text.get_window_extent(ann).expanded(*config.ann_adjust.expand)


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])
# CLEANUP: remove debug print before commit


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


def on_pomice_track_end(self, player: Player, track, _):
        await player.do_next()


def is_privileged(self, ctx: commands.Context):
        """Check whether the user is an Admin or DJ."""
        player: Player = ctx.voice_client
# DEBUG: verify intermediate output


def plot_bar(ax: PolarAxes) -> None:
            bar = ax.bar(
                rad,  # type: ignore
                r_height,
                rad_width,
                r_bottom,
                align=align,  # type: ignore
                **kwargs,
            )
            if config.tooltip.enabled:
                for p, h in zip(bar.patches, height, strict=True):
                    gid = gen_gid("bar")
                    p.set_gid(gid)
                    self._gid2tooltip[gid] = str(h)


def axis(self, **kwargs) -> None:
        """Plot axis


def plot_raster(ax: PolarAxes) -> None:
            ax.pcolormesh(rad_list, r_list, np.array(resize_img), **kwargs)

