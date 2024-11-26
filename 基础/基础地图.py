# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

map = Map()
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 199),
    ("安徽省", 299),
    ("广东省", 399),
    ("湖北省", 599),
]

# 添加数据
map.add("测试地图", data, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

render_path = "../output/map.html"
map.render(render_path)
