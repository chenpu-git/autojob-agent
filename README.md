# AutoJob-Agent

高度工程化的求职 Browser Agent，通过自然语言驱动浏览器自动搜索岗位、提取结构化数据并持久化存储。

## 技术栈

| 组件 | 技术 |
|------|------|
| API 服务 | FastAPI |
| Agent 编排 | LangGraph |
| 浏览器自动化 | Playwright |
| VLM (视觉理解) | GPT-4o |
| 数据提取 | DeepSeek |
| 数据库 | PostgreSQL 15 |
| 缓存/队列 | Redis 7 |

## 项目结构

```
autojob-agent/
├── .env                  # 环境变量
├── docker-compose.yml    # Docker 服务配置
├── requirements.txt      # Python 依赖
└── app/
    ├── main.py           # FastAPI 入口
    ├── core/
    │   └── config.py     # 配置管理
    ├── models/
    │   └── database.py   # SQLAlchemy 引擎
    ├── routers/          # API 路由
    └── services/         # 核心业务与 Agent 逻辑
```

## 快速启动

### 1. 启动基础设施

```bash
docker compose up -d
```

启动 PostgreSQL（5432）和 Redis（6379）。

### 2. 创建虚拟环境并安装依赖

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. 启动 API 服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. 验证

访问 `http://localhost:8000/health`，返回 `{"status":"ok","database":"connected"}` 即表示启动成功。

Swagger 文档：`http://localhost:8000/docs`

## 环境变量

在 `.env` 文件中配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `POSTGRES_HOST` | localhost | 数据库地址 |
| `POSTGRES_PORT` | 5432 | 数据库端口 |
| `POSTGRES_USER` | autojob | 数据库用户 |
| `POSTGRES_PASSWORD` | autojob_dev_2024 | 数据库密码 |
| `POSTGRES_DB` | autojob | 数据库名 |
| `REDIS_HOST` | localhost | Redis 地址 |
| `REDIS_PORT` | 6379 | Redis 端口 |

## Agent 工作流

```
用户输入 → FastAPI → LangGraph Workflow
  ├─ Node 1 (Search)    Playwright 打开网页、截图、提取 DOM
  ├─ Node 2 (Vision)    GPT-4o 分析截图，执行翻页，抓取文本
  ├─ Node 3 (Extract)   DeepSeek 将文本清洗为标准 JSON
  └─ Node 4 (Storage)   SQLAlchemy 写入 PostgreSQL
```
