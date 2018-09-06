# -*- coding: utf-8 -*-

import logging
import sys
import time
from PyMdApi import *
from PyMdApiData import *

def getTime():
    return time.asctime(time.localtime(time.time()))

if __name__ == '__main__':
    handler = PyMdApi()


    print "\n"
    print "=============(%s) call HzTDFSrvApi_Connect begin ==========="%getTime()
    ret = handler.HzTDFSrvApi_Connect()
    print "HzTDFSrvApi_Connect return value: %s"%(ret)
    print "=============(%s) call HzTDFSrvApi_Connect end ============="%getTime()

    print "\n"
    print "=============(%s) call HzTDFSrvApi_Subscribe begin ==========="%getTime()
    ret = handler.HzTDFSrvApi_Subscribe("")
    print "HzTDFSrvApi_Subscribe return value: %s"%(ret)
    print "=============(%s) call HzTDFSrvApi_Subscribe end ============="%getTime()

    # #print "Running python script"
    # str = raw_input("press any key to start test GetLatestStockQuote, GetLatestIndexQuote, GetLatestFutureQuote\n")
    # #str = raw_input("Enter your input: ")
    # print str

	###################### 主动获取接口已废弃 #####################################
    # print "\n"
    # print "=============(%s) call GetLatestStockQuote begin ==========="%getTime()
    # windCode = "600000.SH"
    # ret = handler.GetLatestStockQuote(windCode)
    # print "GetLatestStockQuote return value: %s"%(ret)
    # print "=============(%s) call GetLatestStockQuote end ============="%getTime()

    # print "\n"
    # print "=============(%s) call GetLatestIndexQuote begin ==========="%getTime()
    # windCode = "600000.SH"
    # ret = handler.GetLatestIndexQuote(windCode)
    # print "GetLatestIndexQuote return value: %s"%(ret)
    # print "=============(%s) call GetLatestIndexQuote end ============="%getTime()

    # print "\n"
    # print "=============(%s) call GetLatestFutureQuote begin ==========="%getTime()
    # windCode = "600000.SH"
    # ret = handler.GetLatestFutureQuote(windCode)
    # print "GetLatestStockQuote return value: %s"%(ret)
    # print "=============(%s) call GetLatestFutureQuote end ============="%getTime()

    ###################### 这两个接口已废弃 #####################################
    #print "Running python script"
    #str = raw_input("press any key to start test GetLatestQuote\n")
    #str = raw_input("Enter your input: ")
    #print str

    #print "\n"
    #print "=============(%s) call GetLatestQuote begin ==========="%getTime()
    #windCode = "600000.SH"
    #dataType = 1
    #ret = handler.GetLatestQuote(windCode, dataType)
    #print "GetLatestQuote return value:",ret
    #print "=============(%s) call GetLatestQuote end ============="%getTime()

    #print "\n"
    #print "=============(%s) call GetLatestQuotes begin ==========="%getTime()
    #ret = handler.GetLatestQuotes(200)
    #print "GetLatestQuotes return value: %s"%(ret)
    #print "=============(%s) call GetLatestQuotes end ============="%getTime()

	#wait a second for data comming
    #print "Running python script"
    str = raw_input("press any key to start test callback\n")

    print "\n"
    print "=============(%s) call SetStockQuoteCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(StockQuote)
    def FUNPY_StockQuoteCallback(data):
        print "in FUNPY_StockQuoteCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetStockQuoteCallback(FUNPY_StockQuoteCallback)
    print "SetStockQuoteCallback return value: %s"%(ret)
    print "=============(%s) call SetStockQuoteCallback end ============="%getTime()


    print "\n"
    print "=============(%s) call SetIndexQuoteCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(IndexQuote)
    def FUNPY_IndexQuoteCallback(data):
        print "in FUNPY_IndexQuoteCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetIndexQuoteCallback(FUNPY_IndexQuoteCallback)
    print "SetIndexQuoteCallback return value: %s"%(ret)
    print "=============(%s) call SetIndexQuoteCallback end ============="%getTime()


    print "\n"
    print "=============(%s) call SetFutureQuoteCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(FutureQuote)
    def FUNPY_FutureQuoteCallback(data):
        print "in FUNPY_FutureQuoteCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetFutureQuoteCallback(FUNPY_FutureQuoteCallback)
    print "SetFutureQuoteCallback return value: %s"%(ret)
    print "=============(%s) call SetFutureQuoteCallback end ============="%getTime()


    print "\n"
    print "=============(%s) call SetTransactionCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(Transaction)
    def FUNPY_TransactionCallback(data):
        print "in FUNPY_TransactionCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetTransactionCallback(FUNPY_TransactionCallback)
    print "SetTransactionCallback return value: %s"%(ret)
    print "=============(%s) call SetTransactionCallback end ============="%getTime()


    print "\n"
    print "=============(%s) call SetOrderCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(Order)
    def FUNPY_OrderCallback(data):
        print "in FUNPY_OrderCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetOrderCallback(FUNPY_OrderCallback)
    print "SetOrderCallback return value: %s"%(ret)
    print "=============(%s) call SetOrderCallback end ============="%getTime()


    print "\n"
    print "=============(%s) call SetOrderQueueCallback begin ==========="%getTime()
    #定义回调函数
    #回调参数类型：pointer(OrderQueue)
    def FUNPY_OrderQueueCallback(data):
        print "in FUNPY_OrderQueueCallback"
        print "parameter:%s"%data
    #设置回调函数
    ret = handler.SetOrderQueueCallback(FUNPY_OrderQueueCallback)
    print "SetOrderQueueCallback return value: %s"%(ret)
    print "=============(%s) call SetOrderQueueCallback end ============="%getTime()

    
    #print "Running python script"
    s = raw_input(">\n")
    #str = raw_input("Enter your input: ")
    print str


    print "\n"
    print "=============(%s) call HzTDFSrvApi_UnSubscribe begin ==========="%getTime()
    ret = handler.HzTDFSrvApi_UnSubscribe("")
    print "HzTDFSrvApi_UnSubscribe return value: %s"%(ret)
    print "=============(%s) call HzTDFSrvApi_UnSubscribe end ============="%getTime()

    print "\n"
    print "=============(%s) call HzTDFSrvApi_Dispose begin ==========="%getTime()
    handler.HzTDFSrvApi_Dispose()
    print "=============(%s) call HzTDFSrvApi_Dispose end ============="%getTime()
