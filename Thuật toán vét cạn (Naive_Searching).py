def search(pat, txt):
    m = len(pat)
    n = len(txt)
    count = 0
    # Vòng lặp để quét mẫu từng kí tự một
    for i in range(n - m + 1):
        j = 0
        # Trong mỗi chỉ số i hiện tại, kiểm tra xem có sự trùng của mẫu hay không
        while(j < m):
            if(txt[i + j] != pat[j]):
                count += 1
                break
            j += 1
        if(j == m):
            print("Pattern found at index ", i)
    print("Số phép tính là: ", count)
txt = "nkanmanjkakfjakfkajkkfaslfakfakfaalfajcajcancaowokkbaa"
pat = "kbaa"
search(pat, txt)