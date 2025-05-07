from bs4 import BeautifulSoup
import requests
import json
# import time

url_products = []
base_url = 'https://nhathuoclongchau.com.vn'
lst_url = ["/thuoc/thuoc-di-ung","/thuoc/thuoc-giai-doc-khu-doc-va-ho-tro-cai-nghien","/thuoc/thuoc-da-lieu"]
lstLink = []
data_list = []
for i in lst_url:
    a = base_url + i
    lstLink.append(a)

for i in lstLink:
    response = requests.get(i)
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.findAll("div", class_="h-full relative flex rounded-xl border border-solid border-white bg-white transition-all duration-300 ease-out hover:border-blue-5 flex-col")

    for j in products:
        url_elem = j.find("a", class_="px-3 block pt-3")
        if url_elem:
            url_ = url_elem["href"]
            url1 = base_url + url_
            url_products.append(url1)


for i in url_products:
    try:
        response_ = requests.get(i)
        response_.raise_for_status()
        soup_ = BeautifulSoup(response_.text, "html.parser")


        thuongHieu = soup_.find("a", class_="text-blue-5")
        thuongHieu = thuongHieu.getText(strip=True) if thuongHieu else "Không tìm thấy thương hiệu"

        tenSP = soup_.find("h1", class_="text-body1 omd:text-heading1 font-medium text-gray-10 inline align-middle")
        tenSP = tenSP.getText(strip=True) if tenSP else "Không tìm thấy tên sản phẩm"

        maSP = soup_.find("span", class_="text-body2 omd:text-body1 font-normal text-gray-7 cursor-pointer transition-all duration-300 hover:opacity-70")
        maSP = maSP.getText(strip=True) if maSP else "Không tìm thấy mã sản phẩm"

        giaSP = soup_.find("span", class_="umd:text-heading1 omd:text-title1 omd:font-semibold font-bold")
        giaSP= giaSP.getText(strip=True) if giaSP else "Không tìm thấy giá sản phẩm"


        danh_muc = "Không tìm thấy danh mục"
        so_dang_ky = "Không tìm thấy số đăng ký"
        dang_bao_che = "Không tìm thấy dạng bào chế"
        quy_cach = "Không tìm thấy quy cách"
        thanh_phan = "Không tìm thấy thành phần"
        chi_dinh = "Không tìm thấy chỉ định"
        chong_chi_dinh = "Không tìm thấy chống chỉ định"
        nha_san_xuat = "Không tìm thấy nhà sản xuất"
        nuoc_san_xuat = "Không tìm thấy nước sản xuất"
        xuat_xu_thuong_hieu = "Không tìm thấy xuất xứ thương hiệu"
        thuoc_can_ke_toa = "Không tìm thấy thông tin thuốc cần kê toa"
        mo_ta_ngan = "Không tìm thấy mô tả ngắn"
        doi_tuong_su_dung = "Không tìm thấy đối tượng sử dụng"
        luu_y = "Không tìm thấy lưu ý"

        contents = soup_.findAll("tr", class_="content-container")
        for content in contents:
            title_elem = content.find('p')
            value_elem = content.find('div')
            if title_elem:
                title = title_elem.text.strip()
                if title == "Danh mục":
                    a_elem = content.find('a')
                    danh_muc = a_elem.get_text(strip=True) if a_elem else "Không tìm thấy danh mục"
                elif title == "Số đăng ký":
                    span_elem = value_elem.find('span') if value_elem else None
                    so_dang_ky = span_elem.get_text(strip=True) if span_elem else "Không tìm thấy số đăng ký"
                elif title == "Dạng bào chế":
                    dang_bao_che = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy dạng bào chế"
                elif title == "Quy cách":
                    quy_cach = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy quy cách"
                elif title == "Thành phần":
                    a_elem = value_elem.find('a') if value_elem else None
                    thanh_phan = a_elem.get_text(strip=True) if a_elem else value_elem.get_text(strip=True) if value_elem else "Không tìm thấy thành phần"
                elif title == "Chỉ định":
                    a_elem = value_elem.find('a') if value_elem else None
                    chi_dinh = a_elem.get_text(strip=True) if a_elem else value_elem.get_text(strip=True) if value_elem else "Không tìm thấy chỉ định"
                elif title == "Chống chỉ định":
                    chong_chi_dinh = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy chống chỉ định"
                elif title == "Nhà sản xuất":
                    nha_san_xuat = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy nhà sản xuất"
                elif title == "Nước sản xuất":
                    nuoc_san_xuat = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy nước sản xuất"
                elif title == "Xuất xứ thương hiệu":
                    xuat_xu_thuong_hieu = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy xuất xứ thương hiệu"
                elif title == "Thuốc cần kê toa":
                    thuoc_can_ke_toa = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy thông tin thuốc cần kê toa"
                elif title == "Mô tả ngắn":
                    p_elem = value_elem.find('p') if value_elem else None
                    mo_ta_ngan = p_elem.get_text(strip=True) if p_elem else value_elem.get_text(strip=True) if value_elem else "Không tìm thấy mô tả ngắn"
                elif title == "Đối tượng sử dụng":
                    doi_tuong_su_dung = value_elem.get_text(strip=True) if value_elem else "Không tìm thấy đối tượng sử dụng"
                elif title == "Lưu ý":
                    td_elem = content.find('td', class_="text-gray-10 text-body1")
                    luu_y = td_elem.get_text(strip=True) if td_elem else "Không tìm thấy lưu ý"


        product_data = {
            "thuongHieu": thuongHieu,
            "tenSanPham": tenSP,
            "maSanPham": maSP,
            "giaSP":giaSP,
            "danhMuc": "THUỐC DỊ ỨNG - "+danh_muc,
            "soDangKy": so_dang_ky,
            "dangBaoChe": dang_bao_che,
            "quyCach": quy_cach,
            "thanhPhan": thanh_phan,
            "chiDinh": chi_dinh,
            "chongChiDinh": chong_chi_dinh,
            "nhaSanXuat": nha_san_xuat,
            "nuocSanXuat": nuoc_san_xuat,
            "xuatXu": xuat_xu_thuong_hieu,
            "thuocCanKeToa": thuoc_can_ke_toa,
            "moTa": mo_ta_ngan,
            "doiTuongSuDung": doi_tuong_su_dung,
            "luuY": luu_y,
            "URL": i
        }


        data_list.append(product_data)


        # print(f"Thương hiệu: {thuongHieu}")
        # print(f"Tên sản phẩm: {tenSP}")
        # print(f"Mã sản phẩm: {maSP}")
        # print(f"Danh mục: {danh_muc}")
        # print(f"Số đăng ký: {so_dang_ky}")
        # print(f"Dạng bào chế: {dang_bao_che}")
        # print(f"Quy cách: {quy_cach}")
        # print(f"Thành phần: {thanh_phan}")
        # print(f"Chỉ định: {chi_dinh}")
        # print(f"Chống chỉ định: {chong_chi_dinh}")
        # print(f"Nhà sản xuất: {nha_san_xuat}")
        # print(f"Nước sản xuất: {nuoc_san_xuat}")
        # print(f"Xuất xứ thương hiệu: {xuat_xu_thuong_hieu}")
        # print(f"Thuốc cần kê toa: {thuoc_can_ke_toa}")
        # print(f"Mô tả ngắn: {mo_ta_ngan}")
        # print("\n")


        # time.sleep(1)

    except requests.RequestException as e:
        print(f"Lỗi khi truy cập {i}: {e}")
        continue
    except Exception as e:
        print(f"Lỗi khi xử lý {i}: {e}")
        continue


try:
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print("Đã ghi dữ liệu vào file products.json")
except Exception as e:
    print(f"Lỗi khi ghi file JSON: {e}")