def preprocess_strong_suffix(shift, bpos, pat, m):
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and pat[i - 1] != pat[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j
    return shift, bpos

def preprocess_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]
    return shift

def search(txt, pat):
    m = len(pat)
    n = len(txt)
    bpos = [-1] * (m + 1)
    shift = [0] * (m + 1)
    shift, bpos = preprocess_strong_suffix(shift, bpos, pat, m)
    shift = preprocess_case2(shift, bpos, pat, m)
    s = 0
    count = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
            count += 1
        if j < 0:
            print("Pattern occur at shift: {}".format(s))
            s += shift[0]
        else:
            s += max(shift[j + 1], j - bpos[j] + 1)
            count += 1
    print("Number of operations: {}".format(count))
text = "abacaabadcabacabaabb"
pat = "abacab"
search(text, pat) 
'''Thuật toán Boyer-Moore được xem là cải tiến hơn thuật toán tìm kiếm vét cạn (brute-force) trong trường hợp:

Mẫu cần tìm kiếm có độ dài lớn và không có nhiều lặp lại các ký tự.
Chuỗi văn bản có độ dài rất lớn và không có nhiều sự xuất hiện của mẫu.
Bảng chữ cái (alphabet) có kích thước nhỏ.
Trong những trường hợp này, thuật toán Boyer-Moore có thể bỏ qua được nhiều ký tự trong chuỗi văn bản và giảm được số lần so sánh cần thiết. 
Trong trường hợp tốt nhất, thuật toán Boyer-Moore chỉ cần O (n / m) phép so sánh để tìm kiếm một mẫu có độ dài m trong một chuỗi văn bản có độ dài n3'''