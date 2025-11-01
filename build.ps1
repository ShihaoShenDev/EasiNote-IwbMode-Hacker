# 在安装之前，请确保你安装了 Python 3.14 及以上版本的运行时（尽管没用到3.14的新功能），并确保将 Python 添加到系统 PATH 环境变量中。
# 环境变量可以在安装运行时时设置，亦可手动进行配置。
# 理论上低于 3.14 的版本也是可以使用的，但是我没装，所以我就不知道旧版本的兼容性了[狗头]
# Script Co-Created with Windsurf Auto-Completion

# 安装 PyInstaller 依赖以创建可执行程序
# 我草怎么写着写着就成Python语法了
# 要知道PowerShell里的print是管理打印机的 ToT
# print("开始安装 PyInstaller...")
Write-Host "开始安装 PyInstaller..."
pip install pyinstaller

# 构建 Hack 程序
# print("开始构建 Hack 程序...")
Write-Host "开始构建 Hack 程序..."
pyinstaller --onefile --icon=icon.ico hack.py

# 构建 Reset 程序
# print("开始构建 Reset 程序...")
Write-Host "开始构建 Reset 程序..."
pyinstaller --onefile --icon=icon.ico reset.py

# print("构建成功。")
Write-Host "构建成功。"
