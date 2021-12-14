import redis
import json
import os
from time import sleep
from random import randint

if __name__== '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')       
    redis_port = os.getenv('REDIS_PORT', '6379')
    redis_fila = os.getenv('REDIS_FILA', '0')

    r = redis.Redis(host=redis_host, port=REDIS_PORT, db=REDIS_FILA)
    print('Aguardando recebimento de mensaens...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        #simulando envio de email
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem', mensagem['assunto'], 'enviada')