import time
import numpy as np

# Hàm 1
def swap_list_inplace(path, swap_first, swap_last):
    path[swap_first], path[swap_last] = path[swap_last], path[swap_first]
    return path

# Hàm 2
def swap_list_np(path, swap_first, swap_last):
    path_updated = np.concatenate((path[:swap_first],
                                   path[swap_last:swap_first-1:-1],
                                   path[swap_last + 1:]))
    return path_updated

# Tạo danh sách có 1000 phần tử
my_list = list(range(1000))

# Đo thời gian thực hiện Hàm 1
start_time = time.time()
swap_list_inplace(my_list, 0, 999)
end_time = time.time()
print(f"Thời gian thực hiện Hàm 1: {end_time - start_time} giây")

# Đo thời gian thực hiện Hàm 2
start_time = time.time()
swap_list_np(my_list, 0, 999)
end_time = time.time()
print(f"Thời gian thực hiện Hàm 2: {end_time - start_time} giây")
