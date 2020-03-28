from core.kmp import MatchKMP


def test_fail_function():
    string1 = "ABCACABC"
    assert MatchKMP._build_fail(string1) == [0, 0, 0, 0, 1, 0, 1, 2]

    string2 = "ABABCABABAB"
    assert MatchKMP._build_fail(string2) == [0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 3]


def test_kmp():
    text = "ABABCABABAB"
    matcher = MatchKMP("BABA")

    assert matcher.match(text) == (True, 6)


def test_kmp_dont_match():
    text = "ABABCABABAB"
    matcher = MatchKMP("BABAC")

    assert matcher.match(text) == (False, -1)


def test_kmp_complicated():
    pattern = "ababcababab"
    text = (
        "shfdfgjhofababcababafiasbabcbabcabbaba"
        "ccbcbaababcabaabbacbcababcbcababcbbacbbacbbcbaabab"
        "cabbcbcbacbacbbacababcabababcbahfhdsllss"
    )

    matcher = MatchKMP(pattern)
    found, index = matcher.match(text)
    assert found is True
    assert text[index : index + len(pattern)] == pattern


def test_kmp_at_end():
    pattern = "ababcababab"
    text = (
        "shfdfgjhofababcababafiasbabcbabcabbaba"
        "ccbcbaababcabaabbacbcababcbcababcbbacbbacbbcbaabab"
        "cabbcbcbacbacbbacababcababab"
    )

    matcher = MatchKMP(pattern)
    found, index = matcher.match(text)
    assert found is True
    assert text[index : index + len(pattern)] == pattern


def test_kmp_not_at_end():
    pattern = "ababcababab"
    text = (
        "shfdfgjhofababcababafiasbabcbabcabbaba"
        "ccbcbaababcabaabbacbcababcbcababcbbacbbacbbcbaabab"
        "cabbcbcbacbacbbacababcababa"
    )

    matcher = MatchKMP(pattern)
    found, index = matcher.match(text)
    assert found is False
