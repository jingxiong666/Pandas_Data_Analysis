import pandas as pd 
import numpy as np  
pd.read_csv("文件位置") #默认读取csv把表格第一行当做列名
pd.read_csv("文件位置", header = None) #不把第一行当表头，列名从0开始的数字代替
pd.read_csv("文件位置", index_col = '第一列列名') #将第一列作为标签索引
pd.set_option("display.max_columns", 150) #控制要展示的列数
pd.set_option("display.max_colwidth", 500) #控制每列的值最多包含几个字符

"""
数据评估：
一.结构
整洁数据：1.每列是一个变量
		 2.每行是一个观察值
		 3.每个单元格是一个值
二.内容
脏数据：1.丢失数据
	   2.重复数据
	   3.不一致数据
	   4.无效或错误数据
"""
"""
NumPy为核心数据结构ND array N维数组
Pandas数据结构Series和DataFrame
s1为df1的一列
"""
一、查看表

df1.tail() #获取表df1结尾5行
df1.tail(N) #获取表df1结尾N行
df1.head() #获取表df1前5行
df1.head(N) #获取表df1前N行
df1.sample(N) #随机选出N行
df1.info() #表概况信息：非空缺值有多少行，多少列，哪些数据类型
df1.describe() #展示数据列多种统计信息：个数、平均值、标准差、最大值、最小值

1.查看空缺值
df1.isnull() #检查值是否为空缺值：是空缺值（True），不是（False）
s1.isnull()
s1.isnull.sum() #求空缺值数量和
df1[df1["s1"].isnull()] #提取空缺值行

2.评估重复数据
df1.duplicated() #检查值或行是否存在重复
df1["s1"].duplicated #当前值在前面存在过返回True，否则返回False
df1.duplicated(subset = ["s1", "s2"]) #s1，s2都重复才返回布尔值
df1[df1.duplicated(subset = ["s1", "s2"])] #提取出所有重复的行

3.评估不一致数据
s1.value_counts() #返回s1中各个值的个数

4.评估无效/错误数据
s1.sort_values() #对值进行排序，查出是否有异常大/异常小值
s1.describe() #展示数据列多种统计信息：个数、平均值、标准差、最大值、最小值

二、清洗
#清洗前
df2 = df1.copy() #返回新表

1.索引，列名
df1.rename(index={"老名字":"新名字"; "老名字":"新名字"}) #重命名索引
df1.rename(columns={"老名字":"新名字"; "老名字":"新名字"}) #重命名列名
#rename()不会改变原表，要改变就重新赋值或加入 ",inplace=True"
df1.rename(columns={"老名字":"新名字"; "老名字":"新名字"}, inplace=True)
df2.rename(index=某函数/方法)
df2.rename(columns=某函数/方法)
df2.rename(columns=str.upper) #把所有列名改成大写

df1.set_index("s1") #把某列设为索引
df1.reset_index() #重新排序索引
df1.sort_index() #指定 ", axis=0" 时，对列重新排序，", axis=1"时，对行重新排序
#以上三种方法都不改变原表，要改变就重新赋值或加入 ",inplace=True"

