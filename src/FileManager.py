folder = r"C:\Users\Sudark\Desktop"
data = folder + "\\data.csv"
result = folder + "\\result.txt"


# 读取文件为List<String> labels
def read_data():
    with open(data, 'r', encoding='utf-8') as file:
        labels = file.readlines()
    return labels


# 获取 以姓名为键的字典
def get_all_members():
    members = {}
    for line in read_data():
        member, bookId = line.strip().split(',', 1)
        members.setdefault(member, []).append(bookId)
    return members


# 获取 以书号为键的字典
def get_all_books():
    books = {}
    for line in read_data():
        member, bookId = line.strip().split(',', 1)
        books.setdefault(bookId, []).append(member)
    return books


# 写文件至 result.txt
def write_file(content):
    with open(result, 'w', encoding='utf-8') as file:
        file.write(content)
