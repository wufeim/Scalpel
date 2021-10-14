# Scalpel - Experimental Results Dashboard

The ```Scalpel``` package helps users generate interactive HTML dashboard of their experimental results.

# Getting Started

## Installation

To install the latest release, run

```shell
pip install git+https://github.com/wufeim/Scalpel.git
```

## Example (Single Page)

```python
from scalpel import ScalpelDashboard, ScalpelTable, ScalpelText

table = ScalpelTable(columns=['query', 'return', 'prior', 'complete', 'score'])
table.append_row(['incomplete_0.png', 'return_0.png', 'prior_0.png', 'complete_0.png', 1.000])
table.append_row(['incomplete_1.png', 'return_1.png', 'prior_1.png', 'complete_1.png', 0.922])
table.append_row(['incomplete_2.png', 'return_2.png', 'prior_2.png', 'complete_2.png', 0.850])

dashboard = ScalpelDashboard(title='Completion Pipeline')
dashboard.add_text('Qualitative Example: 0000001.png', style='p')
dashboard.add_component(table)
dashboard.save_html('results.html')
```
