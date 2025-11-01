import os

print("正在终止希沃白板进程...")
os.system("taskkill /f /im EasiNote.exe")

# 获取配置文件目录
user_dir = os.path.expanduser("~")
file_path = os.path.join(user_dir, "AppData", "Roaming", "Seewo", "EasiNote5", "Data", "Configs.fkv")

# 对“IsGeneration7Device”配置项进行修改
# 打开配置文件并读取
print("正在修改配置文件...")
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 替换配置项
new_content = content.replace('DeviceCache.IsGeneration7Device\nTrue', 'DeviceCache.IsGeneration7Device\nFalse')

# 写入修改后的配置
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

# 对“IsIwb”配置项进行相同修改

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

new_content = new_content.replace('DeviceCache.IsIwb\nTrue', 'DeviceCache.IsIwb\nFalse')

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

# 任务完成提示

print("已完成配置修改，下次启动将以普通电脑模式启动希沃白板。")
print("按任意键或直接关闭窗口以退出。")
input()