django_for_blog_systerm
##在部署django时踩的坑 uwsgi + nginx 部署django应用

最初在本地环境开发好django后 利用git克隆到了云主机上。

- 然后网上好多的部署教程 最后在知乎找到了俩比较靠谱的
- http://www.chenxm.cc/post/275.html#1
- http://www.cnblogs.com/jhao/p/6071790.html

####先说数据库(mysql5.7配置utf8）
- 在本地上传github上的时候，不小心点了编译器的版本回退（jetbrins这个编译器真心好用啊），在部署时发现用的数据库是sqlite3。之后在服务器里用vim硬敲了django的setting，改为了mysql数据库。运行之后发现我的后台不可以插入中文。根据报错信息时字符编码的问题，所以想到了以下2点：
	

	1.django在数据传送时编码问题
	2.mysql编码不对

解决：

- 我第一步是先排除数据库，因为在使用python时产生过许多的编码问题，所以这一步留往后解决。
- mysql -u root -p ;输入密码后，进入数据库，输入 show variables like "%character%"; 发现有两个文件的编码是binry。于是乎，就在网上找教程。之间又踩了许多坑。


	网上大部分的mysql版本是5.6的，配置文件根本不一样（不是网上有人说的不同电脑的配置文件不一样）而自从某年某月以后 ubantu 用命令安装的mysql就已经时5.7版本了(安装时未选定版本)。so，修改配置文件，5.7版本配置文件位于 /etc/mysql/mysql.conf.d/mysqld.cnf 下，
	

	1.使用命令 vim /etc/mysql/mysql.conf.d/mysqld.cnf
	2.键盘按 i 才能够对文件进行插入
	3.找到 [mysqld] ，在  [mysqld] 的最后一行插入 character-set-server=utf8
	4.按 ESC 后 在按 ：输入wq 退出保存
	5.重启mysql sudo systemctl restart mysql
	6.再次确认编码 （进入mysql 输入show variables like "%character%";)
	注意：django原来创建的数据表要把它删除掉，不然还是不能够插入中文

##配置uwsgi（官方文档 http://projects.unbit.it/uwsgi/wiki/Doc）
	
- uwsgi作用是对各个project分别生成监听进程，然后和http服务互动。
- uWSGI的主要特点如下：


		◆超快的性能。

		◆低内存占用（实测为apache2的mod_wsgi的一半左右）。

		◆多app管理。

		◆详尽的日志功能（可以用来分析app性能和瓶颈）。

		◆高度可定制（内存大小限制，服务一定次数后重启等）。

	配置过程：

		1.pip install uwsgi

		2.查看版本 uwsgi --version 我的版本是 2.0.15

		3.编写一个简单的wsgi应用测试uwsgi是否能正常使用
        	首先创建一个test.py文件(命令：vim test.py)
```
		# test.py
		def application(env, start_response):
		    start_response('200 OK', [('Content-Type','text/html')])
		    return [b"Hello World"] # python3
		    #return ["Hello World"] # python2
```
		4.uwsgi --http :8000 --wsgi-file test.py
		意思是监听来自 8000端口的 http请求， 运行test.py来处理它
		访问你云服务器的ip地址 like this: 0.0.0.0:8000,查看test.py是否运行

		5.进行项目测试（我的django位置 /home/personl_blog/personl_blog) 命令如下：

uwsgi --http :8000 --chdir /home/personl_blog/ -w personl_blog.wsgi --static-map=/static=static

        6.创建uwsgi文件
        在 home/personl_blog/ 下创建一个script文件夹（mkdir script）,然后vim uwsgi.ini 输入以下配置

        [uwsgi]
        # 项目目录
        chdir=/home/personl_blog/personl_blog/
        # 指定项目的application
        module=personl_blog.wsgi:application
        # 进程个数
        workers=5
        pidfile=/home/personl_blog/script/uwsgi.pid
        # 指定IP端口
        http=192.168.31.123:8000
        #或者 http= ：8000
        # 指定静态文件
        static-map=/static=/home/personl_blog/static
        # 启动uwsgi的用户名和用户组
        uid=root
        gid=root
        # 启用主进程
        master=true
        # 自动移除unix Socket和pid文件当服务停止的时候
        vacuum=true
        # 序列化接受的内容，如果可能的话
        thunder-lock=true
        # 启用线程
        enable-threads=true
        # 设置自中断时间
        harakiri=30
        # 设置缓冲
        post-buffering=4096
        # 设置日志目录
        daemonize=/home/personl_bloh/script/uwsgi.log
        # 指定sock的文件路径
        socket=/home/personl_blog//script/uwsgi.sock

        输入完后 先esc再 ：wq保存退出

        6.启动配置文件
```
        $ uwsgi --ini uwsgi.ini   # 启动uwsgi配置
        [uwsgi-static] added mapping for /static => /home/personl_blog/static    # 启动成功


        $ uwsgi --stop uwsgi.pid  # 关闭uwsgi
        signal_pidfile()/kill(): Operation not permitted [core/uwsgi.c line 1659]
```
        至此你的django已经部署成功了，如果你用的是阿里云的服务器 记得把安全组规则配置一下开放你在上面所设置的端口。
        如果你想要服务器更加稳定 那么请继续看下文配置nginx

###nginx的安装配置

- 1.安装

```
sudo apt-get install nginx  #安装
```

2.检查nginx是否启动成功
```
$ ps -ef |grep -i nginx
root       6961      1  0 03:56 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data   6962   6961  0 03:56 ?        00:00:00 nginx: worker process
pala       6985   2090  0 03:57 pts/0    00:00:00 grep --color=auto -i nginx
```
在浏览器输入 你的ip地址查看nginx是否打开

3.Nginx常用命令
```
$ /etc/init.d/nginx start  #启动
$ /etc/init.d/nginx stop  #关闭
$ /etc/init.d/nginx restart  #重启
```

4.nginx默认会读取/etc/nginx/sites-enabled/default文件中的配置，修改其配置如下:（在最后加入）
```
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name 47.93.218.156; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
   # location /media  {
    #    alias /home/ubuntu/blog/media;  # your Django project's media files - amend as required
   # }我没有视频文件所以注释了

    location /static {
        alias /home/personl_blog/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        include     uwsgi_params; # the uwsgi_params file you installed
        uwsgi_connect_timeout 30;
        uwsgi_pass unix:/home/personl_blog/script/uwsgi.sock;
    }
}
```
5.重启nginx
```
$ /etc/init.d/nginx restart  #重启
```
###题外话
- 其实配置服务器的时候前前后后踩了许多坑所以才想把这个分享出来，
- 还有 如果你修改过了你的django的views 或 models 你需要重启一下 uwsgi，因为你的uwsgi还是在运行上一个版本的django
- 修改过静态文件（js/css）时可以不修改，因为你的静态文件是交给nginx处理的，如果出错的话再重启吧 我也没踩过这个坑


 如果需要的可以联系我 qq 541573560

