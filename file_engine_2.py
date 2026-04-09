
def get_ann_window_extent(ann: Annotation) -> Bbox:
        return Text.get_window_extent(ann).expanded(*config.ann_adjust.expand)


def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


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

