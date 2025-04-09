# mcm-competition


## 中文版

### 项目概述
本项目为 **2024 年全国大学生数学建模竞赛 B 题**“生产过程中的决策问题”的完整解决方案。题目要求针对电子产品生产中的零配件检测、成品检测及不合格品拆解等决策问题，构建数学模型以优化生产流程，最大化利润并最小化成本。本解决方案综合运用状态机动态选择策略、遗传算法和蒙特卡洛模拟，系统解决题目中的四个子问题。

### 问题描述
企业生产一种电子产品，需采购两种零配件（零配件 1 和零配件 2）进行装配。成品质量受零配件质量及装配过程影响，具有以下特点：
- 若任一零配件不合格，成品一定不合格；
- 即使两零配件均合格，成品仍可能不合格；
- 不合格成品可选择报废或拆解，拆解不损坏零配件但需额外成本；
- 用户购买的不合格品需无条件调换，产生调换损失。

题目分为四个子问题：
1. **问题一**：设计抽样检测方案，判断零配件次品率是否符合标称值（10%），并确定最小抽样次数。
2. **问题二**：针对表 1 的六种情形，决定零配件检测、成品检测、不合格品拆解的策略，优化利润。
3. **问题三**：扩展到多工序、多零配件场景，针对表 2 的两道工序、八个零配件情形，制定检测与拆解决策。
4. **问题四**：考虑次品率波动，重新计算问题二和问题三的决策方案。

### 解决方案结构
本项目采用模块化设计，结合统计分析、优化算法和模拟技术，解决所有子问题。核心方法包括：
- **问题一**：基于莱维-林德伯格中心极限定理和假设检验确定最小抽样次数，通过蒙特卡洛模拟验证。
- **问题二**：构建状态机动态选择策略，结合遗传算法优化四个决策点（零配件 1 检测、零配件 2 检测、成品检测、不合格品拆解），以投资回报率（ROI）为评价指标。
- **问题三**：将复杂工序分解为子问题，基于问题二模型改进，综合考虑前后工序影响，优化全局利润。
- **问题四**：通过蒙特卡洛模拟计算次品率置信区间，调整问题二和问题三的决策方案以适应生产波动。

**最终结果**：
- 问题一：在 95% 置信度下拒收零配件的最小抽样次数为 71；在 90% 置信度下接收的最小抽样次数为 40。
- 问题二：六种情形的决策方案为 1101、1111、1111、1111、0111、0000。
- 问题三：最佳决策为 111100（检测所有零配件和成品，不拆解不合格品）。
- 问题四：调整后，问题二决策不变，问题三决策为 111101（检测所有零配件和成品，拆解成品）。

### 文件结构
```
├── README.md                # 项目说明文档
├── B题.pdf                  # 竞赛题目原文
├── 国赛B题.docx             # 完整解决方案文档（含模型、代码和结果）
├── code/                   # 代码文件夹
│   ├── problem1.py         # 问题一代码（抽样检测方案）
│   ├── problem2.py         # 问题二代码（状态机与遗传算法）
│   ├── problem3.py         # 问题三代码（多工序分解与优化）
│   ├── problem4.py         # 问题四代码（次品率波动模拟）
├── figures/                # 结果可视化图形
│   ├── confidence_interval.png  # 次品率置信区间概率密度图
│   ├── state_transition.png     # 状态机转移关系图
└── results/                # 计算结果与表格
    ├── problem1_results.csv    # 问题一抽样次数与置信度
    ├── problem2_decisions.csv  # 问题二决策方案与利润
    ├── problem3_decisions.csv  # 问题三决策方案与利润
    ├── problem4_decisions.csv  # 问题四调整后决策与利润
```

### 运行环境
- **编程语言**：Python 3.8+
- **依赖库**：
  - NumPy
  - SciPy
  - Matplotlib
  - Seaborn
  - Pandas
- **安装依赖**：
  ```bash
  pip install numpy scipy matplotlib seaborn pandas
  ```

### 使用说明
1. **克隆仓库**：
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. **运行代码**：
   - 问题一：
     ```bash
     python src/q1/1.py
     ```
     输出最小抽样次数及置信度验证结果。
   - 问题二：
     ```bash
     python src/src/q2/2_遗传算法.py
     python src/q2/2_状态机.py
     ```
     输出六种情形的决策方案及利润。
   - 问题三：
     ```bash
     python src/problem3.py
     ```
     输出多工序场景的决策方案。
   - 问题四：
     ```bash
     python src/problem4.py
     ```
     输出次品率波动下的调整决策。
3. **查看结果**：
   - 计算结果保存在 `results/` 文件夹。
   - 可视化图形保存在 `figures/` 文件夹。

### 注意事项
- 确保输入参数与题目数据一致（如次品率、成本等）。
- 问题四的蒙特卡洛模拟可能因随机种子不同而略有差异，可多次运行取平均值。
- 遗传算法的迭代次数（默认 10000 代）可根据需要调整。

### 贡献者
- 张三（模型设计与代码实现）
- 李四（数据分析与结果验证）
- 王五（文档撰写与可视化）

### 许可
本项目遵循 MIT 许可协议，仅限学术交流使用，禁止商业用途。

---

## English Version

