
import FileManager

# 根据书目判断 借阅相同书籍的学生 字典
def map_member_to_related_members():
    members = FileManager.get_all_members()
    books = FileManager.get_all_books()
    result = {}
    for member, book_list in members.items():
        related = []
        for b in book_list:
            if b in books:
                related.extend(books[b])  # 加入所有借该书的人
        # 去重并排除自己
        result[member] = list(set(x for x in related if x != member))
    return result


