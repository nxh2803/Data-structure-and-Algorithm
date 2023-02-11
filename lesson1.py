# 1. Cấu trúc dữ liệu List
# List là một danh sách các thành phần dữ liệu được phân cách bởi dấu phẩy 
# và được bao ngoài bởi dấu ngoặc vuông

#! Danh sách 1 chiều
members_1 = ["Hung","Manh","Cuong"]
members_2 = ["Thom","Mai"]
ages = [20,19,21]
print(members_1[1])

#! Danh sách đa chiều 
members_3 = [["Hung",20],["Manh",19],["Cuong",21]]
print(members_3[0][0])
print(members_3[0][1])

#? Hàm, model cơ bản
print(f"Danh sách members_1 có {len(members_1)} bạn") # -> in ra số phần tử trong danh sách
members_1.append("Hieu") # -> thêm phần tử vào vị trí cuối cùng của danh sách
members_1.insert(1,"Tuan") # -> thêm phần tử vào danh sách tại ví trí cho trước
members_1[2] = "Hoa" # -> thay đổi giá trị tại vị trí cho trước
members_1.extend(members_2) # -> kết hợp danh sách với một danh sách khác
members_1.remove("Manh") # -> loại bỏ một phần tử khỏi danh sách
members_1.pop(3) # -> loại bỏ phần tử ở vị trí cho trước
del members_1[0] # -> xóa phần tử
members_1.clear() # -> xóa sạch các phần tử trong danh sách
members_1.count("Hung") # -> đếm số lần một phần tử xuất hiện trong danh sách
members_1.index("Hung") # -> trả về vị trí phần tử trong danh sách
members_1.sort() # -> xếp các phần tử tăng dần trong danh sách
members_1.sort(reverse=True) # -> xếp các phần tử giảm dần trong danh sách
members_1.reverse() # -> đảo ngược thứ tự các phần tử

# 2. Cấu trúc dữ liệu Tuple
# là một danh sách không thể thay đổi nội dung 
members_4 = ("Manh","Hung","Hieu")
# or members_4 = "Manh","Hung","Hieu" or members_4 = "Manh"

#! Thao tác cơ bản
check = "Cuong" in members_4 
len(members_4) 
# Lưu ý các phương thức thay đổi giá trị, thêm, sửa xóa không sử dụng được với cấu trúc dữ liệu này

# 3. Cấu trúc dữ liệu Set
# - có thể chứa nhiều các phần tử và các phần tử trong tập hợp này không có thứ tự 
# - dễ dàng duyệt qua các phần tử, có thể thêm xóa, có thể sử dụng union, intersection, difference,...
# - các phần tử là duy nhất, không lặp lại và phải cùng kiểu dữ liệu
members_5 = {"Manh","Hung","Hieu"}
members_6 = {"Tuan","Huy"}
#! Phương thức cơ bản
members_5.add("Cuong")
members_5.remove("Cuong")
members_5.discard("Cuong") # -> không báo lỗi 
members_5.pop() # -> loại bỏ phần tử đầu 
members_5.clear() # -> loại bỏ các phần tử trong tập hợp -> rỗng
members_5.update(["Tuan","Huy"]) #-> thêm nhiều phần tử
all_members = members_5.union(members_6) # -> hợp của 2 tập hợp
dif_members = members_5.difference(members_6) # -> hiệu của 2 tập hợp
sy_dif_members = members_5.symmetric_difference(members_6) # -> hiệu đối xứng của 2 tập hợp
int_memmbers = members_5.intersection(members_6) # -> giao của 2 tập hợp

#4. Stacks

stack = []
stack.append('Hung')
stack.append('Hieu')
stack.append('Manh')
print(stack)
stack.pop() # -> loại bỏ phần tử cuối Stack
stack.put("Cuong")

# Stack with a Python list
class ArrayStack:
    def __init__(self):
        self._data








