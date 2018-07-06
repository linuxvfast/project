rpc批量执行命令
http://www.cnblogs.com/alex3714/articles/5248247.html
select 或者selectors版ftp

目录结构

rpc_client
    -bin 
	    -start.py   程序入口
	-conf 
        -account.cfg  服务器登录信息
        -settings.py  设置信息
    -core
        -client.py    客户端代码

		

rpc_server
    -conf
	    -server.py   服务端启动程序
		

#只能是单个机器返回结果，没有实现多服务器返回结果
