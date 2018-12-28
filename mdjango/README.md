# **mova_project**

>HITSZ SE group 10

---

### 实现功能

- 注册、登录

   密码密/明文显示，确认密码，4位数字验证码（可点击切换）
   
- 游客模式

   限制使用爬虫、图表整合下载、修改密码功能
   
- 数据更新

   注册用户登录后可启用爬虫，爬取时间约为20min，产品弹出提示框ok即为更新成功
   
- 数据可视化

   题材票房比例：柱状图（动态）、饼图（动态可交互）
   
   总票房趋势：折线图（动态可交互）
   
   电影票房TOP3/5/10: 柱状图（动态）、词云图（动态）
   
   劳模演员TOP3/5/10: 柱状图（动态）、词云图（动态）

- 图表整合下载

   数据可视化界面可单独下载
   
   注册用户登录后可整合下载最近一次生成的图表，整合下载保存为pdf格式至产品所在文件夹mdjango

### 实现技术

- 前端

   框架为Vue.js，组件采用elementUI，数据可视化采用EChanrts

- 后端

   框架为django，爬虫使用Scrapy框架+selenium模拟点击，数据库使用Sqlite3   

### 使用方法

- 环境依赖

   1. 本软件基于python 3，请保证您的PC中以有python 3环境

   2. 您需要下载npm，并且在命令行中使用 pip install 安装 scrapy、phantomjs、selenium、twisted、reportlab、PIL、pyecharts、sqlite3 函数包
  
   3. 必要时您还需要下载chromedriver并将其保存至您的PC的python路径下
   
- 使用步骤

  1. cd 至项目文件夹下 frontend 文件夹中，利用命令行 npm install 下载前端所需的包
  
  2. 返回至上一级文件夹，利用命令行 python3 manage.py runserver 启动服务端
  
  3. 前往浏览器，输入本地服务器 127.0.0.1:8000
  
  4. 开始体验MOVA带来的便利
