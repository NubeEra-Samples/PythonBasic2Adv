basePath="D:\\Trainings\\AWSUSAClass\\Basic2AdvPython\\02.Statements\\"
import string
import os

aToZ=list(string.ascii_uppercase)
for Alpha in aToZ:
    path=basePath+Alpha    
    os.mkdir(path)