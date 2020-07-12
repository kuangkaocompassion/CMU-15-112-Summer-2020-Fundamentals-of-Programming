rgb_v1 = 220020060

r_v1 = rgb_v1/1000000
g_v1 = (rgb_v1%1000000)/1000
b_v1 = (rgb_v1%1000000)%1000

print(r_v1, g_v1, b_v1)