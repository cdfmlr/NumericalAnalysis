# 算法流程图

这个目录下中存放数值分析实验中各种算法的程序流程图资料（只有报告（`ex?/report`）中用到的）。包括：

- `flowcharts.md`: 生成的流程图
- `src/*.py`: 用来生成流程图的简化版本代码（原版代码来自  `ex?/src/*.py`）

这些程序流程图是借助我的 [cdfmlr/pyflowchart](https://github.com/cdfmlr/pyflowchart) 工具逆向得到（并做了手动优化）。

> 具体生成的方法是：
>
> 1. 从 `ex?/src/*.py|ipynb` 复制源代码到该目录下的 `src`；
> 2. 手动化简代码；
> 3. 生成并复制流程图代码（pbcopy 是 macOS 的剪切板）：
>
> ```sh
> python3 -m pyflowchart adaptsim.py | pbcopy
> ```
>
> 4. 把流程图粘贴到 `flowcharts.md`。 


这些流程图是使用 [flowchart.js](https://github.com/adrai/flowchart.js) 语法表达的。在例如 Typora 的 Markdown 编辑器中，可以直接看到这些流程图的渲染结果，其他方法参见 [cdfmlr/pyflowchart](https://github.com/cdfmlr/pyflowchart) 与 [adrai/flowchart.js](https://github.com/adrai/flowchart.js)。

