def search(pat, txt):
    m = len(pat)
    n= len(txt)
    count = 0
    for i in range(n- m +1):
        j = 0
         # Biến đếm số phép toán thực hiện
        # Mỗi phần tử i hiện tại kiểm tra sự trùng khớp mẫu
        while(j < m):
            if(txt[i+j] != pat[j]):
                count += 1
                break
        
            j += 1
          
        if(j == m):
            print("Mẫu xuất hiện ở vị trí %d" % i)
            print("Số phép toán phải thực hiện là %d" % count)
   
if __name__=="__main__":
    pat = "kbaa"
    txt = "nkanmankkbaa"
    search(pat, txt)