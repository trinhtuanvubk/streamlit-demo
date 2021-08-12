import os 
from datetime import datetime
import random
path = os.path.join('./ok','datapth','rac')
print(path)

# def out_recorder_factory(word_name = 'ok', data_path= './data',usr_name = 'ok'):
#     numerical_order = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#     path = os.path.join(data_path,word_name,usr_name,str(numerical_order),str(random.randint(0,10)),'output.wav')
#     print(path)

data_path = './data'
number = 1 
numerical_order = '2020'
usr_name = 'vutuan'

path = os.path.join(data_path,str(number),usr_name+str(numerical_order)+str(random.randint(0,10))+'input.wav')
# os.mkdir(path)print(path)

num_order = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(type(num_order))