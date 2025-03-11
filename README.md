# BYEBYEADS

[![Update Rules](https://github.com/reddishJade/BYEBYEADS/actions/workflows/update-rules.yml/badge.svg)](https://github.com/reddishJade/BYEBYEADS/actions/workflows/update-rules.yml)

## 规则订阅

### 规则状态

![规则更新](https://img.shields.io/badge/dynamic/json?color=blue&label=更新时间&query=time&url=https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/stats.json)  
![规则数量](https://img.shields.io/badge/dynamic/json?color=blue&label=规则数量&query=count&url=https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/stats.json)

### 拦截规则

[Links](https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/adblock.txt)

### 白名单规则

[Links](https://raw.githubusercontent.com/reddishJade/BYEBYEADS/main/data/rules/allow.txt)

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
└── README.md           # 项目文档
```

## 致谢

感谢以下规则项目的贡献：
- GoodbyeADs
- AdGuard Filters
- EasyList
- …
