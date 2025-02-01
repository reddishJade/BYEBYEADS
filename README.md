# BYEBYEADS

[![Update Rules](https://github.com/reddishJade/BYEBYEADS/actions/workflows/update-rules.yml/badge.svg)](https://github.com/reddishJade/BYEBYEADS/actions/workflows/update-rules.yml)

## 项目简介

BYEBYEADS 是一个优化的广告拦截规则集合项目，专门为 AdGuard、uBlock Origin 等广告拦截工具设计。本项目通过自动化方式定期整合多个优质上游规则源，并进行智能去重和优化处理，为用户提供一个高效、精简的广告拦截体验。

## 功能特点

- 🚀 自动更新：每12小时自动从上游规则源获取最新规则
- 🧹 智能去重：自动去除重复规则，保持规则集的简洁性
- 🔄 定期维护：通过 GitHub Actions 实现规则的自动更新和维护
- 📊 优质规则源：整合多个知名规则源，包括：
  - AdGuard 基础过滤器
  - AdGuard 反跟踪过滤器
  - AdGuard 移动广告过滤器
  - AdGuard 中文过滤器
  - EasyList
  - EasyList China
  - EasyPrivacy
  - xinggsf 规则
  - 以及更多...

## 规则订阅

### 规则状态
![规则更新](https://img.shields.io/badge/dynamic/json?color=blue&label=更新时间&query=time&url=https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/stats.json)
![规则数量](https://img.shields.io/badge/dynamic/json?color=blue&label=规则数量&query=count&url=https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/stats.json)

### 拦截规则

[Links](https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/adblock.txt)

### 白名单规则

[Links](https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/allow.txt)

## 更新周期

- 规则每12小时自动更新一次
- 更新时间基于北京时间
- 支持通过 GitHub Actions 手动触发更新

## 项目结构

```
BYEBYEADS/
├── data/
│   ├── python/
│   │   ├── dl.py      # 规则下载脚本
│   │   └── merge.py   # 规则合并处理脚本
│   └── rules/
│       ├── adblock.txt # 广告拦截规则
│       └── allow.txt   # 白名单规则
├── .github/
│   └── workflows/
│       └── update-rules.yml # 自动更新配置
├── requirements.txt    # Python依赖
└── README.md          # 项目文档
```

## 开发指南

### 环境配置

1. 克隆项目
```bash
git clone https://github.com/reddishJade/BYEBYEADS.git
cd BYEBYEADS
```

2. 创建并激活虚拟环境
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

### 手动更新规则

在虚拟环境中执行：
```bash
python data/python/dl.py    # 下载规则
python data/python/merge.py # 合并处理规则
```

## 致谢

感谢以下规则项目的贡献：
- AdGuard Filters
- EasyList
- EasyList China
- xinggsf
- 以及其他所有规则贡献者

---
*本项目不定期更新规则源列表，以提供更好的广告拦截效果。*