2.结构性问题
"""
每列是观察值，每行是变量：将行列转置
每列包含多个变量：对列进行拆分或重塑
每行包括多个观察值：对行进行拆分/重塑，让每个观察值为独立的一行
"""
df1 = df1.T #表转置，并重新赋值
#拆分列，重新赋值或加入 ",inplace=True"
#"xx万人/yy平方公里".split("/") 可以转换为["xx万人", "yy平方公里"]
df1["人口密度"].str.split("/", expand=True) #把分割后的结果分别用Series表示
df2[["人口", "面积"]] = df1["人口密度"].str.split("/", expand=True)
df2 = df2.drop("人口密度", axis=1) #把原来的列删除
#合并列，重新赋值或加入 ",inplace=True"
df3["姓"].str.cat(df3["名"]) #把两列合并
df3["姓"].str.cat(df3["名"], sep="-") #定拼接分隔符
df3["姓名"] = df3["姓"].str.cat(df3["名"])
df3 = df3.drop(["姓", "名"], axis = 1) #重新赋值
#宽数据转换成长数据，重新赋值或加入 ",inplace=True"
pd.melt(df4, id_vars=["国家代码", "年份"], var_name= "年龄组", value_name= "肺结核病例数")
pd.melt(df4, id_vars=["s1", "s2"], var_name= "news3", value_name= "news4")
#拆分，重新赋值或加入 ",inplace=True"
df1.explode("s1") #s1列中都是一个个数组，把s1数组拆成单独值形成新行
#删除，重新赋值或加入 ",inplace=True"
df1.drop("index1", axis=0) #删除行，不写axis默认为0
df1.drop("s1", axis=1) #删除列
df1.drop(["index1", "index2"]) #一次性删除多行
df1.drop(["s2", "s3"], axis=1) #一次性删除多列
df1 = df1.drop(["index1", "index2"])
df1.drop(["s2", "s3"], axis=1, inplace = True)

3.内容性问题
"""
1.丢失数据：   
空缺值实际值。   
若不影响分析，则不处理空缺值。   
关键变量丢失：把空缺值所在行删除。   
填充值：平均数、中位数、众数。。。填进去
2.重复数据：   
找到后删除  
3.不一致数据：   
进行统一   
4.无效数据：  
删除无效数据使其变为`NaN`值或替换填充值:平均数、中位数、众数。。。
"""

#缺失值，重新赋值或加入 ",inplace=True"
df1["s1"]= "中国" #s1列全是缺失值，全部赋值为 中国
df1.loc["index1", "s1"] = 800 #某个值缺失，定位后赋值
df1.loc["index1":"index3", "s2"] = 800
df1["s1"].fillna(0) #将s1列所有NaN值填充为0
df1["s1"].fillna(s1.mean()) #将s1列所有NaN值填充为平均值
df2.fillna(0) #全表NaN全部替换为0
df3.fillna({"s1": 0, "s2": 1, "s4": 3}) #一次性分别替换NaN

df1.dropna() #删除所有包含NaN的行
df1.dropna(subset=["s1"]) #只删除s1列有NaN的行
df1.dropna(axis=1) #不指定axis默认为0，删除行，指定axis=1删除列

#重复数据，重新赋值或加入 ",inplace=True"
df1.drop_duplicates() #删除重复行，所有变量都一样才删
df2["s2"].drop_duplicates() #删除s1里的重复值
df3.drop_duplicates(subset=["s1", "s2"]) #s1和s2都重复才删除
#默认删除第二遍及以上出现的值
df3.drop_duplicates(keep='last') #只保留最后一个出现的值

#不一致数据，重新赋值或加入 ",inplace=True"
df2["s3"].replace("清华", "清华大学") #把s3列的 清华 替换成 清华大学
df2.repalce("清华", "清华大学") #把全表 清华 替换成 清华大学
df2["s3"].repalce(["清华", "五道口", "Tsinghua"], "清华大学")
replace_dict = {"华工": "华南理工", 
				"清华": "清华大学",
				"北大": "北京大学"}
df2.repalce(replace_dict) #传入字典，批量指定替换
df1["s1"].str.slice(0, -2) #字符串取出一部分

#数值类型转换
type() #查值类型
#Pandas中字符串str类型会被表示成object
df1["s1"].astype(str) #结果会是object
#Pandas数据类型category：指分类数据（性别，奖牌，部门种类）
s2 = pd.Series(["红", "红", "蓝", "绿"])
s2.astype("category") #category不是Python自带的，是Pandas库的，要用""包围，其他类型不用
pd.to_datetime(df1["s1"]) #转换为提起时间格式


