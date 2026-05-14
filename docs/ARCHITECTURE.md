# AutoJob-Agent 项目架构

> 最后更新：2026-05-14

---

## 目录结构

```
app/
├── main.py                 # FastAPI 启动入口
│
├── core/                   # 全局配置
│   └── config.py           #   环境变量、密钥、连接参数
│
├── agent/                  # Agent 核心（项目的灵魂）
│   ├── state.py            #   Agent 记忆——节点间流转的数据结构
│   ├── graph.py            #   流程编排——节点如何连接、条件分支
│   ├── prompts/            #   Prompt 模板——给 LLM 的指令
│   │   ├── vision.txt      #     视觉分析 prompt
│   │   └── extraction.txt  #     数据提取 prompt
│   └── nodes/              #   每个节点是一个处理步骤
│       ├── search.py       #     Playwright 打开网页、截图
│       ├── vision.py       #     LLM 分析截图、判断翻页
│       ├── extract.py      #     LLM 将文本转为结构化 JSON
│       └── store.py        #     写入数据库
│
├── tools/                  # 工具层——Agent 调用的外部能力
│   ├── browser.py          #   Playwright 浏览器管理
│   ├── vision_client.py    #   MiMo V2.5 视觉模型调用
│   ├── llm_client.py       #   DeepSeek 文本模型调用
│   └── database.py         #   数据库读写操作
│
├── models/                 # 数据结构定义
│   ├── database.py         #   SQLAlchemy 引擎
│   ├── orm_models.py       #   数据库表结构
│   └── schemas.py          #   API 请求/响应模型
│
└── routers/                # API 路由（触发器，不含业务逻辑）
    └── agent.py            #   POST /agent/search — 触发 Agent
```

---

## 各层功能

| 层 | 目录 | 功能 | 当前状态 |
|----|------|------|----------|
| **启动入口** | `main.py` | 创建 FastAPI 实例，注册路由 | 已有 /health 接口 |
| **配置中心** | `core/` | 集中管理密钥、连接参数等配置 | 已完成 |
| **Agent 核心** | `agent/` | 定义 State、Graph、Nodes，驱动整个决策流程 | 待实现 |
| **工具层** | `tools/` | 封装外部服务调用（浏览器、LLM、数据库） | vision.py 和 extractor.py 待迁移 |
| **数据层** | `models/` | ORM 表模型、Pydantic 请求响应模型 | 引擎已建，模型待定义 |
| **API 路由** | `routers/` | 接收 HTTP 请求，触发 Agent 执行 | 待实现 |
