### 一. pip安装环境
> pip install pandas curl_cffi openpyxl tqdm

### 二. 将源文件放到项目根目录下
> 网址链接.xlsx

### 三. 修改配置文件settings.py

1. PROXIES 设置代理，没有代理的话置空
2. FOLDER_NAME 修改结果的存储目录（一级文件夹的名字）

> 其他设置保持默认即可

### 四. 使用方法

直接运行main.py即可，程序内部自动处理以下逻辑

1. 正常全量采集
2. 全量采集后自动检测遗漏评论并回采

### 五. 手动补采

直接运行main.py即可

### 六. 更新项目最新评论

从success.txt中，删除对应项目的链接，然后直接运行main.py即可