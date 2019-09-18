import requests
import os.path as op
import os
from sys import stdout
import time

def downloadfile(url, filename):
    filename = filename.split(" ")[0] + op.splitext(url)[-1]
    file_to_save = op.join(os.getcwd(), filename)
    headers = {'user-agent': 'Mozilla/5.0'}

    with open(file_to_save, "wb") as fw:
        with requests.get(url,headers = headers,stream=True) as r:
            # 此时只有响应头被下载
            # print(r.headers)
            print("下载文件基本信息:")
            print('-' * 30)
            print("文件名称:", filename)
            print("文件类型:", r.headers["Content-Type"])
            filesize = r.headers["Content-Length"]
            length = float(r.headers['content-length'])
            print("文件大小:", format(int(r.headers['Content-Length'])/1048576,".2f") + " Mb")
            print("下载地址:", url)
            print("保存路径:", file_to_save)
            print('-' * 30)
            print("下载进度:")
            chunk_size = 1048576

            if filesize is None:
                fw.write(r.content)
            else:
                dl = 0
                total_length = int(filesize)
                t1 = time.time()
                for data in r.iter_content(chunk_size):
                    dl += len(data)
                    show = dl / total_length
                    fw.write(data)
                    t2 = time.time()
                    t = t2-t1
                    speed = dl / 1024 / 1024 / t
                    done = int(50 * dl / total_length)
                    stdout.write("\r[%s%s]%.2f%%  %.2f%s" % ('█' * done, ' ' * (50 - done),show * 100,speed,"M/S"))
                    stdout.flush()

            print('')
            print('下载完成：%s' % filename)


if __name__ == "__main__":
    url = "https://codeload.github.com/godweiyang/hexo-matery-modified/zip/master"
    downloadfile(url, "a")