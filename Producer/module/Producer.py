#!/usr/bin/env python3

#----------------------------------------------------------------------------
# Purpose : Main Program
# 
# Developer : Ankit Sharma
#-----------------------------------------------------------------------------

from kafka import KafkaProducer

class Producer(object):
    ''' Produce Message to Kafka Topic '''

    def __init__(self):
       pass

    def sendRecord(self,client,msg):
        ''' send record to Kafka '''
        try:
          producer = KafkaProducer(bootstrap_servers=["localhost:9092"],retries=2,acks=1,compression_type='lz4')
          g = producer.send('transaction',msg)
          producer.flush()
          producer.close()
        except Exception as e:
          ''' Can be send to error topic with exception.'''
          raise (e)
