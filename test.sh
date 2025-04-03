#!/bin/bash

# 确保split_chapters.py可执行
chmod +x split_chapters.py

# 运行脚本处理示例文件
python split_chapters.py example.md

# 显示生成的文件
echo "生成的文件列表："
ls -la example/

# 显示生成的文件内容
echo -e "\n00_introduction.md 内容:"
cat example/00_introduction.md

echo -e "\n01_第一章：介绍.md 内容:"
cat example/01_第一章：介绍.md

echo -e "\n02_第二章：实现.md 内容:"
cat example/02_第二章：实现.md

echo -e "\n03_第三章：结论.md 内容:"
cat example/03_第三章：结论.md 