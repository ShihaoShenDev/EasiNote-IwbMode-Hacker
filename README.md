<div align="center">
  
  ![Icon](icon.png)
  # EasiNote IwbMode Hacker
  [![Build Application](https://github.com/ShihaoShenDev/EasiNote-IwbMode-Hacker/actions/workflows/build.yml/badge.svg)](https://github.com/ShihaoShenDev/EasiNote-IwbMode-Hacker/actions/workflows/build.yml)

  新一代希沃白板一体机伪装解决方案
  
</div>

## 简介
通过~~配置劫持~~最简单的配置修改，实现伪装方案。

## 原理
通过修改 `DeviceCache` 的方式实现。

## 立即使用

### 系统要求
- Windows 8 及以上版本
> [!IMPORTANT]
> Windows 7 及以下版本已不再支持新版本 Python。

### 二进制文件
目前在 [GitHub Actions](https://github.com/ShihaoShenDev/EasiNote-IwbMode-Hacker/actions/workflows/build.yml) 中提供。

要伪装为一体机，请使用 `hack.exe`；反之，则使用 `reset.exe`。

### 直接运行脚本
运行之前，请确保你已安装 [Python](https://www.python.org/downloads/), 并将其添加至 `PATH`。
``` powershell
# 伪装为一体机
python ./hack.py
```
``` powershell
# 恢复为普通电脑
python ./reset.py
```
### 手动构建二进制文件
先决条件：
- 已安装 Python 并将其添加至 `PATH`。
- `pip` 指令可在终端内直接使用。
打开一个新的 PowerShell 窗口，在包含源代码的目录输入：
``` powershell
./build.ps1
```
在 `dist` 目录下找到二进制文件。
