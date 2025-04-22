# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 20:23:38 2025

@author: hp
"""

import gym
import time

env = gym.make('CartPole-v1', render_mode = 'human')

#Ortamı başlat
env.reset()

for _ in range(1000):
    env.render() #Ortamı görselleştir
    env.step(env.action_space.sample()) #Rastgele bir aksiyonu uygula
    time.sleep(0.05) #her adımda 50 ms bekle (hızı düşür)
    
env.close()