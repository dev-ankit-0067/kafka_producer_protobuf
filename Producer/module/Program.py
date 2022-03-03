#!/usr/bin/env python3

#----------------------------------------------------------------------------
# Purpose : Main Program
# 
# Developer : Ankit Sharma
#-----------------------------------------------------------------------------


import os
import click
from Record import Record 
from Producer import Producer
from Sample import Sample
import logging


@click.command()
@click.option('--numoftrans','--n',help='Number of Transactions to be Generate',default=1000)

def program(numoftrans):
  logging.basicConfig(filename="../logs/program.log",level=logging.INFO)
  try:
    rec = Record()
    kp = Producer()
    trans = Sample()
    for num in range(1,numoftrans):
      message = trans.getTransaction()
      record = rec.getRecord(message)
      kp.sendRecord(10,record)

  except Exception as e:
      logging.ERROR(f"Error occuerd {e}")

if __name__ == '__main__':
    program()