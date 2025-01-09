# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from glob import glob
from PIL import Image
# 把数据保存在pandas dataframe里
skin_df = pd.read_csv('HAM10000/HAM10000_metadata.csv')
# 读取图像
## 设置图像查询文件夹（两个）
image_path = {os.path.splitext(os.path.basename(x))[0]: x
                     for x in glob(os.path.join('HAM10000/', '*', '*.jpg'))}


# 加入图像数据的文件路径
skin_df['path'] = skin_df['image_id'].map(image_path.get)
# 通过文件路径读取图像
skin_df['image'] = skin_df['path'].map(lambda x: np.asarray(Image.open(x).resize((32,32))))
# print(skin_df['dx'].value_counts())

print(skin_df['dx'].value_counts())
# show the first one's image
plt.imshow(skin_df['image'][0])

