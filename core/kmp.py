from typing import Tuple, List


class MatchKMP:
    def __init__(self, pattern: str):
        self._pattern = pattern
        self._fail = self._build_fail(pattern)

    def match(self, text: str) -> Tuple[bool, int]:
        pattern_index = 0
        text_index = 0

        while text_index < len(text) - len(self._pattern) + pattern_index + 1:
            if pattern_index == len(self._pattern):
                return True, text_index - len(self._pattern)
            if self._pattern[pattern_index] == text[text_index]:
                pattern_index += 1
                text_index += 1
            elif pattern_index != 0:
                pattern_index = self._fail[pattern_index]
            else:
                text_index += 1

        return False, -1

    @staticmethod
    def _build_fail(pattern: str) -> List[int]:
        """
        Build the fail array for pattern.
        fail[i] stores length of the longest proper prefix of pattern[:i]
        that is also a suffix.
        Consequently, fail[0] is irrelevant.
        """
        fail = [0] * len(pattern)

        # fail[0] is irrelevant
        # fail[1] is always zero

        for i in range(2, len(fail)):
            # determine fail[i] for pattern[:i]
            # with last letter pattern[i-1]
            new_letter = pattern[i - 1]
            prefix_length = fail[i - 1]

            while True:
                if pattern[prefix_length] == new_letter:
                    fail[i] = prefix_length + 1
                    break
                elif prefix_length == 0:
                    fail[i] = 0
                    break
                else:
                    prefix_length = fail[prefix_length]

        return fail
