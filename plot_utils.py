"""
Provides set_yaxis_label() function for labeling color axis.
"""

__author__ = "Ondrej Tucek"
__email__ = "ondrej.tucek@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"


import numpy as np
import matplotlib.pyplot as plt
from pylab import text as label_text
from matplotlib.transforms import Bbox

def get_half_axis_coord(axis='y'):
    '''
    Return half size of axis range.
    '''

    ax = plt.gca()

    if axis == 'y':
        y_min = ax.get_ylim()[0]
        y_max = ax.get_ylim()[1]

        return (y_min + y_max)/2
    elif axis == 'x':
        x_min = ax.get_xlim()[0]
        x_max = ax.get_xlim()[1]

        return (x_min + x_max)/2
    else:
        raise TypeError("Inputs argumets are only 'y' or 'x'!")


def put_el_to_odd_position_at_array(_el, _arr):
    '''
    Return array with added _el on odd position.
    '''

    _arr_len = len(_arr)
    out_arr = [_el]*(2*_arr_len - 1)
    out_arr[0::2] = map(lambda x: x, _arr)

    return out_arr


def get_width_height_text(text=None):
    '''
    Return inverted coordinates of text string and their width
    and height in Bbox structure.

    For more information see
    http://matplotlib.org/users/transforms_tutorial.html
    '''

    fig = plt.gcf()
    ax = plt.gca()
    r = fig.canvas.get_renderer()

    if text is None:
        # for bounding box that encloses the axis
        bb = ax.yaxis.get_tightbbox(renderer=r)
    else:
        bb = text.get_window_extent(renderer=r)

    bb_inv = ax.transData.inverted()
    bbox = bb_inv.transform(
        (bb.x0, bb.y0, bb.x1, bb.y1)
    )
    # print('bb', bb)
    # print('bbox', bbox)

    return Bbox.from_bounds(bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1])


def fake_ylabel():
    '''
    Return Bbox structure of ylabel string.
    '''

    fig = plt.gcf()
    ax = plt.gca()

    h = plt.ylabel('this is vertical label')
    wh = get_width_height_text(h)
    h.set_visible(False)

    return wh


def fake_text(_text, rotation=90, size=12):
    '''
    Return array of width or height of text label in figure.
    '''

    x_coor, y_coor = 0.5, 0.5
    text_width = []
    text_height = []

    for t_el in _text:
        h = label_text(
            x_coor, y_coor, t_el,
            size=size,
            ha='center',
            va='center',
            rotation=rotation
        )
        bbox = get_width_height_text(h)
        if rotation == 90:
            text_width.append(bbox.width)
            text_height.append(bbox.height)
        elif rotation == 0:
            text_width.append(bbox.width)
            text_height.append(bbox.height)
        h.set_visible(False)

    return (text_width, text_height)


def set_yaxis_label(
        _text, _color, label='line', axis='ax1', ha='center', va='bottom',
        sep=', ', size=12, x_corr=0.0, y_corr=0.0, space_between_text = 0.005
    ):
    '''
        _text  ... string array of axis labels
        _color ... string array of color for axis labels
        label  ... [ 'line' | 'rows' | 'cols' ], mode of displaying axis labels
               ...      valid for 'rows' are 'ha' and 'va'
               ...      valid for 'cols' is only 'va'
        axis   ... [ 'ax1' | 'ax2' ], left/right axis y
        ha     ... [ 'left' | 'center' | 'right' ], horizontal alignment of labels
        va     ... [ 'top' | 'bottom' ], vertical alignment of labels
        sep    ... string, separator between labels, valid only for label='line'
        size   ... size in points, font size of labels
        x_corr ... float, position of labels, correction of position
        y_corr ... float, position of labels, correction of position
        space_between_text ... real positive number, means between labels
    '''

    t_len = len(_text)
    c_len = len(_color)
    ax = plt.gca()

    if label == 'rows':
        rotation = 0
    elif label == 'cols' or label == 'line':
        rotation = 90

    middle_point_ax = get_half_axis_coord()
    axs = get_width_height_text()
    ylab_bbox = fake_ylabel()
    text_size_arr = fake_text(_text, rotation, size)

    max_width = max(text_size_arr[0])
    min_width = min(text_size_arr[0])
    max_height = max(text_size_arr[1])
    min_height = min(text_size_arr[1])
    sum_width = sum(text_size_arr[0])
    sum_height_half = sum(text_size_arr[1])/2.0

    if t_len != c_len:
        raise ValueError('Size of text vector has to be equal to color vector!')

    if axis == 'ax1':
        x_bbox0 = ylab_bbox.x0
        x_bbox1 = ylab_bbox.x1
    elif axis == 'ax2':
        x_bbox0 = ylab_bbox.x1 + max_width
        x_bbox1 = ylab_bbox.x0 + max_width

    else:
        ValueError("Variable 'axis' has to be either ax1 or ax2!")

    if label == 'rows':
        zip_text_color = zip(_text[::-1], _color[::-1])

        if ha == 'left':
            x_coord = x_bbox1 - max_width + x_corr
        elif ha == 'center':
            x_coord = x_bbox1 - max_width/2 + x_corr
        elif ha == 'right':
            x_coord = x_bbox1 + x_corr
        else:
            ValueError("Variable 'ha' has to be either left, center or right!")

        if va == 'bottom':
            y_coord = middle_point_ax - sum_height_half + y_corr
        elif va == 'top':
            y_coord = axs.y1 - sum_height_half + y_corr
        else:
            ValueError("Variable 'va' has to be either bottom or top!")

    elif label == 'cols':
        zip_text_color = zip(_text, _color)
        x_coord = axs.x0 - (t_len-1)*(text_size_arr[0][0] + space_between_text) + x_corr

        if va == 'bottom':
            y_coord = middle_point_ax + y_corr
        elif va == 'top':
            y_coord = axs.y1 - min_height + y_corr
        else:
            ValueError("Variable 'va' has to be either bottom or top!")

        if axis == 'ax2':
            x_coord = x_bbox1 - max_width + x_corr

    elif label == 'line':
        text_with_sep = put_el_to_odd_position_at_array(sep, _text)
        color_with_col_sep = put_el_to_odd_position_at_array('k', _color)
        text_size_arr = fake_text(text_with_sep, rotation, size)
        zip_text_color = zip(text_with_sep, color_with_col_sep)

        max_width = max(text_size_arr[0])
        sum_height_half = sum(text_size_arr[1])/2.0

        x_coord = x_bbox1 + x_corr
        y_coord = middle_point_ax - sum_height_half + y_corr
        if axis == 'ax2':
            x_coord = x_bbox1 - max_width + x_corr

    else:
        raise ValueError("Variable 'label' has to be either rows, cols or line!")


    for i, (t_el, c_el) in enumerate(zip_text_color):
        h = label_text(
            x_coord, y_coord, t_el,
            size=size,
            color=c_el,
            ha=ha,
            va='bottom',
            rotation=rotation,
            transform=ax.transData
        )

        if label == 'rows' or label == 'line':
            y_coord += text_size_arr[1][i] + space_between_text
        elif label == 'cols':
            x_coord += text_size_arr[0][i] + space_between_text
