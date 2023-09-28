import torch  
import torch.nn as nn  
import torch.optim as optim  
import numpy as np  
import matplotlib.pyplot as plt

'''
需要：pip3 install -U matplotlib

创建一个简单的线性回归模型来进行训练和推理.

先生成了一些随机的训练数据，然后将数据转换为 PyTorch 张量。
接下来，我们定义了一个线性回归模型，并创建了一个模型实例。
我们还定义了损失函数和优化器，然后进行了训练。
最后，我们使用训练好的模型进行了预测，并可视化结果输出为图片。
'''

# 生成训练数据  
np.random.seed(42)  
x = np.random.rand(100, 1)  
y = 1 + 2 * x + 0.1 * np.random.randn(100, 1)
# 将 NumPy 数组转换为 PyTorch 张量  
x_tensor = torch.from_numpy(x).float()  
y_tensor = torch.from_numpy(y).float()
# 定义线性回归模型  
class LinearRegression(nn.Module):  
   def __init__(self):  
       super(LinearRegression, self).__init__()  
       self.linear = nn.Linear(1, 1)
   def forward(self, x):  
       return self.linear(x)
# 创建模型实例  
model = LinearRegression()
# 定义损失函数和优化器  
criterion = nn.MSELoss()  
optimizer = optim.SGD(model.parameters(), lr=0.1)
# 训练模型  
num_epochs = 100  
for epoch in range(num_epochs):  
   # 前向传播  
   output = model(x_tensor)  
   loss = criterion(output, y_tensor)
   # 反向传播和优化  
   optimizer.zero_grad()  
   loss.backward()  
   optimizer.step()
   if (epoch + 1) % 10 == 0:  
       print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')
# 预测  
model.eval()  
with torch.no_grad():  
   x_test = np.random.rand(1, 1)  
   y_pred = model(torch.from_numpy(x_test).float())  
   print(f'Prediction: {y_pred.item():.4f}')
# 可视化结果保存为图片  
plt.scatter(x, y, color='blue', label='True data')  
plt.scatter(x, model(x_tensor).detach().numpy(), color='red', label='Prediction')  
plt.legend()  
plt.savefig('out.png')