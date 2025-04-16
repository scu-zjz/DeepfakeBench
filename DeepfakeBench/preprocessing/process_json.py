import os
import json

def replace_backslash(obj):
    if isinstance(obj, dict):
        return {k: replace_backslash(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_backslash(elem) for elem in obj]
    elif isinstance(obj, str):
        return obj.replace("\\", "/")
    else:
        return obj

# 你的 JSON 文件夹路径
folder_path = '/mnt/data1/xuekang/workspace/DeepfakeBench/preprocessing/dataset_json'  # 修改为你的路径

# 遍历文件夹中的所有 .json 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            cleaned_data = replace_backslash(data)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

            print(f"✅ 处理完成: {filename}")
        except Exception as e:
            print(f"❌ 处理失败: {filename}，错误信息：{e}")
