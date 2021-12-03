from day1.day1 import depth_increases, measurement_sets


def test_depth_increases_when_no_measurements_expect_0():
    measurements = []
    expected = 0

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_1_measurement_expect_0():
    measurements = [1]
    expected = 0

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_2_measurements_expect_1():
    measurements = [1, 2]
    expected = 1

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_3_measurements_expect_2():
    measurements = [1, 2, 3]
    expected = 2

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_three_measurements_one_decrease_expect_1():
    measurements = [1, 2, 1]
    expected = 1

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_four_measurements_one_decrease_expect_2():
    measurements = [1, 2, 1, 3]
    expected = 2

    actual = depth_increases(measurements)

    assert expected == actual


def test_depth_increases_when_sample_expect_7():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7

    actual = depth_increases(measurements)

    assert expected == actual


def test_measurement_sets_when_no_measurements_expect_empty():
    measurements = []
    expected = []

    actual = measurement_sets(measurements)

    assert expected == actual


def test_measurement_sets_when_1_measurement_expect_empty():
    measurements = [1]
    expected = []

    actual = measurement_sets(measurements)

    assert expected == actual


def test_measurement_sets_when_2_measurements_expect_empty():
    measurements = [1, 2]
    expected = []

    actual = measurement_sets(measurements)

    assert expected == actual


def test_measurement_sets_when_3_measurements_expect_6():
    measurements = [1, 2, 3]
    expected = [6]

    actual = measurement_sets(measurements)

    assert expected == actual


def test_measurement_sets_when_4_measurements_expect_6_9():
    measurements = [1, 2, 3, 4]
    expected = [6, 9]

    actual = measurement_sets(measurements)

    assert expected == actual
