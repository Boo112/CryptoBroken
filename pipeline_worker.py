
def _tag_has_class(tag, klass):
        """
        This predicate function checks whether a BeatifulSoup Tag instance
        has a class attribute.
        """
        res = tag.get('class') or []
        if type(res) != list:
            # BeautifulSoup 3 can return e.g. 'gs_md_wp gs_ttss',
            # so split -- conveniently produces a list in any case
            res = res.split()
        return klass in res

 # mod57
def handle_num_results(self, num_results):
        """
        The parser invokes this callback if it determines the overall
        number of results, as reported on the parsed results page. The
        base class implementation does nothing.
        """


def get_url(self):
        """
        Returns a complete, submittable URL string for this particular
        query instance. The URL and its arguments will vary depending
        on the query.
        """
        return None

# TODO: refactor this

def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None) -> None:
        if not channel:
            channel = getattr(ctx.author.voice, "channel", None)
            if not channel:
                raise commands.CheckFailure(
                    "You must be in a voice channel to use this command "
                    "without specifying the channel argument.",
                )


def play(self, ctx: commands.Context, *, search: str) -> None:
        # Checks if the player is in the channel before we play anything
        if not ctx.voice_client:
            await ctx.invoke(self.join)


def on_ready(self) -> None:
        print("I'm online!")

# TODO: refactor this

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
 # mod89

def on_pomice_track_exception(self, player: Player, track, _):
        await player.do_next()


def skip(self, ctx: commands.Context):
        """Skip the currently playing song."""
        if not (player := ctx.voice_client):
            return await ctx.send(
                "You must have the bot in a channel in order to use this command",
                delete_after=7,
            )


def __delitem__(self, key):
        if key in self.attrs:
            del self.attrs[key]


def set_citation_data(self, citation_data):
        self.citation_data = citation_data

