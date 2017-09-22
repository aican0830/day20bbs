#!/usr/bin/env python
# -*- coding:utf-8  -*-




data = [
    (None,'A'),
    ('A','A1'),
    ('A','A1-1'),
    ('A1','A2'),
    ('A1-1','A2-3'),
    ('A2-3','A3-4'),
    ('A1','A2-2'),
    ('A2','A3'),
    ('A2-2','A3-3'),
    ('A3','A4'),
    (None,'B'),
    ('B','B1'),
    ('B1','B2'),
    ('B1','B2-2'),
    ('B2','B3'),
    (None,'C'),
    ('C','C1'),

]


data_dic = {
    'A': {
        'A1': {
            'A2':{
                'A3':{
                    'A4':{}
                }
            },
            'A2-2':{
                'A3-3':{}
            }
        }
    },
    'B':{
        'B1':{
            'B2':{
                'B3':{}
            },
            'B2-2':{}
        }
    },
    'C':{
        'C1':{}
    }

}
def tree_search(d_dic,parent,son):
    for k,v_dic in d_dic.items():
        if k == parent:
            d_dic[k][son]={}
        else:
            tree_search(d_dic[k],parent,son)




data_dic = {}
for item in data:
    parent,son = item
    if parent is None:
        data_dic[son] = {}
    else:
        tree_search()