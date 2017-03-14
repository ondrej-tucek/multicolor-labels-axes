# Multicolor labels of axes
The following `plot_utils.py` file contains function `set_yaxis_label()` that allows the user set up color of labels vertical axes.
This function was developed under `matplotlib` package.

For correct displaying labels and graphs, it is recommended usage of parameter `figsize=(..., ...)` inside `plt.figure()`
and `x_corr` or `y_corr`.

## Arguments
| Property | Value Type   | Description | Notes |
| ---------| -------------| ----------- | ----- |
| label    | [ 'line' \| 'rows' \| 'cols' ] | mode of displaying axis labels | valid for `'rows'` are `ha` and `va`,</br>valid for `'cols'` is only `va` |
| axis     | [ 'ax1' \| 'ax2' ] | left/right axis y |  |
| ha       | [ 'left' \| 'center' \| 'right' ] | horizontal alignment of labels |  |
| va       | [ 'top' \| 'bottom' ] | vertical alignment of labels |  |
| sep      | string | separator between labels | valid only for `label='line'` |
| size     | size in points | font size of labels |  |
| x_corr   | float | position of labels | correction of position |
| y_corr   | float | position of labels | correction of position |
| space_between_text  | real positive number | means between labels |  |

## Usage
```python
import matplotlib.pyplot as plt
import numpy as np

from plot_utils import set_yaxis_label

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

x = np.linspace(0,5,100)
y1 = ...
...
yN = ...

text = ['Label 1', ..., 'Label N']
color = ['#1F77B4', ..., '#47AC47']

ax.plot(x, y1, color=color[0])
...
ax.plot(x, yN, color=color[N])

plt.title('...')
plt.xlabel('...')

# The properties below are default.
set_yaxis_label(
    text,
    color,
    label='line',
    axis='ax1',
    ha='center',
    va='bottom',
    sep=', ',
    size=12,
    x_corr=0.0,
    y_corr=0.0,
    space_between_text = 0.005
)
```

## Examples
<div style="margin: 0px auto;">
	<table style="margin: 0px auto;">
		<tr valign="middle">
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig1a-code.png" height="150">
			</td>
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig1a.png" height="250">
			</td>
		</tr>
	</table>
	<table style="margin: 0px auto;">
		<tr valign="middle">
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig1b-code.png" height="200">
			</td>
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig1b.png" height="250" width="330">
			</td>
		</tr>
	</table>
	<table style="margin: 0px auto;">
		<tr valign="middle">
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig2a-code.png" height="170">
			</td>
			<td align="center" rowspan="2">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig2a.png" height="250" width="330">
			</td>
		</tr>
        <tr>
            <td>
                Used <a href="https://lmfit.github.io/lmfit-py/model.html">data</a>
            </td>
        </tr>
	</table>
	<table style="margin: 0px auto;">
		<tr valign="middle">
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig2b-code.png" height="200">
			</td>
			<td align="center" rowspan="2">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig2b.png" height="250" width="330">
			</td>
		</tr>
        <tr>
            <td>
                Used <a href="https://lmfit.github.io/lmfit-py/model.html">data</a>
            </td>
        </tr>
	</table>
	<table style="margin: 0px auto;">
		<tr valign="middle">
			<td align="center" rowspan="2">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig3cd-code.png" height="560" width="220">
			</td>
			<td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig3c.png" height="250" width="330">
			</td>
		</tr>
        <tr>
            <td align="center">
                <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig3d.png" height="250" width="330">
            </td>
        </tr>
	</table>
</div>
<p align="center">
    <img src="https://raw.github.com/ondrej-tucek/multicolor-labels-axes/master/img/fig3a.png" height="415">
</p>

## TODO
- [x] multicolor labels of one vertical axis
- [x] multicolor labels of two vertical axes
- [ ] multicolor labels of axis X

## License
[MIT](https://github.com/ondrej-tucek/multicolor-labels-axes/blob/master/LICENSE)

