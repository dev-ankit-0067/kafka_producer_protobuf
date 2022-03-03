#!/usr/bin/env python3

#----------------------------------------------------------------------------
# Purpose : This code will convert a json message to protobuf format. 
#           Encode it with base64 encoding and return a record
# 
# Developer : Ankit Sharma
#-----------------------------------------------------------------------------


import json
import base64
import transaction_pb2 as tp
from google.protobuf import json_format as jf
from google.protobuf import message as ap

class Record(object):
  ''' Convet input record to protobuf format '''

  def __init__(self):
     self._tran = tp.Transaction()

  def getRecord(self,message):
    ''' Set record to protpbuf format '''

    msg = jf.Parse(json.dumps(message),self._tran)
    record = jf.base64.b64encode(msg.SerializeToString())
    return record

