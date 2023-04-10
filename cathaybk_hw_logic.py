def hw_logic_source(source):
    for i in source.copy():
        next_source = (source[i] // 5 + 1) * 5
        if (next_source - source[i] <= 3) and (next_source >= 40):
            source[i] = next_source

    for k, v in source.items():
        print(k + ':', v)

def hw_logic_hight(height):
    total_height = -100
    for i in range(0, 10):
        total_height += height * 2
        height /= 2

    print("總共", total_height)
    print("第十次", height)

# HW_logic 1
source = {'Derek':33, 'Shawn': 73, 'Jeff': 63, 'Maki': 39}
hw_logic_source(source)

# HW_logic 2
hight = 100
hw_logic_hight(hight)
