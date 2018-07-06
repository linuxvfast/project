import pika
import uuid
import configparser
from conf import settings
import json
import paramiko
import threading
import random
import sys




class FibonacciRpcClient(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost',5672,'/',self.credentials))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        self.thread_list = []
        self.result_lit = {}
        self.complete = []

    def on_response(self, ch, method, props, body):
        while True:
            if self.corr_id == props.correlation_id:
                self.response = body
                body = body.decode()
                result = eval(body)
                # print('body', result)
                # print(type(result))
                if len(self.complete) == 0:
                    print('\033[31m没有结果\033[0m')
                else:
                    for i in self.complete:
                        print('\033[33m有结果的任务id列表\033[0m'.center(30,'-'))
                        print('task_id'+' '+str(i))
                        self.result_lit[str(i)].append(result[str(i)])
                        self.complete.remove(i)
                    if len(self.complete) == 0:
                        break


    def call(self,info):
        info =json.dumps(info)
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=info)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

    def distribution(self, cmd):
        '''分发函数功能'''
        # print('cmd',cmd)
        if len(cmd['check_task']) != 0:
            str = 'check_task'
        else:
            str = 'run'
        if hasattr(self, 'cmd_%s' % str):
            func = getattr(self, 'cmd_%s' % str)
            res = func(cmd)
            return res


    def help(self):
        '''帮助信息'''
        print('\033[32m命令操作如下\033[0m'.center(30, '-'))
        print('''run 'cmd' --hosts ip地址  ip地址2      #主机执行的命令' 
task_all                               #查看所有的id号
check_task  线程id号                   #根据线程查看命令执行结果''')

    def cmd_run(self,cmd):
        '''根据str分发功能，如果是run命令分发到cmd_exec,如果是checkout命令分发到cmd_checkout'''

        try:
            config = configparser.ConfigParser()
            config.read(settings.ACCOUNT_DIR)
            hosts = cmd['--hosts']
            cmds = cmd['run']
            # print(len(cmds))
            cmd_len = len(cmds) - 1
            command = ''

            for i in range(cmd_len):
                command += cmds[i] + ' ' + cmds[i + 1]
            # print(command)
            while True:
                for host in hosts:
                    tak_id = random.randint(1000, 99999)
                    host, port, username, password = host, \
                                                     config[host]['port'], \
                                                     config[host]['username'], \
                                                     config[host]['password']
                    run_dic = {
                        'host': host,
                        'cmd': command,
                        'port': port,
                        'username': username,
                        'password': password,
                        'pid':tak_id,
                    }
                    # print('run_dic',run_dic)
                    t = threading.Thread(target=self.call, args=(run_dic,))
                    t.start()
                    self.thread_list.append(tak_id)
                    self.result_lit[str(tak_id)]=[host,command]
                    hosts.remove(host)

                for i in self.thread_list:
                    # print(i)
                    self.complete.append(i)
                    self.thread_list.remove(i)
                if len(hosts) != 0:
                    continue
                else:
                    print('有的进程', self.complete)
                    break
        except IndexError as e:
            print("\33[31;0mError：%s\33[0m" % e)
        return True



    def cmd_check_task(self,cmd):
        '''根据id查询结果'''
        try:
            id = cmd['check_task'][0]
            # print('id',type(id))
            print('\033[33m任务id 【%s】 主机【%s】 命令【%s】 查询结果\033[0m'.center(50,'-')%\
                  (id,self.result_lit[id][0],self.result_lit[id][1]))
            print(self.result_lit[id][2])
            del self.result_lit[id]
            # self.thread_list.remove(id)
            self.interactive()
        except Exception as e:
            print('Error info:%s'%str(e))
        return True



    def interactive(self):
        while True:
            config = configparser.ConfigParser()
            config.read(settings.ACCOUNT_DIR)
            print('server list'.center(30, '-'))
            for keys,values in config.items():
                print(keys)
            print('\033[31m 请从上面的列表中选择操作的主机，否则无法运行\033[0m')
            cmd = input('执行命令>>').strip()
            print(cmd)
            if len(cmd) == 0: continue
            if cmd.startswith('run') and '--hosts' in cmd or cmd.startswith('check_task'):
                cmd_str = cmd.split(' ')
                print('cmd_str',cmd_str)
                tags = False
                sql_dic = {
                    "run":[],
                    "--hosts":[],
                    "check_task":[],
                }
                for line in cmd_str:
                    if tags and line in sql_dic:
                        tags = False
                    if not tags and line in sql_dic:
                        tags = True
                        key = line
                        continue
                    if tags:
                        sql_dic[key].append(line.strip("'"))
                res = self.distribution(sql_dic)
                if res == 'True':
                    continue
            else:
                print('invalid cmd...')
                self.help()
                continue






# if __name__ == '__main__':
#     st = FibonacciRpcClient()
#     st.interactive()