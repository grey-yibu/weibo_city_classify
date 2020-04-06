# coding=utf-8
# encoding=utf-8
"""
    Author      : grey(yangyuzhou)
    lastCtime   : 2018.8.6
    call        : 18813011762    563965323@qq.com
    desc        : weibo_sum 类
                  主要用于对一段文字进行切词合并
                  主要步骤：
                    1.加载文件内容到内存     self.loadFile()
                    2.对文本进行符号过滤     self.regularFunc()
                    3.对文本进行切词         self.startCutWord()
                    4.对切词进行合并         self.convergeWord_r()
                    5.对结果进行输出         self.show_ans()
    demo        :  依赖 加载文件,切词最短长度(默认2),切词最大长度(默认12)
                   a = weibo_sum(fileName, start, end)  ( 初始化 依赖变量 )
                   a.startInit()                        ( 包含1~4步骤 )
                   a.show_ans()                         ( 输出结果 )
    输出        ：出现次数    \t    出现内容    \t    \n(从高到低排序)
"""
import os
import re
import sys
import json
from collections import OrderedDict



all_city_dict      =  {}
all_cutword_array  =  []
all_city_ans       =  []
all_city_sort      =  []



def  loadFload():
    dir_or_files = os.listdir("./result")
    for dir_file in dir_or_files:
        #print  ("./result/"+dir_file)
        fp = open("./result/"+dir_file, "r")
        source_lines = ""
        try:
            source_lines = fp.read()
        finally:
            fp.close()
        try:
            tmp_json = json.loads(source_lines)
        except Exception as e:
            print ("./result/"+dir_file)
        all_city_dict[dir_file] = tmp_json
        count = 0
        for  i  in tmp_json:
            if count >= 1000:
                break
            count += 1
            if i  not  in  all_cutword_array:
                all_cutword_array.append(i)


def  remake_city_ans():
    for  city_id  in all_city_dict:
        tmp_num_array = []
        if  len(all_city_dict[city_id]) < 1000:
            continue
        for i in all_cutword_array:
            if  i in all_city_dict[city_id]:
                tmp_num_array.append( int(all_city_dict[city_id][i]) )
            else:
                tmp_num_array.append( 0 )
        all_city_sort.append(city_id)
        all_city_ans.append(tmp_num_array)


def  yibu_write( write_file_name, write_str ):
    fp = open(write_file_name, "w")
    try:
        fp.write(write_str)
    finally:
        fp.close()



def  dict_write():
    all_cutword_array_str = json.dumps(all_cutword_array, indent=2, ensure_ascii=False)
    all_city_ans_str      = json.dumps(all_city_ans, indent=2, ensure_ascii=False)
    all_city_sort_str     = json.dumps(all_city_sort, indent=2, ensure_ascii=False)
    yibu_write( "all_cutword_array_str", all_cutword_array_str )
    yibu_write( "all_city_ans_str", all_city_ans_str )
    yibu_write( "all_city_sort", all_city_sort_str )




loadFload()
remake_city_ans()
dict_write()