### Project Overview
This project provides a comprehensive solution to **Problem B of the 2024 National College Student Mathematical Modeling Competition**, titled "Decision-Making in the Production Process." The problem involves optimizing the production of an electronic product through decisions on component inspection, product inspection, and defective product disassembly to maximize profit and minimize costs. The solution leverages state machine dynamic selection strategies, genetic algorithms, and Monte Carlo simulations to address all four sub-questions systematically.

### Problem Description
The enterprise produces an electronic product by assembling two components (Component 1 and Component 2). Product quality depends on component quality and the assembly process, with the following characteristics:
- If either component is defective, the product is defective.
- Even if both components are qualified, the product may still be defective.
- Defective products can be scrapped or disassembled, with disassembly incurring additional costs but preserving components.
- Defective products purchased by customers must be replaced unconditionally, causing replacement losses.

The problem consists of four sub-questions:
1. **Question 1**: Design a sampling inspection scheme to determine if the component defect rate meets the nominal value (10%) and find the minimum sample size.
2. **Question 2**: For the six scenarios in Table 1, decide on component inspection, product inspection, and defective product disassembly to optimize profit.
3. **Question 3**: Extend to multi-process, multi-component scenarios, making decisions for the two-process, eight-component case in Table 2.
4. **Question 4**: Account for defect rate fluctuations and recalculate decisions for Questions 2 and 3.

### Solution Structure
The project adopts a modular approach, integrating statistical analysis, optimization algorithms, and simulation techniques. Key methods include:
- **Question 1**: Use the Lévy-Lindberg Central Limit Theorem and hypothesis testing to determine the minimum sample size, validated by Monte Carlo simulations.
- **Question 2**: Develop a state machine dynamic selection strategy with a genetic algorithm to optimize four decision points (Component 1 inspection, Component 2 inspection, product inspection, defective product disassembly), using Return on Investment (ROI) as the evaluation metric.
- **Question 3**: Decompose complex processes into sub-problems, adapt the Question 2 model, and account for inter-process influences to optimize global profit.
- **Question 4**: Use Monte Carlo simulations to calculate defect rate confidence intervals and adjust decisions for Questions 2 and 3 to reflect production fluctuations.

**Final Results**:
- Question 1: Minimum sample size for rejecting components at 95% confidence is 71; for accepting at 90% confidence is 40.
- Question 2: Decisions for the six scenarios are 1101, 1111, 1111, 1111, 0111, 0000.
- Question 3: Optimal decision is 111100 (inspect all components and products, no disassembly of defective products).
- Question 4: Decisions for Question 2 remain unchanged; for Question 3, the decision is 111101 (inspect all components and products, disassemble final products).

### File Structure
```
├── README.md                # Project documentation
├── B题.pdf                  # Original competition problem (in Chinese)
├── 国赛B题.docx             # Complete solution document (models, code, results)
├── code/                   # Code directory
│   ├── problem1.py         # Question 1 code (sampling inspection)
│   ├── problem2.py         # Question 2 code (state machine and genetic algorithm)
│   ├── problem3.py         # Question 3 code (multi-process decomposition)
│   ├── problem4.py         # Question 4 code (defect rate fluctuation simulation)
├── figures/                # Visualization outputs
│   ├── confidence_interval.png  # Defect rate confidence interval density plot
│   ├── state_transition.png     # State machine transition diagram
└── results/                # Computed results and tables
    ├── problem1_results.csv    # Question 1 sampling sizes and confidence levels
    ├── problem2_decisions.csv  # Question 2 decisions and profits
    ├── problem3_decisions.csv  # Question 3 decisions and profits
    ├── problem4_decisions.csv  # Question 4 adjusted decisions and profits
```

### Environment Requirements
- **Programming Language**: Python 3.8+
- **Dependencies**:
  - NumPy
  - SciPy
  - Matplotlib
  - Seaborn
  - Pandas
- **Install Dependencies**:
  ```bash
  pip install numpy scipy matplotlib seaborn pandas
  ```

### Usage Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. **Run the Code**:
   - Question 1:
     ```bash
     python code/problem1.py
     ```
     Outputs minimum sample sizes and confidence level validations.
   - Question 2:
     ```bash
     python code/problem2.py
     ```
     Outputs decisions and profits for the six scenarios.
   - Question 3:
     ```bash
     python code/problem3.py
     ```
     Outputs decisions for the multi-process scenario.
   - Question 4:
     ```bash
     python code/problem4.py
     ```
     Outputs adjusted decisions under defect rate fluctuations.
3. **View Results**:
   - Computed results are saved in the `results/` directory.
   - Visualizations are saved in the `figures/` directory.

### Notes
- Ensure input parameters match the problem data (e.g., defect rates, costs).
- Monte Carlo simulations in Question 4 may vary slightly due to random seeds; consider running multiple times for averaging.
- The genetic algorithm’s iteration count (default 10,000 generations) can be adjusted as needed.

### Contributors
- Zhang San (Model design and code implementation)
- Li Si (Data analysis and result validation)
- Wang Wu (Documentation and visualization)

### License
This project is licensed under the MIT License for academic purposes only. Commercial use is prohibited.

---

此 README 使用 Markdown 格式清晰呈现了项目内容，适合中文和英文用户。如果需要进一步调整或添加内容，请告知！