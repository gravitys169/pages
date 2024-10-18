import os
import shutil

def list_subfolders(directory='.'):
    """
    列出指定目录下的所有子文件夹名称
    
    :param directory: 要搜索的目录路径,默认为当前目录
    :return: 无返回值,直接打印子文件夹名称
    """
    # 确保目录路径存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在")
        return
    
    # 获取目录下的所有项目
    items = os.listdir(directory)
    
    # 筛选出文件夹并排序
    subfolders = sorted([item for item in items if os.path.isdir(os.path.join(directory, item))])
    
    # 打印子文件夹名称
    if subfolders:
        print(f"'{directory}' 目录下的子文件夹:")
        for folder in subfolders:
            print(f"- {folder}")
    else:
        print(f"'{directory}' 目录下没有子文件夹")

def list_markdown_files(directory='.', output_file='README.md'):
    """
    遍历指定目录下的所有文件，将Markdown文件的路径和名称以多级目录形式输出到README.md
    如果文件名中包含空格，则将空格替换为下划��
    使用正斜杠(/)作为目录分隔符
    每次运行都会覆盖原有的README.md文件
    
    :param directory: 要搜索的目录路径，默认为当前目录
    :param output_file: 输出文件的名称，默认为'README.md'
    :return: 无返回值，直接写入文件
    """
    # 确保目录路径存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在")
        return
    
    # 用于存储Markdown文件信息的字典
    markdown_files = {}

    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'README.md':  # 排除README.md本身
                # 检查文件名是否包含空格
                if ' ' in file:
                    # 构建新的文件名，将空格替换为下划线
                    new_file = file.replace(' ', '_')
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_file)
                    
                    # 重命名文件
                    shutil.move(old_path, new_path)
                    print(f"已重命名: {file} -> {new_file}")
                    
                    # 更新文件名为新文件名
                    file = new_file
                
                # 构建相对路径，并将反斜杠替换为正斜杠
                relative_path = os.path.relpath(os.path.join(root, file), directory).replace('\\', '/')
                # 将路径分割成目录层级
                path_parts = relative_path.split('/')
                
                # 递归创建嵌套字典
                current_level = markdown_files
                for part in path_parts[:-1]:
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
                
                # 添加文件到最后一级
                current_level[path_parts[-1]] = relative_path

    def write_markdown_tree(tree, f, level=0):
        """递归写入Markdown树结构"""
        for key, value in sorted(tree.items()):
            if isinstance(value, dict):
                # 如果是目录
                f.write("  " * level + f"- {key}\n")
                write_markdown_tree(value, f, level + 1)
            else:
                # 如果是文件
                file_name = os.path.splitext(key)[0]
                f.write("  " * level + f"- [{file_name}]({value})\n")

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 目录\n\n")  # 修改这里，将标题改为"目录"
        write_markdown_tree(markdown_files, f)

    print(f"Markdown文件列表已写入到 {output_file}")

# 调用函数，遍历当前目录下的Markdown文件并输出到README.md
list_markdown_files()
