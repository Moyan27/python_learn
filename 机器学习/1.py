from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import jieba


def dome1():
    # 加载数据集
    iris = load_iris()
    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print(x_train.shape)


def dome2():
    # 实例化一个转换器(类)
    transfer = DictVectorizer(sparse=False)
    data = [{'city': '北京', '温度': 40}, {'city': '上海', '温度': 39}, {'city': '江西', '温度': 42}]
    data_new = transfer.fit_transform(data)
    # data_new 不是二维数组形式，稀疏矩阵将非零数据表示出来，节约内存
    # 所以在实例化时加入sparse=False,也可以用data.toarray()方法
    # print(data_new)
    # print('特征名字：',transfer.get_feature_names_out())
    # 合成新矩阵
    df = np.append([transfer.get_feature_names_out()], data_new, axis=0)
    print(df)


def deom3():
    data = ['life is short,i like python but i also like you', 'life is too long,i dislike python']
    # 实例化转换器 ，transfer 没有sparse=false参数, 所以转换的data用toarray()方法
    transfer = CountVectorizer()
    data_new = transfer.fit_transform(data)
    df = np.append([transfer.get_feature_names_out()], data_new.toarray(), axis=0)
    print(df)


def deom4():
    text = ['', '', '']
    data = '我爱北京天安门'
    a = ' '.join(list(jieba.cut(data)))
    # print(a)
