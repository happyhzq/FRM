#加载需要的库
#导入宏观数据库
import macro_history as macro_h
#导入股票数据库
import stock_price_history as st_p
#导入期货数据库
import future_price_history as fu_p
#导入外汇数据库
import fx_price_hisotry as fx_p
#导入债券数据库
import bond_price_history as bo_p
#导入自有的投资组合
import portfolio as pf
import pandas as pd



#首先判断投资组合的类型
#如果是投资组合全部是股票，那么用log normal distribution比较合适
if (portfolio = stock):
  {
    VAR = 1 - exponentiation ^ (u + z * segma)
  }
#如果投资组合全部是期货，那么用log normal distribution比较合适
elseif (portfolio = future):
  {
    VAR = 1 - exponentiation ^ (u + z * segma)
  }
#如果投资组合全部是外汇，那么用normal distribution比较合适
elseif (portfolio = fx):
  {
    VAR = -1 * ( u - z * segma)
  }
#如果投资组合全部是债券，那么用normal distribution比较合适
elseif (portfolio = bond):
  {
    VAR = -1 * (u - z * segma)
  }

#计算投资组合的收益率
#计算日收益率：
#计算算数收益率
arithmetic_rt = ((pt + dt - pt-1)/pt-1 )  and t>0
#计算几何收益率
log_rt = ln((pt+dt)/(pt-1)) and t>1


#描述算数收益的分布情况：

distribution = f(arithmetic_rt) and t > 0

#计算样本量
calculate n 
#计算样本均值
calculate u
#计算样本方差
calculate variance
#计算样本标准差
calculate segma = std deviation
#计算样本峰度
calculate kurtosis
#计算样本的偏度
calculate skewness

#描述对数收益的分布情况
distribution = f(log_rt) and t > 0

#计算样本量
calculate n 
#计算样本均值
calculate u
#计算样本方差
calculate variance
#计算样本标准差
calculate segma = std deviation
#计算样本峰度
calculate kurtosis
#计算样本的偏度
calculate skewness

calculate VaR distribution

i = 0.0001
n = (0,10000)
q = n * i;

#一致性风险度量：
M = \int_{0}^{1} (p * q) dp
#计算指数加权函数：
p = (exponent ^(-(1-p) / r) / (1 - exponent ^ (-1 / r))

r = 0.05

calculate conditional VaR

calculate ES

ES = 1/n * VaR

compare the difference between VaR and ES

df = ES - VaR

if distribution != normal distribution and distribution != log_normal distribution:

{
  use noparametic method  
}



#为历史数据赋予权重









