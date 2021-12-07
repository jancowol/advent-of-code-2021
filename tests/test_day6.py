import advent.day6 as d6

def test_day_6_1_model_fish_internal_clock():
    f = d6.Fish(3)

    f.day_tick()
    assert f.clock == 2

    f.day_tick()
    assert f.clock == 1

    result = f.day_tick()
    assert f.clock == 0
    assert result == None

    result = f.day_tick()
    assert f.clock == 6
    assert result == 8