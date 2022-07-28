import os
from shutil import copy
import random

def split(config):
    img_path=config['img_path']
    json_path=config['json_path']
    save_path=config['save_path']
    shuffle = config['shuffle']
    num_each_dir = config['num_each_dir']

    img_list = os.listdir(img_path)
    img_postfix = ['jpg', 'jpeg', 'png', 'bmp', 'tif']
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

        tmp_img_path = os.path.join(save_path,'images','0')
        tmp_json_path = os.path.join(save_path,'labels','0')
        if not os.path.isdir(tmp_img_path):
            os.makedirs(tmp_img_path)
        if not os.path.isdir(tmp_json_path):
            os.makedirs(tmp_json_path)

        for index,img in enumerate(img_list):
            if index % num_each_dir == 0:
                tmp_img_path = os.path.join(save_path,'images',str(index // num_each_dir))
                tmp_json_path = os.path.join(save_path,'labels',str(index // num_each_dir))
                if not os.path.isdir(tmp_img_path):
                    os.makedirs(tmp_img_path)
                if not os.path.isdir(tmp_json_path):
                    os.makedirs(tmp_json_path)

            copy(os.path.join(img_path,img),tmp_img_path)
            json_file = os.path.join(json_path,'.'.join(img.split('.')[:-1])+'.json')
            copy(json_file,tmp_json_path)
            print(img,"移动成功")

    else:
        print("文件夹里没有图像")


if __name__ == '__main__':

    config = {
    'img_path':'../dataset/extra_data/extra_data/zhengjian_images',
    'json_path':'../dataset/extra_data/extra_data/zhengjian_labels',
    'save_path':'../dataset/extra_data/split',
    'num_each_dir':100,
    'shuffle':True
    }

split(config)