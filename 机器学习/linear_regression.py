import numpy as np 
from utils.featuers import prepare_for_training

class LinearRegression:
    def __init__(self,data,labels,polynomial_degree=0,sinusoid_degree=0,normalize_data=True):
        (data_processed,
         features_mean,
         features_deviation)=prepare_for_training(data,polynomial_degree=0,sinusoid_degree=0,normalize_data=True)
        self.data=data_processed
        self.labels=labels
        self.features_mean=features_mean
        self.features_deviation=features_deviation
        self.polynomial_degree=polynomial_degree
        self.sinusoid_degree=sinusoid_degree
        self.normalize_data=normalize_data
        
        num_features=self.data.shape[1]
        self.theta =np.zeros((num_features,1))
    
    def tranin(self,alpha,num_iterations=500):
        '''
        训练模块，执行梯度下降
        '''
        cost_history = gredient_descent(alpha,num_iterations)
        return self.theta
    
    
    def gredient_descent(self,alpha,num_iterations):
        """
        实际迭代模块，会迭代num_iterations 次数
        """
        for i in range(num_iterations):
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data,self.labels))
        return cost_history
    
    def gradient_step(self,alpha):
        """
        梯度下降参数更新计算方法，注意是矩阵运算
        """
        num_examples =self.data.shape[0]
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        delta =prediction - self.labels
        theta=self.theta
        theta = theta -alpha*(1/num_examples)*(np.dot(delta.T,self.data)).T
        self.theta = theta
    
    def cost_function(self,data,labels):
        """
        损失计算方法
        """
        num_examples = data.shape[0]
        delta = LinearRegression.hypothesis(self.data, self.theta) - labels
        cost = (1/2)*np.dot(delta.T,delta)
        return cost[0][0]
    
    def hypothesis(data,theta):
        prediction = np.dot(data,theta)
        return predictions
    
    
    def get_cost(self,data,labels):
        data_processed=prepare_for_training(data,
                                            self.polynomial_degree,
                                            self.sinusoid_degree,
                                            self.normalize_data)[0]

        return self.cost_function(data_processed, labels)
    
    def predict(self):
        """
        用训练好的参数模型，与预测得到回归值结果
        """
        data_processed=prepare_for_training(data,
                                            self.polynomial_degree,
                                            self.sinusoid_degree,
                                            self.normalize_data)[0]
        predictions=LinearRegression.hypothesis(data_processed, self.theta)
        