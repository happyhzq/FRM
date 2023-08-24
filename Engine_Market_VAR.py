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
rt = ((pt + dt - pt-1)/pt-1 )  and t>0
#计算几何收益率
rt = ln((pt+dt)/(pt-1)) and t>1

#模拟收益的分布

distribution = f(rt) and t > 0

calculate u 
calculate variance



