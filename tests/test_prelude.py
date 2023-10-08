from std.prelude import derive
from std.cmp import PartialEq

def test_derive():
    @derive(PartialEq)
    class MyClass:
        pass

    assert True
