import FileManager
import DataHandler

if __name__ == '__main__':
    content = ""
    content += "=== 校园图书馆借阅关系网络分析报告 ===\n\n"

    dataMap = DataHandler.map_member_to_related_members()

    content += "各学生的借阅关系网络:\n"
    content += "\n".join(f"{k}: {v}" for k, v in dataMap.items())

    content += "\n\n"

    content += "各学生的关联度：\n"
    content += "\n".join(f"{k}: {len(v)}" for k, v in dataMap.items())

    content += "\n\n"

    content += "网络核心分析:\n"
    sorted_items = sorted(dataMap.items(), key=lambda item: len(item[1]), reverse=True)
    key, value = sorted_items[0]
    content += f" 关联度最高的学生:\n{key}"
    content += f" 关联度最高的学生借阅关系网络:\n{value} (共 {len(value)} 人)"

    FileManager.write_file(content)
