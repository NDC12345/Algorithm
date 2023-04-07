# KMPSearch(pat, txt)
from __future__ import annotations


def kmp(pattern: str, text: str) -> int:
    # 1) Construct the failure array
    failure = get_failure_array(pattern)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    count = 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return (i - j)
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
        count += 1
    
    


def get_failure_array(pattern: str) -> list[int]:
    """
    Calculates the new index we should go to if we fail a comparison
    :param pattern:
    :return:
    """
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure


text = "abacaabaccabacabaabb"
pattern = "abacab"
print("Tìm thấy mẫu ở vị trí %d " % kmp(pattern, text))