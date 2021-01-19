from .Odo import Odometer
o = Odometer(4)

def test_is_ascending():
    assert(o.is_ascending(1234) == True)
    assert(o.is_ascending(4231) == False)
    assert(o.is_ascending(5678) == True)
    assert(o.is_ascending(1020) == False)
    assert(o.is_ascending(9999) == False)

def test_next_reading():
    o.next_reading(2)
    assert(o.position == 2)

    # o.position = o.LENGTH - 1
    o.next_reading(o.LENGTH - 2)
    assert(o.position == 0)

    o.next_reading(o.LENGTH)
    assert(o.position == 0)

def test_prev_reading():
    o.prev_reading(2)
    assert(o.position == 124)

    # o.position = o.LENGTH - 1
    o.prev_reading(o.LENGTH - 2)
    assert(o.position == 0)

    o.prev_reading(o.LENGTH)
    assert(o.position == 0)