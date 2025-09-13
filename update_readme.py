import os

BOOKS_DIR = "./"
README_FILE = "README.md"

def scan_books(base_dir=BOOKS_DIR):
    """递归扫描目录，生成 Markdown 列表"""
    lines = []

    for root, dirs, files in os.walk(base_dir):
        # 相对路径（用于 README 链接和分层显示）
        rel_dir = os.path.relpath(root, base_dir)
        indent_level = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
        indent = "  " * indent_level

        # 如果是子目录，加目录标题
        if rel_dir != ".":
            folder_name = os.path.basename(root)
            lines.append(f"{indent}- **{folder_name}/**")

        # 文件列表
        for file in sorted(files):
            if file.startswith("."):  # 忽略隐藏文件
                continue
            file_path = os.path.join(root, file).replace("\\", "/")
            display_name = file
            lines.append(f"{indent}  - [{display_name}]({file_path})")

    return lines


def update_readme():
    """更新 README.md"""
    books_list = scan_books()

    header = "# 📚 我的电子书收藏\n\n以下是仓库中的电子书：\n\n"
    content = "\n".join(books_list) if books_list else "（目前还没有电子书哦）"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(header + content + "\n")

    print(f"✅ 已更新 {README_FILE}")


if __name__ == "__main__":
    update_readme()
