# py_study

## 我的python学习记录
#### mydload下载器

传入url,文件名即可下载
```python
from mydload import downloadfile
downloadfile(url,filename)
```
#### 抖音视频下载

+ douyin1.py（已经失效）

传入分享链接即可+

+ douyin2.py(目前可用)

    使用方法：

    1.直接引用上方源码，运行即可

    2.安装

    ```python
    pip3 install ddouyin
    ```

    然后在你的代码里这样使用：

    ```python
    from ddouyin import douyin
    douyin("你复制的抖音分享链接")
    ```

    

#### 必应壁纸爬虫

相关信息见源码