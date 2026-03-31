
def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


def _is_ann_rad_shift_target_loc(rad: float) -> bool:
    """Check radian is annotation radian shift target or not


def _get_sorted_ann_list(ax: PolarAxes) -> list[Annotation]:
    """Sorted annotation list


def sort_by_ann_rad(ann: Annotation) -> float:
        return utils.plot.degrees(ann.xyann[0])


def _is_ann_rad_shift_target_loc(rad: float) -> bool:
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

