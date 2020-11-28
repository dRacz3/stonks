import attr

@attr.s
class BUY:
    stonk_name : str = attr.ib()
    price : float = attr.ib(converter=lambda x : -x)
    amount :float  = attr.ib()
    date = attr.ib()
    action = attr.ib(default='BUY')

@attr.s
class SELL:
    stonk_name : str = attr.ib()
    price : float = attr.ib()
    amount :float  = attr.ib(converter=lambda x : -x)
    date = attr.ib()
    action = attr.ib(default='SELL')

@attr.s
class DIVIDENT:
    stonk_name : str = attr.ib()
    price : float = attr.ib()
    date = attr.ib()
    action = attr.ib(default='DIVIDENT')