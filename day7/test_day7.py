from day7.day7 import align_horizontally


def test_align_horizontally_when_1_expect_0():
    crabs = [1]
    expected = 0

    actual = align_horizontally(crabs)

    assert expected == actual


def test_align_horizontally_when_1_2_expect_1():
    crabs = [1,2]
    expected = 1

    actual = align_horizontally(crabs)

    assert expected == actual


def test_align_horizontally_when_1_2_3_expect_2():
    crabs = [1,2,3]
    expected = 2

    actual = align_horizontally(crabs)

    assert expected == actual


def test_align_horizontally_when_1_2_4_expect_4():
    crabs = [1,2,4]
    expected = 4

    actual = align_horizontally(crabs)

    assert expected == actual


def test_align_horizontally_when_sample_expect_37():
    crabs = [16,1,2,0,4,2,7,1,2,14]
    expected = 168

    actual = align_horizontally(crabs)

    assert expected == actual