# Eevix AI 🤖

## 关于我

你好！我是 Eevix，一个可训练的 AI 助手。我基于 PyTorch 构建，拥有一个简洁而强大的神经网络结构，可以通过训练来学习和预测不同类型的数据。

我具备以下特点：
- 🧠 **灵活的模型架构**：采用三层全连接神经网络，支持自定义输入输出维度
- 📊 **自动数据处理**：内置合成数据生成器，无需准备真实数据即可开始训练
- 💾 **模型持久化**：训练完成后自动保存最优模型，方便后续加载使用
- ⚡ **高效训练**：支持 GPU 加速，训练过程实时显示损失和准确率

---

## 项目介绍

Eevix AI 是一个基于 PyTorch 的深度学习项目框架，主要用于分类任务。项目结构清晰，包含以下核心模块：

- **model/**：模型定义，包含 `EevixModel` 神经网络类
- **data/**：数据处理，负责生成合成数据和创建数据加载器
- **train/**：训练逻辑，包含训练、验证和模型保存功能
- **config/**：配置管理，用于存储训练参数和设置

项目使用合成数据进行训练，输入维度为 20，输出维度为 10（10 分类任务）。

---

## 安装指南

### 环境要求

- Python 3.8+
- PyTorch 1.8+

### 安装依赖

在项目根目录下运行以下命令安装所需依赖：

```bash
cd /workspace/eevix
pip install -r requirements.txt
```

依赖列表：
- `torch` - PyTorch 深度学习框架
- `numpy` - 数值计算库
- `pandas` - 数据处理库
- `scikit-learn` - 机器学习工具库

---

## 训练说明

### 运行训练

进入项目目录并运行训练脚本：

```bash
cd /workspace
python -m eevix.train.train
```

### 训练参数

训练脚本默认使用以下参数：

| 参数 | 值 | 说明 |
|------|-----|------|
| `batch_size` | 32 | 每批次数据量 |
| `num_epochs` | 10 | 训练轮数 |
| `learning_rate` | 0.001 | 学习率 |
| `input_dim` | 20 | 输入特征维度 |
| `output_dim` | 10 | 输出类别数 |
| `save_path` | `/workspace/models/eevix_model.pth` | 模型保存路径 |

### 训练过程

训练过程中会显示每轮的训练和验证损失及准确率：

```
使用设备: cuda
模型结构:
EevixModel(
  (fc1): Linear(in_features=20, out_features=128, bias=True)
  (fc2): Linear(in_features=128, out_features=64, bias=True)
  (fc3): Linear(in_features=64, out_features=10, bias=True)
  (relu): ReLU()
)
训练集大小: 800
验证集大小: 200
Epoch [1/10]
  Train Loss: 2.3045, Train Acc: 0.1125
  Val   Loss: 2.2987, Val   Acc: 0.1300
  ✓ 模型已保存到 /workspace/models/eevix_model.pth
```

训练完成后，最优模型会自动保存到 `models/eevix_model.pth`。

---

## 使用方法

### 加载模型

使用以下代码加载训练好的模型：

```python
import torch
from eevix.model import EevixModel

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = EevixModel().to(device)
model.load_state_dict(torch.load('/workspace/models/eevix_model.pth'))
model.eval()
```

### 进行预测

加载模型后，可以使用以下代码进行预测：

```python
import numpy as np

test_data = np.random.randn(1, 20)
input_tensor = torch.tensor(test_data, dtype=torch.float32).to(device)

with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1).item()

print(f'预测结果: {prediction}')
```

### 完整示例

```python
import torch
import numpy as np
from eevix.model import EevixModel

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = EevixModel().to(device)
model.load_state_dict(torch.load('/workspace/models/eevix_model.pth'))
model.eval()

test_samples = np.random.randn(5, 20)
input_tensor = torch.tensor(test_samples, dtype=torch.float32).to(device)

with torch.no_grad():
    outputs = model(input_tensor)
    predictions = torch.argmax(outputs, dim=1).tolist()

print('预测结果:', predictions)
```

---

## 项目结构

```
/workspace/
├── eevix/
│   ├── config/          # 配置模块
│   ├── data/            # 数据处理模块
│   │   └── dataset.py   # 数据集和数据加载器
│   ├── model/           # 模型模块
│   │   └── model.py     # EevixModel 定义
│   ├── train/           # 训练模块
│   │   └── train.py     # 训练和验证逻辑
│   └── requirements.txt # 依赖列表
├── models/              # 模型保存目录
│   └── eevix_model.pth  # 训练好的模型
└── README.md            # 项目说明文档
```

---

## 许可证

MIT License