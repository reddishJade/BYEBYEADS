import os
import subprocess
import glob
import re
import shutil
from pathlib import Path
from datetime import datetime
import pytz

def generate_metadata(rule_count):
    # 获取北京时间
    beijing_tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(beijing_tz)
    
    metadata = f"""! Title: BYEBYEADS
! Homepage: https://github.com/reddishJade/BYEBYEADS
! Version: {current_time.strftime('%Y-%m-%d %H:%M:%S')}（北京时间）
! Description: 适用于AdGuard、uBlock Origin等的去广告规则，合并优质上游规则并去重整理排列
! Total count: {rule_count}

"""
    return metadata

os.chdir('tmp')

print("合并上游拦截规则")
file_list = glob.glob('adblock*.txt')
with open('combined_adblock.txt', 'w', encoding='utf-8') as outfile:
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
        outfile.write('\n')

with open('combined_adblock.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = re.sub(r'^[!].*$\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^#(?!\s*#).*\n?', '', content, flags=re.MULTILINE)

with open('cleaned_adblock.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("拦截规则合并完成")

print("合并上游白名单规则")
allow_file_list = glob.glob('allow*.txt')
with open('combined_allow.txt', 'w', encoding='utf-8') as outfile:
    for file in allow_file_list:
        with open(file, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
        outfile.write('\n')

with open('combined_allow.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    content = re.sub(r'^[!].*$\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^#(?!\s*#).*\n?', '', content, flags=re.MULTILINE)

with open('cleaned_allow.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("白名单规则合并完成")

print("过滤白名单规则")
with open('cleaned_allow.txt', 'r', encoding='utf-8') as f:
    allow_lines = f.readlines()

with open('combined_adblock.txt', 'a', encoding='utf-8') as outfile:
    outfile.writelines(allow_lines)

with open('combined_adblock.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('allow.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if line.startswith('@'):
            f.write(line)

current_dir = os.getcwd()
adblock_file = os.path.join(current_dir, 'cleaned_adblock.txt')
allow_file = os.path.join(current_dir, 'allow.txt')
target_dir = os.path.join(current_dir, '.././data/rules/')
Path(target_dir).mkdir(parents=True, exist_ok=True)
adblock_file_new = os.path.join(target_dir, 'adblock.txt')
allow_file_new = os.path.join(target_dir, 'allow.txt')
os.rename(adblock_file, adblock_file_new)
os.rename(allow_file, allow_file_new)

print("规则去重中")
os.chdir(".././data/rules/")  # 更改当前目录
files = os.listdir()  # 得到文件夹下的所有文件名称
result = []
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        if os.path.splitext(file)[1] == '.txt':
            with open(file, encoding="utf-8") as f:  # 打开文件
                result = list(set(f.readlines()))
                result.sort()
            
            # 添加元信息
            metadata = generate_metadata(len(result))
            with open('test' + (file), "w", encoding="utf-8") as fo:
                fo.write(metadata)  # 先写入元信息
                fo.writelines(result)  # 再写入规则
            
            os.remove(file)
            os.rename('test' + (file), (file))

print("规则去重完成")

# 清理临时文件夹
print("清理临时文件")
tmp_dir = os.path.join(os.path.dirname(os.getcwd()), 'tmp')
if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)
    print("临时文件清理完成")