3.整理数据
pd.concat([df1, df2]) #纵向拼接df1，df2
ps.concat([df1, df2], ignore_index = True) #忽视索引拼接
pd.concat([df1, df3], axis=1) #横向拼接

pd.merge(df1, df2, on = "s1")  #表合并
pd.merge(df1, df2, on = ["s1", "s2"]) #多列值同时匹配
pd.merge(df1, df2, left_on = ["s1", "s2"], right_on = ["S3", "s4"])
# left_on传入的是df1用于合并的列名，right_on传入的是df2用于合并的列名；
pd.merge(df1, df2, on = ["s1", "s2"], sufixes=["_df1", "_df2"])
#给合并后的重名列加后缀
pd.merge(df1, df2, on = "s1", how = "inner")
#how赋值可以是：inner、outer、left、right，不写默认是inner
#inner：只保留左右表都有匹配的值，不匹配就不合并进去
#outer：保留所有值，匹配不上的用NaN值填充
#left：根据左边表去匹配，保留左边所有值，匹配不上的用NaN
#right：根据右边表去匹配，保留左边所有值，匹配不上的用NaN
df1.join(df2, how = "inner") #join根据索引合并，保留两表所有列
df1.join(df2, how = "inner", lsuffix="_df1", rsuffix = "_df2")
#lsuffix：给左边表重名列名加后缀
#rsuffix：给右边表重名列名加后缀

df1.groupby("s1")["s2"].mean() 
"""
将s1中值相同的行组合到一起，但还要加上组合后想看的列名，以及对应的聚合函数
聚合函数：mean()、sum()、max()、min()
、count()、first()、last()、median()中位数
、std()标准差、var()方差、prod()积
只有在聚合函数运行后才能得到新表
"""
df1.groupby("s1")[["s2", "s3"]].mean()
df1.groupby(["s1", "s2"])["s3"].mean() #多变量聚合
def max_plus_10(nums):
	return nums.max() + 10
df1.groupby("s1")["s2"].apply(max_plus_10) #自定义聚合函数
#groupby后有分层索引的话，用下面的方法提取（切片）
grouped_df1.loc["001"] #提取“001”对应的片段
grouped_df1.loc["001"].loc["202210"] #提取"001"下，“202210”对应的片段
grouped_df1.reset_index() #重置groupby后的分层，还原成干净表的样子

pd.pivot_table(df1, index=["s1", "s2"], columns="s3", values="s4", aggfunc=np.sum)
"""
建立透视操作
index：索引
columns：列
values：值
aggfunc：聚合操作
s3分别在各个s1和在各个s2的s4聚合计算结果
"""
pd.pivot_table(df, index=["分店编号", "时间段"], columns="商品类别", values="销售额", aggfunc=np.sum)
#不传入aggfunc，默认是Numpy的mean方法

age_bins = [0, 10, 20, 30, 40, 50, 60, 120] #分箱
pd.cut(df1["s1"], age_bins) #切片
#返回新的列，数据类型都是category
age_labels = ["儿童", "青少年", "青年", "壮年", "中年", "中老年", "老年"]
pd.cut(df1["年龄"], age_bins, labels = age_labels)
#指定可选参数labels=自定义的分组标签列表
df1["年龄组"] = pd.cut(df1["年龄"], age_bins, labels = age_labels)
df1.groupby("年龄组")["工具"].mean()
#即可得到各个年龄组的平均工资

df1[(df1["性别"] == "男") & (df1["年龄"] <= 20)] #条件筛选
df1.query('(性别 == "男") & (年龄 <= 20)')  #条件筛选



4.保存数据
df1.to_csv("文件路径") #覆盖或新建文件
df1.to_csv("文件路径", index=False) #写入时自动忽略索引，索引没关键信息在用
#默认把列名和索引都写入文件，但再读取会不知道是索引
cleaned_df1.rename(columns={"Unnamed:0": "s1"}, inplace=True)
cleaned_df1.set_index("s1", inplace=True)
