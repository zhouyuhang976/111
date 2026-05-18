# Binance Quant Bot

一个默认安全的币安现货量化机器人骨架：

- 默认 `paper` 模式，只做纸交易
- 真下单默认走币安现货；控制台里可切到实验性的 `USDⓈ-M Futures`
- 控制台已支持实验性的 `USDⓈ-M Futures` 参数入口，建议优先跑测试网
- `live` 模式默认走 Spot Testnet
- 切到币安主网前，必须显式设置环境变量解锁
- 自带一个简单的均线交叉策略，方便你后续替换

## 功能

- 读取币安 K 线
- 基于收盘价做均线交叉信号
- 纸交易资金曲线和持仓状态持久化
- 支持止损、止盈、冷却条数、最大回撤保护
- 支持 `--once` 单次运行和常驻轮询

## 目录

- `main.py`：启动入口
- `config.example.json`：示例配置
- `bot/client.py`：币安 Spot REST 接口
- `bot/strategy.py`：均线策略
- `bot/broker.py`：纸交易 / 真交易执行
- `bot/engine.py`：主循环与风控

## 快速开始

1. 复制配置：

```powershell
Copy-Item .\config.example.json .\config.json
```

2. 先跑纸交易：

```powershell
py .\main.py --config .\config.json --once
py .\main.py --config .\config.json
```

3. 如果要跑 Spot Testnet：

```powershell
$env:BINANCE_API_KEY="your_testnet_key"
$env:BINANCE_API_SECRET="your_testnet_secret"
```

然后把 `config.json` 里的 `mode` 改成 `live`，并保持 `live.use_testnet` 为 `true`。

## 主网安全开关

如果你把 `live.use_testnet` 改成 `false`，程序还会要求你设置：

```powershell
$env:BINANCE_ENABLE_LIVE_TRADING="YES_I_UNDERSTAND"
```

不设置这个环境变量，程序会直接拒绝下单。

## 配置说明

- `symbol`：交易对，例如 `BTCUSDT`
- `interval`：K 线周期，例如 `1m`、`5m`、`15m`
- `strategy.fast_period` / `strategy.slow_period`：均线周期
- `execution.quote_asset_budget`：每次最多动用多少报价资产
- `paper.starting_quote_balance`：纸交易初始资金
- `risk.stop_loss_pct`：止损百分比，`0.02` 表示 2%
- `risk.take_profit_pct`：止盈百分比
- `risk.max_drawdown_pct`：最大回撤阈值，触发后暂停交易

## 注意

- 这是一个开发起点，不是现成盈利机器
- 真交易前先用 Testnet 和 `paper` 跑足够久
- 如果你账户里已有仓位，`live` 模式的本地状态可能和真实仓位不一致，建议先清仓或重置本地状态
- 币安区域限制、接口权限、最小下单额会影响实际可用性

## 后续建议

下一步通常会做这些增强：

- 加入更多策略或多因子信号
- 接 WebSocket，降低轮询延迟
- 增加 Telegram / 钉钉告警
- 增加回测模块和参数搜索
- 把状态存到 SQLite 或 PostgreSQL
