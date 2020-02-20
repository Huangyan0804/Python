import pytesseract
from PIL import Image
import time


def get_string(img):
    """识别图片的字符"""
    data = pytesseract.image_to_string(img, lang='chi_sim+eng', config='--psm 7')
    print(data)
    # return data


def get_step_string(img):
    data = pytesseract.image_to_string(img, lang='test', config='--psm 6')
    print(data)


def get_init_value(img):
    data = pytesseract.image_to_string(img, lang='test1', config='--psm 6')
    print(data)


def gray_img(img):
    """灰度化图片"""
    img_grey = img.convert("L")
    # img_grey.show()
    return img_grey


def two_img(img):
    """二值化图片"""
    img_two = img.point(lambda x: 255 if x < 120 else 0)
    # img_two.show()
    return img_two


def process_img(img, filename):
    """把图片有用的区域裁剪下来，分别处理"""
    # 步骤次数图像位置 (729, 112, 948, 190) 需要二值化
    move_time_img = img.crop((750, 126, 948, 190))
    move_time_img = two_img(gray_img(move_time_img))

    # 目标值位置 (521, 275, 966, 409) 需要二值化
    dest_value_img = img.crop((521, 275, 966, 409))
    dest_value_img = two_img(gray_img(dest_value_img))
    w = int(dest_value_img.size[0] * 3)
    h = int(dest_value_img.size[1] * 3)
    dest_value_img = dest_value_img.resize((w, h))

    # 初始值位置 (85, 479, 996, 817) 二值化
    init_value_img = img.crop((85, 479, 996, 817))
    init_value_img = two_img(gray_img(init_value_img))
    # w = int(init_value_img.size[0] * 0.5)
    # h = int(init_value_img.size[1] * 0.5)
    # init_value_img = init_value_img.resize((w, h))
    # init_value_img.show()

    # 按钮都需要灰度化
    # 按钮1位置 (393, 1226, 648, 1365)
    button_img1 = img.crop((393, 1226, 648, 1365))
    button_img1 = gray_img(button_img1)

    # 按钮2位置 (51, 1520, 308, 1660)
    button_img2 = img.crop((51, 1520, 308, 1660))
    button_img2 = gray_img(button_img2)

    # 按钮3位置 (392, 1516, 648, 1653)
    button_img3 = img.crop((392, 1516, 648, 1653))
    button_img3 = gray_img(button_img3)

    # 按钮4位置 (48, 1812, 300, 1948)
    button_img4 = img.crop((48, 1812, 300, 1948))
    button_img4 = gray_img(button_img4)

    # 按钮5位置 (394, 1809, 650, 1948)
    button_img5 = img.crop((394, 1809, 650, 1948))
    button_img5 = gray_img(button_img5)

    # button_img1.show()
    # button_img2.show()
    # button_img3.show()
    # button_img4.show()
    # button_img5.show()

    # move_time_img.save(filename + '-01.png')
    # dest_value_img.save(filename + '-02.png')
    # init_value_img.save(filename + '-03.png')
    # button_img1.save(filename + '-04.png')
    # button_img2.save(filename + '-05.png')
    # button_img3.save(filename + '-06.png')
    # button_img4.save(filename + '-07.png')
    # button_img5.save(filename + '-08.png')
    # img.show()
    # get_string(move_time_img)
    # get_value_string(dest_value_img)
    init_value_img.show()
    get_init_value(init_value_img)
    # get_string(button_img1)
    # get_string(button_img2)
    # get_string(button_img3)
    # get_string(button_img4)
    # get_string(button_img5)
    time.sleep(3)




def open_img(st, ed):
    for i in range(st, ed+1):
        img = Image.open(r'calculator2-images/%d.png' % i)
        filename = str(i)
        print(i, end=': ')
        process_img(img, filename)
        break


def main():
    # open_img(1, 12)
    # open_img(7, 30)
    # return
    for i in range(1, 2):
        img = Image.open('b-03.png')
        # img = img.crop((300, 40, 420, 95))
        w = int(img.size[0] * 3)
        h = int(img.size[1] * 3)
        img = img.resize((w, h))
        # img = gray_img(img)
        # img = two_img(img)

        img.show()
        print('%d-msg: ', end='')
        get_init_value(img)
        time.sleep(3)

    pass


if __name__ == '__main__':
    main()


"""

"""