# coding:utf-8
import time
from pathlib import Path
import re
import logging


def search_info(file_path, file_type):
    path = Path(file_path)
    ###########普通写法##########
    # all_file=[]
    # for file in path.glob("**/*"):
    #     if re.search(file_type,str(file)):
    #         all_file.append(file)
    # return all_file

    #######列表推导式下写法#######
    return [all_file for all_file in path.glob("**/*") if re.search(file_type, str(all_file))]


def log(filename):
    # /var/log/python- 当前日期 /xxxx.log
    datefmt = time.strftime("%Y%m%d", time.localtime())
    data_folder = Path('D:\ilearning')/datefmt
    data_folder.mkdir(exist_ok=True, parents=True)
    print(data_folder/filename)
    logging.basicConfig(filename=data_folder/filename,  # log文件名
                        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
                        datefmt='%Y/%m/%d %I:%M:%S',  # 定义时间格式
                        # 定义输出log的格式
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s'
                        )

if __name__ == "__main__":
    files = search_info(r"D:\BaiduNetdiskDownload", "mp4$")
    log('test.log')
    for file in files:
        logging.info(file)