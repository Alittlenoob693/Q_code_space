#这个代码可能运行不了
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

torch.manual_seed(42)


train_data = datasets.CIFAR10(
    root='./data',
    train=True,
    download=True,
    transform=None
)


x, y = train_data[21]
plt.imshow(x)
plt.title(f'Label: {y}')
plt.show()


tarin_set, val_set = random_split(train_data, [40000, 10000])  # 40000+10000=50000
test_set = datasets.CIFAR10(
    root='./data',
    train=False,
    download=True,
    transform=None
)


train_loader = DataLoader(tarin_set, batch_size=500, shuffle=True)
val_loader = DataLoader(val_set, batch_size=500, shuffle=True)
test_loader = DataLoader(test_set, batch_size=500, shuffle=True)

def estimate_loss(model):
    re = {}
    model.eval()
    re['train'] = t_loss(model, train_loader)
    re['val'] = t_loss(model, val_loader)
    re['test'] = t_loss(model, test_loader)
    model.train()
    return re

@torch.no_grad()
def t_loss(model, dataloader):
    loss = []
    acc = []
    for inputs, labels in dataloader:
        inputs = inputs.float()
        logits = model(inputs)
        loss.append(F.cross_entropy(logits, labels).item())
        acc.append((logits.argmax(1) == labels).float().mean().item())
    return {
        'loss': sum(loss) / len(loss),
        'acc': sum(acc) / len(acc) * 100
    }

def train_m_l(model, optimizer, epochs=10):
    losses = []
    for epoch in range(epochs):
        model.train()
        for inputs, labels in train_loader:
            inputs = inputs.float()
            optimizer.zero_grad()
            logits = model(inputs)
            loss = F.cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()
            losses.append(loss.item())

        stats = estimate_loss(model)
        print(f'Epoch {epoch}: '
              f'Train Loss: {stats["train"]["loss"]:.3f} | '
              f'Val Acc: {stats["val"]["acc"]:.1f}%')
    return losses

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_channel, out_channel, stride=1, downsample=None):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channel, out_channel, kernel_size=3,
                               stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channel)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(out_channel, out_channel, kernel_size=3,
                               padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channel)
        self.downsample = downsample

    def forward(self, x):
        identity = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        if self.downsample is not None:
            identity = self.downsample(x)
        out += identity
        out = self.relu(out)
        return out



class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=10):
        super().__init__()
        self.in_channels = 64
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()

        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512 * block.expansion, num_classes)

    def _make_layer(self, block, out_channels, blocks, stride=1):
        downsample = None
        if stride != 1 or self.in_channels != out_channels * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channels, out_channels * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels * block.expansion))

        layers = []
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        self.in_channels = out_channels * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.in_channels, out_channels))

        return nn.Sequential(*layers)
    def forward(self, x):
        x = x.float()
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x


def resnet18():
    return ResNet(BasicBlock, [2, 2, 2, 2])



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = resnet18().to(device)
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)

print("开始训练...")
loss_history = train_m_l(model, optimizer, epochs=10)


model.eval()
test_result = t_loss(model, test_loader)
print(f"\n测试集准确率: {test_result['acc']:.1f}%")