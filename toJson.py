import os
import json

# 定义基础 URL 和目录
directories = {
    "Alpha": {
        "base_url": "https://raw.githubusercontent.com/yinuan-i/mini/master/Alpha/",
        "name": "mini-Alpha-icons",
        "description": "By Orz-3"
    },
    "Color": {
        "base_url": "https://raw.githubusercontent.com/yinuan-i/mini/master/Color/",
        "name": "mini-Color-icons",
        "description": "By Orz-3"
    }
}

# 创建 JSON 结构的函数
def create_json_structure(directory, base_url, name, description):
    result = {
        "name": name,
        "description": description,
        "icons": []
    }

    for root, _, files in os.walk(directory):
        for file in files:
            file_url = f"{base_url}{file}"
            result["icons"].append({
                "name": file,
                "url": file_url
            })

    return result

# 生成并写入每个目录的 JSON 结构
for directory, info in directories.items():
    json_structure = create_json_structure(directory, info["base_url"], info["name"], info["description"])
    output_file = f"{directory}.json"
    
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(json_structure, json_file, ensure_ascii=False, indent=4)
    
    print(f"JSON 结构已创建并保存到 {output_file} 文件中")
