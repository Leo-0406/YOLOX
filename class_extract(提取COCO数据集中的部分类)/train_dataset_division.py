# # *_*coding: utf-8 *_*
# # Author --LiMing--
 
# import os
# import random
# import shutil
# import time
 
# def copyFile(fileDir, class_name):
#  image_list = os.listdir(fileDir) # 获取图片的原始路径
#  image_number = len(image_list)
 
#  train_number = int(image_number * train_rate)
#  train_sample = random.sample(image_list, train_number) # 从image_list中随机获取0.8比例的图像.
#  test_sample = list(set(image_list) - set(train_sample))
#  sample = [train_sample, test_sample]
 
#  # 复制图像到目标文件夹
#  for k in range(len(save_dir)):
#      if os.path.isdir(save_dir[k] + class_name):
#          for name in sample[k]:
#              shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k] + class_name+'/', name))
#      else:
#          os.makedirs(save_dir[k] + class_name)
#          for name in sample[k]:
#              shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k] + class_name+'/', name))
 
# if __name__ == '__main__':
#  time_start = time.time()
 
#  # 原始数据集路径
#  origion_path = '/home/ubuntu/COCO/images/'
#  #origion_path = '/data1/bhuang/3/images/'
 
#  # 保存路径
#  # save_train_dir = '/data1/bhuang/5/images/train/images/'
#  # save_test_dir = '/data1/bhuang/5/images/val/images/'

#  save_train_dir = '/home/ubuntu/COCO/divide/'
#  save_test_dir = '/home/ubuntu/COCO/divide/'
#  save_dir = [save_train_dir, save_test_dir]
 
#  # 训练集比例
#  train_rate = 0.8
 
#  # 数据集类别及数量
#  file_list = os.listdir(origion_path)
#  num_classes = len(file_list)
 
#  for i in range(num_classes):
#      class_name = file_list[i]
#      image_Dir = os.path.join(origion_path, class_name)
#      copyFile(image_Dir, class_name)
#      print('%s划分完毕！' % class_name)
 
#  time_end = time.time()
#  print('---------------')
#  print('训练集和测试集划分共耗时%s!' % (time_end - time_start))



 # 将图片和标注数据按比例切分为 训练集和测试集
 
import os
import random
from shutil import copy2
 
# 原始路径
image_original_path = "/home/ubuntu/COCO/images/train2017/"
label_original_path = "/home/ubuntu/COCO/annotations/train2017/"
# 上级目录
# parent_path = os.path.dirname(os.getcwd())
# parent_path = "D:\\AI_Find"

# 训练集路径
# train_image_path = os.path.join(parent_path, "image_data/seed/train/images/")
# train_label_path = os.path.join(parent_path, "image_data/seed/train/labels/")
train_image_path = os.path.join("/home/ubuntu/COCO/train/images/")
train_label_path = os.path.join("/home/ubuntu/COCO/train/annotations/")
# 测试集路径
test_image_path = os.path.join("/home/ubuntu/COCO/test/images/")
test_label_path = os.path.join("/home/ubuntu/COCO/test/annotations/")
 
 
# test_image_path = os.path.join(parent_path, 'image_data/seed/val/images/')
# test_label_path = os.path.join(parent_path, 'image_data/seed/val/labels/')
 
 
# 检查文件夹是否存在
def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)
    if not os.path.exists(test_image_path):
        os.makedirs(test_image_path)
    if not os.path.exists(test_label_path):
        os.makedirs(test_label_path)
def main():
    mkdir()
    # 复制移动图片数据
    all_image = os.listdir(image_original_path)
    for i in range(len(all_image)):
        num = random.randint(1,5)#随机给图片赋值，每五个随机赋值一次，抽取不为2的图片
        if num != 2:
            copy2(os.path.join(image_original_path, all_image[i]), train_image_path)
            train_index.append(i)
        else:
            copy2(os.path.join(image_original_path, all_image[i]), test_image_path)
            val_index.append(i)
 
    # 复制移动标注数据
    all_label = os.listdir(label_original_path)
    for i in train_index:
            copy2(os.path.join(label_original_path, all_label[i]), train_label_path)
    for i in val_index:
            copy2(os.path.join(label_original_path, all_label[i]), test_label_path)
 
 
if __name__ == '__main__':
    train_index = []
    val_index = []
    main()