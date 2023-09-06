# import pyecharts

# print(pyecharts.__version__)


from pyecharts.charts import Line
from pyecharts.options import TitleOpts


#得到这线图对象
line = Line()
#得到x轴数据
line.add_xaxis(["中国","美国","日本"])
#得到y轴数据
line.add_yaxis("GDP",[30,20,10])

#设置全局变量
line.set_global_opts(
       title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="15")
)
# 生成图表
line.render()
