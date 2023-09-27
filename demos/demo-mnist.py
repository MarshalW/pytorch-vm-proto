import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

'''
示例使用了PyTorch的torchvision模块加载了MNIST数据集，并对数据进行了预处理。
然后定义了一个简单的全连接神经网络模型，使用交叉熵损失函数和随机梯度下降（SGD）优化器进行训练。
在训练过程中，每个epoch会打印出平均损失值。训练完成后，使用测试集进行推理并计算准确率。

请注意，这只是一个最简易的示例，实际的训练和推理过程可能需要更多的细节和调整，具体取决于任务和数据集的复杂性。
'''

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 加载训练集和测试集
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# 定义模型
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
for epoch in range(5):  # 进行5个epoch的训练
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data

        optimizer.zero_grad()

        outputs = model(inputs.view(inputs.size(0), -1))
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 200 == 199:  # 每200个batch打印一次损失值
            print(f'Epoch: {epoch + 1}, Batch: {i + 1}, Loss: {running_loss / 200:.3f}')
            running_loss = 0.0

print('Training finished.')

# 在测试集上进行推理
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = model(images.view(images.size(0), -1))
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy on test set: {(100 * correct / total):.2f}%')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")