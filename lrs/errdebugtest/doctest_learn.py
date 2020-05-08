import doctest

class Dict(dict):
    """
    Simple dict but also support access as x.y style

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2)
    >>> d2.b
    2
    >>> d2["empty"]
    123
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError("Dict object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    doctest.testmod()