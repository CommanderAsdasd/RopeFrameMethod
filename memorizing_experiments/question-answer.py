# -*- coding: UTF-8 -*-

import random

czech_list = [("Гласные верхнего подъёма" , "ɪ	iː	u	uː"), 
            ("Гласные верхнего подъёма" , "ɪ	iː	u	uː"),
            ("Союз", "konjunkce/spojka")]

code = [("NVGlineCap", """NVG_BUTT,
                        NVG_ROUND,
                        NVG_SQUARE,
                        NVG_BEVEL,
                        NVG_MITER,""")]

showing_card = random.choice(czech_list)
print(showing_card[0])
input(" ")
# stop = input()
print(showing_card[1])
print("How good you remember that?")
# print(mark)