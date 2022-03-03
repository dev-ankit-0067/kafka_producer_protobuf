#!/usr/bin/env python3

#----------------------------------------------------------------------------
# Purpose : This code will convert a json message to protobuf format. 
#           Encode it with base64 encoding and return a record
# 
# Developer : Ankit Sharma
#-----------------------------------------------------------------------------

import pendulum
import random

class Sample(object):
  ''' To Create Sample Records '''

  def __init__(self):
      pass

  def getTransaction(self):
    ''' Returns a dummy message '''
    try: 
      timstamp = pendulum.now().format("YYYY-MM-DDTHH:mm:ss.SSSZ")
      num = random.randint(1,20)
      tranRandom = random.randint(1,1000)
      amt = round(random.uniform(1,1000),2)

      message = {
        "transaction_id":f"{num}",
        "account_number":f"acct_{num}",
        "transaction_referance":f"AT{tranRandom}",
        "transaction_datetime":timstamp,
        "amount": amt
      } 

      return message
      
    except Exception as e:
      raise e
