import os

def batch_rename(folder_path, prefix="file", start_num=1, suffix=None):
    if not os.path.isdir(folder_path):
        print("❌ 文件夹路径不存在！")
        return
    file_list = os.listdir(folder_path)
    current_num = start_num
    success_count = 0
    for filename in file_list:
        old_full_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_full_path):
            name_part, ext_part = os.path.splitext(filename)
            if suffix is None:
                new_filename = f"{prefix}_{current_num}{ext_part}"
            else:
                new_filename = f"{prefix}_{current_num}_{suffix}{ext_part}"
            new_full_path = os.path.join(folder_path, new_filename)
            os.rename(old_full_path, new_full_path)
            print(f"{filename} → {new_filename}")
            current_num += 1
            success_count += 1
    print(f"\n✅ 重命名完成！一共处理了 {success_count} 个文件")

if __name__ == "__main__":
    print("===== 批量文件重命名工具 =====")
    path = input("请输入目标文件夹完整路径：")
    pre = input("输入文件前缀：")
    num = int(input("输入起始编号："))
    batch_rename(path, pre, num)
  
