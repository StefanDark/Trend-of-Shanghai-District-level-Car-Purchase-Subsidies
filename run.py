import numpy as np  
from sklearn.linear_model import LinearRegression  
import matplotlib.pyplot as plt  
from datetime import datetime, timedelta  
  
# 准备数据  此部分尚未完善，需手动贴入相关数据
dates = [  

]  
applications = 
  
# 将日期转换为数值（距离起始日期的天数）  
start_date = datetime.strptime(dates[0], '%Y-%m-%d')  
date_numbers = [(datetime.strptime(date, '%Y-%m-%d') - start_date).days for date in dates]  
  
# 创建线性回归模型  
model = LinearRegression()  
X = np.array(date_numbers).reshape(-1, 1)  
y = np.array(applications)  
model.fit(X, y)  
  
# 预测达到20000人的日期  
target = 20000  
predicted_day = (target - model.intercept_) / model.coef_[0]  
predicted_date = start_date + timedelta(days=predicted_day)  
  
# 输出预测结果  
print(f'线性回归模型预测申请数达到20000人的日期为：{predicted_date.strftime("%Y-%m-%d")}')  
  
# 可视化数据点和回归线  
plt.scatter(date_numbers, applications, color='blue', label='实际数据')  
plt.plot(date_numbers, model.predict(X), color='red', label='线性回归线')  
  
# 标记预测点  
plt.scatter(predicted_day, target, color='green', marker='x', s=100, label='预测点')  
plt.text(predicted_day, target, f'预测日期: {predicted_date.strftime("%Y-%m-%d")}', fontsize=8)  
  
plt.xlabel('日期（距离起始日期的天数）')  
plt.ylabel('申请数')  
plt.title('申请数增长趋势及预测')  
plt.legend()  
plt.savefig('application_trend_prediction.png')
