from pyecharts import options as opts
from pyecharts.charts import Bar, Gauge, Line, Page
from pyecharts.charts import Radar
from pyecharts.charts import WordCloud
from pyecharts.faker import Faker

page = Page()

# 词云(词云图)
# 构建词云数据,词云格式[(word,count),(word,count)]
data = [
    ('java', 170),
    ('python', 150),
    ('c', 112),
    ('javascript', 99),
    ('c++', 89),
    ('c#', 87),
    ('PHP', 79),
    ('SQL', 75),
    ('Go', 75),
    ('Swift', 74),
    ('Ruby', 72)
]
print({datum: datum for datum in data})

# 创建实例对象
c = WordCloud()
# c.add(series_name="", data_pair=data)
print(type(data))
c.add(series_name="", data_pair=data)
# 设置标题
c.set_global_opts(title_opts=opts.TitleOpts("编程语言排行"))
# 展示图片
c.render('worldcloud.html')

# example2
name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']

value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
dictionary = dict(zip(name, value))
l = list(dictionary.items())
# 创建实例对象
c2 = WordCloud()
c2.add(series_name="a", data_pair=l)
# 设置标题
c.set_global_opts(title_opts=opts.TitleOpts("xxxxtest"))
# 展示图片
c.render('worldcloud2.html')

# 绘制柱状图
v1 = [70, 85, 95, 64]
v2 = [80, 75, 85, 70]
str1 = ['数学', '物理', '化学', '英语']
bar = Bar()
bar.add_xaxis(str1)
bar.add_yaxis('小明', v1)
bar.add_yaxis('小红', v2)
bar.set_global_opts(title_opts=opts.TitleOpts(title='柱状图', subtitle='分数'))
bar.render()

# 绘制仪表盘图
c = (
    Gauge()
        .add("", [("完成率", 66.6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
        .render("gauge_base.html")
)

# 绘制雷达图
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

(
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
        .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="销售（sales）", max_=6500),
            opts.RadarIndicatorItem(name="管理（Administration）", max_=16000),
            opts.RadarIndicatorItem(name="信息技术（Information Technology）", max_=30000),
            opts.RadarIndicatorItem(name="客服（Customer Support）", max_=38000),
            opts.RadarIndicatorItem(name="研发（Development）", max_=52000),
            opts.RadarIndicatorItem(name="市场（Marketing）", max_=25000),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
        .add(
        series_name="预算分配（Allocated Budget）",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
        .add(
        series_name="实际开销（Actual Spending）",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="基础雷达图"), legend_opts=opts.LegendOpts()
    )
        .render("basic_radar_chart.html")
)

# 绘制面积图
c = (
    Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values(), is_smooth=True)
        .add_yaxis("商家B", Faker.values(), is_smooth=True)
        .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Line-面积图（紧贴 Y 轴）"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
        .render("line_areastyle_boundary_gap.html")
)
