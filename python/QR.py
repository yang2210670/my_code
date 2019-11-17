from MyQR import myqr
import os
import time


def QR(url,photo):
    myqr.run(
        words = url,
        picture = photo,
        colorized=True,
    )

def main():
    url = input("请输入链接：")
    photo = input("请输入背景图片路径：")
    print("正在制作，请稍等...")
    QR(url,photo)
    print("制作完成,程序3秒后退出！")
    print("二维码保存目录：",os.getcwd())
    time.sleep(3)
if __name__ == "__main__":
    main()