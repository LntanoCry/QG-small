'''
Author       : chenrunyu
created time : 2022/3/29
Introduction : 实现多元线性回归模型
'''
import numpy as np

class LRegression(object):
    # 构造函数,初始化
    def __init__(self):
        self.weight = None     # 系数,即w1,w2,w3,...
        self.intercept = None  # 截距
        self.themat = None     # x的系数和截距构成的系数矩阵

    # 用类实例模型调用类方法从而来训练模型
    def Fit(self,train_date,train_label): # 利用训练数据集来训练模型
        if train_date.shape[0] == train_label.shape[0]: # 判断训练集和标签的行数是否对应
            ones = np.ones((train_date.shape[0],1)) # 在每组向量中新增一个截距项
            X = np.hstack((ones,train_date))
            #下面是开始计算W和b,也就是通过训练设置类实例的属性
            self.themat=np.linalg.inv(X.T.dot(X)).dot(X.T).dot(train_label) # 利用WX=Y求出W
            self.intercept = self.themat[0]
            self.weight = self.themat[1:]
            return self

    def Predict(self,text_date):
        assert self.intercept is not None and self.weight is not None # 要求在Predict前先进行Fit
        # assert text_date.shape[0] == self.weight.shape[0] # 保证为相同维度的向量
        X_predict = np.hstack([np.ones((text_date.shape[0],1)),text_date])
        Y_predict = X_predict.dot(self.themat)
        return Y_predict  # 返回用测试集预测的结果

    # 返回决定系数R^2,衡量超直线对数据的拟合程度
    def score(self,text_date,text_label):
        y_predict = self.Predict(text_date)
        return self.__r_squared(text_label,y_predict)

    def m_s_e(self,text_label,Y_predict):
        return np.mean(np.square(text_label-Y_predict))
    
    
    # 一般而言R^2有两种求法,此处用的是 1-SSE/SST
    def __r_squared(self,text_label,Y_predict):
        assert len(text_label) == len(Y_predict) #确保真实值和预测值的数量相同
        return 1 - (self.m_s_e(text_label,Y_predict)/np.var(text_label)) # MSE是指均方误差
    
    
    def __repr__(self):
        return "LRegression()"

    






