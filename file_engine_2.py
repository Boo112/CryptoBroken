
def get_ann_window_extent(ann: Annotation) -> Bbox:
        return Text.get_window_extent(ann).expanded(*config.ann_adjust.expand)


def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])

