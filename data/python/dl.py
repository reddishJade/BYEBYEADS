import os
import subprocess
import time
import shutil
import requests

# 删除目录下所有的文件
directory = "./data/rules/"

# 确保目录存在并遍历删除其中的文件
if os.path.exists(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"无法删除文件: {file_path}, 错误: {e}")
else:
    print(f"目录 {directory} 不存在")

# 删除目录本身
try:
    shutil.rmtree(directory)
    print(f"成功删除目录 {directory} 及其中的所有文件")
except Exception as e:
    print(f"无法删除目录 {directory}, 错误: {e}")

# 创建临时文件夹
os.makedirs("./tmp/", exist_ok=True)

# 复制补充规则到tmp文件夹
# shutil.copy("./data/mod/adblock.txt", "./tmp/adblock01.txt")
# shutil.copy("./data/mod/whitelist.txt", "./tmp/allow01.txt")

# 拦截规则
adblock = [
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_10_Useful/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt",
    # "https://easylist-downloads.adblockplus.org/easylist.txt",
    # "https://easylist-downloads.adblockplus.org/easylistchina.txt",
    # "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    # "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt",
    "https://raw.githubusercontent.com/d3ward/toolz/master/src/d3host.txt",
    # "https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt",
    # "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt",
    # "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt",
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
]

# 白名单规则
allow = [
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/allowlist.txt"
]

# 下载函数
def download_file(url, output_path):
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()  # 检查请求是否成功
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"成功下载: {url} 到 {output_path}")
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")

# 下载拦截规则
for i, adblock_url in enumerate(adblock):
    output_path = os.path.join("./tmp/", f"adblock{i}.txt")
    download_file(adblock_url, output_path)
    time.sleep(1)

# 下载白名单规则
for j, allow_url in enumerate(allow):
    output_path = os.path.join("./tmp/", f"allow{j}.txt")
    download_file(allow_url, output_path)
    time.sleep(1)

print('规则下载完成')
