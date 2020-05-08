import unittest

class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError("Dict object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d["empty"]