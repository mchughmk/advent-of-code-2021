from day6.day6 import cycle_day, model_scenario


def test_cycle_day_when_empty_expect_empty():
    fish_state = [0,0,0,0,0,0,0,0,0]    
    expected = [0,0,0,0,0,0,0,0,0]

    actual = cycle_day(fish_state)

    assert expected == actual

def test_cycle_day_when_2_expect_1():
    fish_state = [0,0,1,0,0,0,0,0,0]    
    expected = [0,1,0,0,0,0,0,0,0]

    actual = cycle_day(fish_state)

    assert expected == actual

def test_cycle_day_when_0_expect_6_8():
    fish_state = [1,0,0,0,0,0,0,0,0]    
    expected = [0,0,0,0,0,0,1,0,1]

    actual = cycle_day(fish_state)

    assert expected == actual

def test_cycle_day_when_0_2_expect_6_8_1():
    fish_state = [1,0,1,0,0,0,0,0,0]    
    expected = [0,1,0,0,0,0,1,0,1]

    actual = cycle_day(fish_state)

    assert expected == actual

def test_model_scenario_when_empty_expect_0():
    fish_state = []
    expected = 0

    actual = model_scenario(fish_state, 1)

    assert expected == actual

def test_model_scenario_when_1_2_and_1_day_expect_2():
    fish_state = [1,2]
    expected = 2

    actual = model_scenario(fish_state, 1)

    assert expected == actual

def test_model_scenario_when_1_2_and_2_days_expect_3():
    fish_state = [1,2]
    expected = 3

    actual = model_scenario(fish_state, 2)

    assert expected == actual

def test_model_scenario_when_1_2_and_3_days_expect_4():
    fish_state = [1,2]
    expected = 4

    actual = model_scenario(fish_state, 3)

    assert expected == actual

def test_sample_scenario_when_18_days_expect_26():
    fish_state = [3,4,3,1,2]
    expected = 26

    actual = model_scenario(fish_state, 18)

    assert expected == actual

def test_sample_scenario_when_80_days_expect_5934():
    fish_state = [3,4,3,1,2]
    expected = 5934

    actual = model_scenario(fish_state, 80)

    assert expected == actual
