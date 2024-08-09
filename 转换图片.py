from PIL import Image


def jpg_to_eps(jpg_file_path, eps_file_path):
    # 打开JPG图片
    image = Image.open(jpg_file_path)

    # 转换并保存为EPS格式
    image.save(eps_file_path, 'EPS')


# 使用示例
jpg_file_path = r'C:\Users\legionb\Desktop\0态.jpg'  # 使用原始字符串
eps_file_path = r'C:\Users\legionb\Desktop\output2.eps'  # 使用原始字符串
jpg_to_eps(jpg_file_path, eps_file_path)
