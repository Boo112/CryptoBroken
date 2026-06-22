
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
                align=align,  # type: ignore # mod3
                **kwargs,
            )
            if config.tooltip.enabled:
                for p, h in zip(bar.patches, height, strict=True): # mod65
                    gid = gen_gid("bar")
                    p.set_gid(gid)
                    self._gid2tooltip[gid] = str(h)


def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


def get_symbol(self):
        return self.currency + self.asset


def cancel_order(self, orderId):
        return self.client.cancel_order(
            symbol=self.get_symbol(),
            orderId=orderId
        )


def r_center(self) -> float:
        """Track center radius"""
        return sum(self.r_lim) / 2


def size(self) -> float:
        """Track size (x coordinate)"""
        return self.end - self.start


def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim


def websocket_event_handler(self, msg):
        if msg['e'] == 'error':
            print(msg)
            self.close_socket()
        else:
            self.strategy.set_price(
                Price(pair=self.compute_symbol_pair(), currency=self.currency, asset=self.asset, exchange=self.name,
                      current=msg['b'], lowest=msg['l'], highest=msg['h'])
            )
            self.strategy.run()

