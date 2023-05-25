import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.tensorboard import SummaryWriter
 

class Mioird(nn.Module):
    def __init__(self):
        super(Mioird,self).__init__()
        # self.conv1 = Conv2d(in_channels=3,out_channels=32,kernel_size=5,stride=1,padding=2)
        # self.maxpool1 = MaxPool2d(kernel_size=2)
        # self.conv2 = Conv2d(in_channels=32,out_channels=32,kernel_size=5,stride=1,padding=2)
        # self.maxpool2 = MaxPool2d(kernel_size=2)
        # self.conv3 = Conv2d(in_channels=32,out_channels=64,kernel_size=5,stride=1,padding=2)
        # self.maxpool3 = MaxPool2d(kernel_size=2)
        # self.flatten = Flatten()
        # self.linear1 = Linear(1024,64)
        # self.linear2 = Linear(64,10)
 
        self.model1 = Sequential(
            Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2),
            MaxPool2d(kernel_size=2),
            Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            MaxPool2d(kernel_size=2),
            Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2),
            MaxPool2d(kernel_size=2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )
 
    def forward(self,x):
        # x = self.conv1(x)
        # x = self.maxpool1(x)
        # x = self.conv2(x)
        # x = self.maxpool2(x)
        # x = self.conv3(x)
        # x = self.maxpool3(x)
        # x = self.flatten(x)
        # x = self.linear1(x)
        # x = self.linear2(x)
        x = self.model1(x)
        return x
 
mioird = Mioird()
input = torch.ones((64,3,32,32))
output = mioird(input)

transformer_model = nn.Transformer(nhead=16, num_encoder_layers=12)
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))
out = transformer_model(src, tgt)

writer = SummaryWriter("logs")
writer.add_graph(transformer_model,(src, tgt))
writer.close()