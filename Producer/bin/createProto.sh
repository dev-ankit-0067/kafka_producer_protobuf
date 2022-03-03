#/usr/bin/bash

#-------------------------------------------------------
# Purpose : Create Proto File for message structure
# Developer : Ankit Sharma
#-------------------------------------------------------

protoc -I=../protoFile --python_out=../module/ ../protoFile/transaction.proto