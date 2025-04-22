# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 20:49:39 2025

@author: hp
"""

import gym
import time

env = gym.make('CartPole-v1', render_mode = 'human')

#20 episode (deneme) boyunca oyunu çalıştır
for episode in range(1, 21):
    print(f"\n EPISODE {episode} BAŞLIYOR. . .")
    
    observation, info = env.reset()
    
    #maksimum 100 adıma kadar çalıştır
    for step in range(1, 101):
        env.render() #ortamı görselleştir
        print(f"\n Adım {step}: Güncel Gözlem Verileri -> {observation}")
        
        #Rastgele bir aksiyon seç (0 -> sola it, 1 -> sağa it)
        action = env.action_space.sample()
        print(f"Seçilen Aksiyon: {action} ({'Sola İt' if action == 0 else 'Sağa İt'})")

        #Seçilen aksiyonu uygula ve yeni gözlemi al
        observation, reward, terminated, truncated, info = env.step(action)

        print(f"Alınan ödül: {reward}")

        #Eğer episode bittiyse (kutunun dengesi bozulduysa) çık
        if terminated or truncated:
            print(f"EPISODE {episode} BİTTİ! {step} adımda sona erdi.\n")
            time.sleep(2)
            break
        
    print(f"EPISODE {episode} başarıyla tamamlandı!\n")
    time.sleep(0.05)

env.close()
print("\nTüm Episodelar Tamamlandı!")        
        
        
        
        
        
        
        
        
        