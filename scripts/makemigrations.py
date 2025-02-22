import os
import re
import subprocess

# 获取alembic/versions目录
versions_dir = 'alembic/versions'

# 获取所有版本文件
version_files = os.listdir(versions_dir)

# 提取版本号并找到最大值
version_numbers = []
for file in version_files:
    match = re.search(r'(\d+)', file)
    if match:
        version_numbers.append(int(match.group(1)))

# 计算下一个版本号
next_version = f"{max(version_numbers) + 1 if version_numbers else 1:04}"


# 手动输入消息
message = input("Please input migrate message:")

# 生成命令
command = f"alembic revision --autogenerate -m \"{message}\" --rev-id {next_version}"

# 执行命令
subprocess.run(command, shell=True)
