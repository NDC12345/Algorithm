def preprocess_strong_suffix(shift, bpos, pat, m):
    # m là độ dài của mẫu
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        '''Nếu kí tự ở vị trí i-1 không tương đương với kí tự ở vị trí j-1
        , sau đó tiếp tục tìm kiếm ở vị trí mẫu cho biên giới'''
        while j <= m and pat[i-1] != pat[j - 1]:
            '''Kí tự trước sự xuất hiện của t trong mẫu P khác với ký tự 
            không khớp trong P, chúng ta dừng bỏ qua các lần xuất hiện và dịch mẫu
            từ i đến j'''
            if shift[j] == 0:
                shift[j] = j - i
            # Cập nhật vị trí của kí tự ranh tiếp
            j = bpos[j]
        '''p[i-1] trùng với p[j-1], kí tự ranh được tìm. Lưu vị trí bắt đầu của kí tự ranh'''
        i -= 1
        j -= 1
        bpos[i] = j
def process_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):
        '''Đặt vị trí đường viền của kí tự đầu tiên của mẫu cho tất cả
        các chỉ số trong dịch chuyển mảng shift[i] = 0'''
        if(shift[i] == 0):
            shift[i] = j
        '''Hậu tố trở nên ngắn hơn bpos[0], sử dụng vị trí của đường viền rộng nhất tiếp theo
        như giá trị của j'''
        if i == j:
            j = bpos[j]
def search(text, pat):
    count = 0
    s = 0
    m = len(pat)
    n = len(text)
    bpos = [0] * (m + 1)
    # Khởi tạo toàn bộ sự xuất hiện của shift là 0
    shift = [0] * (m + 1)
    preprocess_strong_suffix(shift, bpos, pat, m)
    process_case2(shift, bpos, pat, m)
    while(s <= n - m):
        j = m -1
        '''Giảm chỉ số j của mẫu trong khi kí tự của mẫu và đoạn text trùng nhau ở vị trì shift s'''
        while(j >= 0 and pat[j] == text[s+j]):
            j -= 1
        ''' Nếu mẫu có mặt trong đoạn text trên thì chỉ số j sẽ trở thành -1'''
        if j < 0:
            print("Mẫu xuất hiện ở vị trí %d" %s)
            s += shift[0]
        else:
            '''pat[i] != pat[s+j] vì vậy shift tới mẫu shift[j+1] lần'''
            s += shift[j + 1]
            count += 1
    print("Số lần thực hiện tính toán là: %d" %count)

if __name__ == "__main__":
    text = "abacaabadcabacabaabb"
    pat = "abacab"
    search(text, pat)           