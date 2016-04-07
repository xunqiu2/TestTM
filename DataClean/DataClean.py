#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/6 下午6:58
# @Author  : ZHZ

import pandas as pd
import numpy as np


#读取数据,columns默认为空
songs = pd.read_csv("mars_tianchi_songs.csv",header=None)
actions = pd.read_csv("mars_tianchi_user_actions.csv",header=None)

#重命名列名
songs.columns = ['song_id','artist_id','publish_time','song_init_plays','Language','Gender']
actions.columns = ['user_id','song_id','gmt_create','action_type','Ds']


#
users_value_counts = actions.user_id.value_counts()
action1 = actions[actions['action_type']==1]
action2 = actions[actions['action_type']==2]
action3 = actions[actions['action_type']==3]

