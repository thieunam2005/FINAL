import datetime


class SanPham:
    def __init__(self):
        self.maSP = ""
        self.thuongHieu = ""
        self.tenSP = ""
        self.giaSP = 0
        self.donVi = ""
        self.danhMuc = ""
        self.soDK = ""
        self.dangBC = ""
        self.quyCach = ""
        self.xuatXu = ""
        self.nhaSX = ""
        self.thanhPhan = ""
        self.moTa = ""
        self.hanSD = datetime.date.today()
        self.soLuong = 0
    def TC_Create(self):
        while True:
            maSP = input("Nhập mã sản phẩm (8 chữ số): ")
            if not re.match(r"^\d{8}$", maSP):
                print("Lỗi: Mã sản phẩm phải là chuỗi 8 chữ số!")
                continue
            self.maSP = maSP

            thuongHieu = input("Nhập thương hiệu: ").strip()
            if not thuongHieu:
                print("Lỗi: Thương hiệu không được để trống!")
                continue
            self.thuongHieu = thuongHieu

            tenSP = input("Nhập tên sản phẩm: ").strip()
            if not tenSP:
                print("Lỗi: Tên sản phẩm không được để trống!")
                continue
            self.tenSP = tenSP

            try:
                giaSP = float(input("Nhập giá sản phẩm: "))
                if giaSP <= 0:
                    print("Lỗi: Giá sản phẩm phải lớn hơn 0!")
                    continue
                self.giaSP = giaSP
            except ValueError:
                print("Lỗi: Giá sản phẩm phải là số!")
                continue

            donVi = input("Nhập đơn vị (ví dụ: viên, hộp): ").strip()
            if not donVi:
                print("Lỗi: Đơn vị không được để trống!")
                continue
            self.donVi = donVi

            danhMuc = input("Nhập danh mục: ").strip()
            if not danhMuc:
                print("Lỗi: Danh mục không được để trống!")
                continue
            self.danhMuc = danhMuc

            self.soDK = input("Nhập số đăng ký (nếu có): ").strip()

            dangBC = input("Nhập dạng bào chế (ví dụ: viên nén, siro): ").strip()
            if not dangBC:
                print("Lỗi: Dạng bào chế không được để trống!")
                continue
            self.dangBC = dangBC

            quyCach = input("Nhập quy cách (ví dụ: hộp 10 viên): ").strip()
            if not quyCach:
                print("Lỗi: Quy cách không được để trống!")
                continue
            self.quyCach = quyCach

            xuatXu = input("Nhập xuất xứ: ").strip()
            if not xuatXu:
                print("Lỗi: Xuất xứ không được để trống!")
                continue
            self.xuatXu = xuatXu

            nhaSX = input("Nhập nhà sản xuất: ").strip()
            if not nhaSX:
                print("Lỗi: Nhà sản xuất không được để trống!")
                continue
            self.nhaSX = nhaSX

            thanhPhan = input("Nhập thành phần: ").strip()
            if not thanhPhan:
                print("Lỗi: Thành phần không được để trống!")
                continue
            self.thanhPhan = thanhPhan

            self.moTa = input("Nhập mô tả (nếu có): ").strip()

            while True:
                try:
                    hanSD_str = input("Nhập hạn sử dụng (YYYY-MM-DD): ")
                    hanSD = datetime.datetime.strptime(hanSD_str, "%Y-%m-%d").date()
                    if hanSD < datetime.date.today():
                        print("Lỗi: Hạn sử dụng phải từ hôm nay trở đi!")
                        continue
                    self.hanSD = hanSD
                    break
                except ValueError:
                    print("Lỗi: Định dạng hạn sử dụng phải là YYYY-MM-DD!")

            try:
                soLuong = int(input("Nhập số lượng: "))
                if soLuong < 0:
                    print("Lỗi: Số lượng phải lớn hơn hoặc bằng 0!")
                    continue
                self.soLuong = soLuong
            except ValueError:
                print("Lỗi: Số lượng phải là số nguyên!")
                continue

            print("Tạo sản phẩm thành công!")
            break

