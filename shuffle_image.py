import os
from shutil import copy
import random

def split(config):
    img_path=config['img_path']
    json_path=config['json_path']
    save_path=config['save_path']
    shuffle = config['shuffle']
    num_each_dir = config['num_each_dir']
    img_list = []
    dir_list = os.listdir(img_path)
    for dir in dir_list:
        image_list = os.listdir(os.path.join(img_path,dir))
        for i,m in enumerate(image_list):
            image_list[i] = os.path.join(dir,m)
        img_list += image_list

    img_postfix = ['jpg', 'jpeg', 'png', 'PNG', 'tif']
    n = 0
    for index,img in enumerate(img_list):
        if img.split('.')[-1] not in img_postfix:
            img_list.pop(index - n)
            n += 1

    if len(img_list) > 0:
        if shuffle:
            random.shuffle(img_list)
            print("顺序已打乱")
        if not os.path.isdir(save_path):
            os.makedirs(save_path)

        for index,img in enumerate(img_list):
            if index > 200:
                break
            copy(os.path.join(img_path,img),save_path)
            print(img,"移动成功")

    else:
        print("文件夹里没有图像")


if __name__ == '__main__':

    config = {
    'img_path':'D:/dataset/可视化/证照最终',
    'json_path':'../dataset/extra_data/extra_data/zhengjian_labels',
    'save_path':'D:/dataset/证照抽检',
    'num_each_dir':100,
    'shuffle':True
    }
    split(config)