def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # Tạo ra 1 list các giá trị failure giữ giá trị tiền tố và hậu tố dài nhất cho mẫu
    lps = [0]*M
    j = 0 # chỉ số cho pat[]
    count = 0 # số phép toán
 
    # Tiền xử lý mẫu (calculate failure[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0 # chỉ số cho txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print ("Found pattern at index", str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        # phát hiện sự không khớp sau j lần khớp
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
            count += 1
        
 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)