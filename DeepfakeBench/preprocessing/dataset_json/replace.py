def replace_text_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 顺序不能反，先替换长的关键词，避免重复替换
    content = content.replace('FaceForensics++', 'FaceForensics++_c40')
    content = content.replace('c23', 'c40')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 示例用法
replace_text_in_file('/mnt/data1/xuekang/workspace/DeepfakeBench/DeepfakeBench/preprocessing/dataset_json/FaceForensics++_c40.json')
