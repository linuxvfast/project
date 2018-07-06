#-*- encoding:utf-8 -*-
import pika
import os,sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,BASE_DIR)
import paramiko
import threading
import configparser
from conf import settings
import json

class RPCServer(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost',5672,'/',self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')
        self.result_list = {}

    def cmd_exec(self,run_dic):
        '''执行命令返回结果'''
        # while True:
        print('dic', run_dic)
        run_dic = json.loads(run_dic)
        # print(type(run_dic))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # print(run_dic['pid'])
        # print(run_dic['host'], run_dic['port'], run_dic['username'], run_dic['password'])
        ssh.connect(hostname=run_dic['host'], \
                    port=run_dic['port'], \
                    username=run_dic['username'], \
                    password=run_dic['password'])
        stdin, stdout, stderr = ssh.exec_command(run_dic['cmd'])
        res, err = stdout.read(), stderr.read()
        result = res if res else err

        result = str(result,encoding='utf8')
        print(result)

        self.result_list[str(run_dic['pid'])] = result
        # run_dic['pid'] = ''
        # print('pid',run_dic['pid'])
        ssh.close()
        print(self.result_list)
        return self.result_list

    def on_request(self,ch, method, props, body):
        # print('body',body)
        response = self.cmd_exec(body)
        response = str(response)
        print(type(response))
        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id= \
                                                             props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def run_server(self):
        self.channel.basic_consume(self.on_request, queue='rpc_queue')
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()

if __name__ == '__main__':
    while True:
        server = RPCServer()
        server.run_server()