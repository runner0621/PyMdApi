# -*- coding: utf-8 -*-

#import called
import os
import sys
import types
from cffi import FFI
from PyMdApiData import *

#config DLLs path
dll_path = os.getcwd()

#config MdApi.dll path
mdapi_dll_path = '%s/MdApi.dll'%(dll_path)
sys.path.insert(0, dll_path)

DEG = True

class PyMdApi:

    def __init__(self):
        self.ffi = FFI()
        self.dll_handler = self.ffi.dlopen(mdapi_dll_path)
        self.ffi.cdef("""
            enum DataType
            {
                eDataBase = 0,
                eStockQuote = 1,
                eFutureQuote = 2,
                eIndexQuote = 3,
                eTransaction = 4,
                eOrder = 5,
                eOrderQueue = 6
            };

            struct DataBase
            {
                char szWindCode[32];
                enum DataType eType;
                void* quote;
            };

            struct StockQuote
            {
                char  szWindCode[32];
                char  szCode[32];
                int         nActionDay;
                int         nTradingDay;
                int      nTime;
                int      nStatus;
                unsigned int nPreClose;
                unsigned int nOpen;
                unsigned int nHigh;
                unsigned int nLow;
                unsigned int nMatch;
              
                unsigned int nAskPrice[10];
                unsigned int nAskVol[10];
                unsigned int nBidPrice[10];
                unsigned int nBidVol[10];
                unsigned int nNumTrades;
                long long    iVolume;
                long long    iTurnover;
                long long    nTotalBidVol;
                long long    nTotalAskVol;
              
                unsigned int nWeightedAvgBidPrice;
                unsigned int nWeightedAvgAskPrice;
                int      nIOPV;
                int      nYieldToMaturity;
                unsigned int nHighLimited;
                unsigned int nLowLimited;
                char     chPrefix[4];
                int      nSyl1;
                int      nSyl2;
                int      nSD2;
            };

            struct FutureQuote
            {
                char  szWindCode[32];
                char  szCode[32];
                int          nActionDay;
                int          nTradingDay;
                int      nTime;
                int      nStatus;
                long long  iPreOpenInterest;
                unsigned int nPreClose;
                unsigned int nPreSettlePrice;
                unsigned int nOpen;
                unsigned int nHigh;
                unsigned int nLow;
                unsigned int nMatch;
                long long  iVolume;
                long long  iTurnover;
                long long  iOpenInterest;
                unsigned int nClose;
                unsigned int nSettlePrice;
                unsigned int nHighLimited;
                unsigned int nLowLimited;
                int      nPreDelta;
                int      nCurrDelta;
                unsigned int nAskPrice[5];
                unsigned int nAskVol[5];
                unsigned int nBidPrice[5];
                unsigned int nBidVol[5];
                
                int     lAuctionPrice;
                int     lAuctionQty;
                int     lAvgPrice;
            };
            struct IndexQuote
            {
                char  szWindCode[32];
                char  szCode[32];
                int         nActionDay;
                int         nTradingDay;
                int         nTime;
                int       nOpenIndex;
                int       nHighIndex;
                int       nLowIndex;
                int       nLastIndex;
                long long iTotalVolume;
                long long iTurnover;
                int       nPreCloseIndex;
            };
            struct Transaction
            {
                char  szWindCode[32];
                char  szCode[32];
                int     nActionDay;
                int   nTime;
                int   nIndex;
                int   nPrice;
                int   nVolume;
                int   nTurnover;
                int     nBSFlag;
                char    chOrderKind;
                char    chFunctionCode;
                int     nAskOrder;
                int     nBidOrder;
            };
            struct Order
            {
                char  szWindCode[32];
                char  szCode[32];
                int   nActionDay;
                int   nTime;
                int   nOrder;
                int   nPrice;
                int   nVolume;
                char    chOrderKind;
                char    chFunctionCode;
            };
            struct OrderQueue
            {
                char  szWindCode[32];
                char  szCode[32];
                int     nActionDay;
                int   nTime;
                int     nSide;
                int   nPrice;
                int   nOrders;
                int   nABItems;
                int   nABVolume[200];
            };

            int HzTDFSrvApi_Connect(void);
            void HzTDFSrvApi_Dispose(void);

            int HzTDFSrvApi_Subscribe(const char* sub);
            int HzTDFSrvApi_UnSubscribe(const char* sub);
			
            typedef void (*StockQuoteCallback)(struct StockQuote*);
            typedef void (*IndexQuoteCallback)(struct IndexQuote*);
            typedef void (*FutureQuoteCallback)(struct FutureQuote*);
			typedef void (*TransactionCallback)(struct Transaction*);
			typedef void (*OrderCallback)(struct Order*);
			typedef void (*OrderQueueCallback)(struct OrderQueue*);
			
            void SetStockQuoteCallback(StockQuoteCallback cb);
            void SetIndexQuoteCallback(IndexQuoteCallback cb);
            void SetFutureQuoteCallback(FutureQuoteCallback cb);
			void SetTransactionCallback(TransactionCallback cb);
			void SetOrderCallback(OrderCallback cb);
			void SetOrderQueueCallback(OrderQueueCallback cb);
        """)


    ####################登录接口####################
    #0:失败，1：成功
    def HzTDFSrvApi_Connect(self):
        return self.dll_handler.HzTDFSrvApi_Connect()

    ####################退出接口####################
    #0:失败，1：成功
    def HzTDFSrvApi_Dispose(self):
        self.dll_handler.HzTDFSrvApi_Dispose()

    ####################订阅接口####################
    #默认无订阅，必须订阅后才有数据传输，HzTDFSrvApi_Subscribe("")表示全订阅
    #必需在Connect成功后订阅
    #0:失败，1：成功
    def HzTDFSrvApi_Subscribe(self, charStr):
        return self.dll_handler.HzTDFSrvApi_Subscribe(charStr)

    ####################取消订阅接口####################
    #0:失败，1：成功
    def HzTDFSrvApi_UnSubscribe(self, charStr):
        return self.dll_handler.HzTDFSrvApi_UnSubscribe(charStr)

    ####################设置回调接口####################
    #参数类型必须是：StockQuoteCallback
    def SetStockQuoteCallback(self, callback):
        #Check parameter data type
        self.stockQuoteCallback = self.ffi.callback("void (*StockQuoteCallback)(struct StockQuote* )", callback)
        self.dll_handler.SetStockQuoteCallback(self.stockQuoteCallback)


    ####################设置回调接口####################
    #参数类型必须是：IndexQuoteCallback
    def SetIndexQuoteCallback(self, callback):
        #Check parameter data type
        self.indexQuoteCallback = self.ffi.callback("void (*IndexQuoteCallback)(struct IndexQuote*)", callback)
        self.dll_handler.SetIndexQuoteCallback(self.indexQuoteCallback)

    ####################设置回调接口####################
    #参数类型必须是：FutureQuoteCallback
    def SetFutureQuoteCallback(self, callback):
        #Check parameter data type
        self.futureQuoteCallback = self.ffi.callback("void (*FutureQuoteCallback)(struct FutureQuote*)", callback)
        self.dll_handler.SetFutureQuoteCallback(self.futureQuoteCallback)
		
	####################设置回调接口####################
    #参数类型必须是：FutureQuoteCallback
    def SetTransactionCallback(self, callback):
        #Check parameter data type
        self.transactionCallback = self.ffi.callback("void (*TransactionCallback)(struct Transaction*)", callback)
        self.dll_handler.SetTransactionCallback(self.transactionCallback)
		
	####################设置回调接口####################
    #参数类型必须是：OrderCallback
    def SetOrderCallback(self, callback):
        #Check parameter data type
        self.orderCallback = self.ffi.callback("void (*OrderCallback)(struct Order*)", callback)
        self.dll_handler.SetOrderCallback(self.orderCallback)
		
	####################设置回调接口####################
    #参数类型必须是：OrderQueueCallback
    def SetOrderQueueCallback(self, callback):
        #Check parameter data type
        self.orderQueueCallback = self.ffi.callback("void (*OrderQueueCallback)(struct OrderQueue*)", callback)
        self.dll_handler.SetOrderQueueCallback(self.orderQueueCallback)

    # ####################获取股票最新行情接口####################
    # #0:失败，1：成功
    # #返回值：StockQuote指针
    # def GetLatestStockQuote(self, szWindCode):
				# cData = self.ffi.new("struct StockQuote[]", 1)
				# for i in range(0, min(len(cData[0].szWindCode), len(szWindCode))):
				    # cData[0].szWindCode[i] = szWindCode[i]
				# self.dll_handler.GetLatestStockQuote(cData)

				# pyData = StockQuote();

				# #copy data
				# char_buf_len = len(cData[0].szWindCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szWindCode[i] = ord((cData[0].szWindCode)[i])

				# char_buf_len = len(cData[0].szCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szCode[i] = ord((cData[0].szCode)[i])

				# pyData.nActionDay = cData[0].nActionDay
				# pyData.nTradingDay = cData[0].nTradingDay
				# pyData.nTime = cData[0].nTime
				# pyData.nStatus = cData[0].nStatus
				# pyData.nPreClose = cData[0].nPreClose
				# pyData.nOpen = cData[0].nOpen
				# pyData.nHigh = cData[0].nHigh
				# pyData.nLow = cData[0].nLow
				# pyData.nMatch = cData[0].nMatch

				# char_buf_len = len(cData[0].nAskPrice)
				# for i in range(0, char_buf_len-1):
						# pyData.nAskPrice[i] = (cData[0].nAskPrice)[i]

				# char_buf_len = len(cData[0].nAskVol)
				# for i in range(0, char_buf_len-1):
						# pyData.nAskVol[i] = (cData[0].nAskVol)[i]

				# char_buf_len = len(cData[0].nBidPrice)
				# for i in range(0, char_buf_len-1):
						# pyData.nBidPrice[i] = (cData[0].nBidPrice)[i]

				# char_buf_len = len(cData[0].nBidVol)
				# for i in range(0, char_buf_len-1):
						# pyData.nBidVol[i] = (cData[0].nBidVol)[i]

				# pyData.nNumTrades = cData[0].nNumTrades
				# pyData.iVolume = cData[0].iVolume
				# pyData.iTurnover = cData[0].iTurnover
				# pyData.nTotalBidVol = cData[0].nTotalBidVol
				# pyData.nTotalAskVol = cData[0].nTotalAskVol
				# pyData.nWeightedAvgBidPrice = cData[0].nWeightedAvgBidPrice
				# pyData.nWeightedAvgAskPrice = cData[0].nWeightedAvgAskPrice
				# pyData.nIOPV = cData[0].nIOPV
				# pyData.nYieldToMaturity = cData[0].nYieldToMaturity
				# pyData.nHighLimited = cData[0].nHighLimited
				# pyData.nLowLimited = cData[0].nLowLimited

				# char_buf_len = len(cData[0].chPrefix)
				# for i in range(0, char_buf_len-1):
						# pyData.chPrefix[i] = ord((cData[0].chPrefix)[i])

				# pyData.nSyl1 = cData[0].nSyl1
				# pyData.nSyl2 = cData[0].nSyl2
				# pyData.nSD2 = cData[0].nSD2

				# return pyData

    # ####################获取指数最新行情接口####################
    # #0:失败，1：成功
    # #返回值：IndexQuote指针
    # def GetLatestIndexQuote(self, szWindCode):
				# cData = self.ffi.new("struct IndexQuote[]", 1)
				# for i in range(0, min(len(cData[0].szWindCode), len(szWindCode))):
				    # cData[0].szWindCode[i] = szWindCode[i]
				# self.dll_handler.GetLatestIndexQuote(cData)

				# pyData = IndexQuote();

				# #copy data
				# char_buf_len = len(cData[0].szWindCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szWindCode[i] = ord((cData[0].szWindCode)[i])

				# char_buf_len = len(cData[0].szCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szCode[i] = ord((cData[0].szCode)[i])

				# pyData.nActionDay = cData[0].nActionDay
				# pyData.nTradingDay = cData[0].nTradingDay
				# pyData.nTime = cData[0].nTime
				# pyData.nOpenIndex = cData[0].nOpenIndex
				# pyData.nHighIndex = cData[0].nHighIndex
				# pyData.nLowIndex = cData[0].nLowIndex
				# pyData.nLastIndex = cData[0].nLastIndex
				# pyData.iTotalVolume = cData[0].iTotalVolume
				# pyData.iTurnover = cData[0].iTurnover
				# pyData.nPreCloseIndex = cData[0].nPreCloseIndex

				# return pyData

    # ####################获取期货最新行情接口####################
    # #0:失败，1：成功
    # #返回值：FutureQuote指针
    # def GetLatestFutureQuote(self, szWindCode):
				# cData = self.ffi.new("struct FutureQuote[]", 1)
				# for i in range(0, min(len(cData[0].szWindCode), len(szWindCode))):
				    # cData[0].szWindCode[i] = szWindCode[i]
				# self.dll_handler.GetLatestFutureQuote(cData)

				# pyData = FutureQuote();

				# #copy data
				# char_buf_len = len(cData[0].szWindCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szWindCode[i] = ord((cData[0].szWindCode)[i])

				# char_buf_len = len(cData[0].szCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szCode[i] = ord((cData[0].szCode)[i])

				# char_buf_len = len(cData[0].nAskPrice)
				# for i in range(0, char_buf_len-1):
						# pyData.nAskPrice[i] = (cData[0].nAskPrice)[i]

				# char_buf_len = len(cData[0].nAskVol)
				# for i in range(0, char_buf_len-1):
						# pyData.nAskVol[i] = (cData[0].nAskVol)[i]

				# char_buf_len = len(cData[0].nBidPrice)
				# for i in range(0, char_buf_len-1):
						# pyData.nBidPrice[i] = (cData[0].nBidPrice)[i]

				# char_buf_len = len(cData[0].nBidVol)
				# for i in range(0, char_buf_len-1):
						# pyData.nBidVol[i] = (cData[0].nBidVol)[i]

				# pyData.nActionDay = cData[0].nActionDay
				# pyData.nTradingDay = cData[0].nTradingDay
				# pyData.nTime = cData[0].nTime
				# pyData.nStatus = cData[0].nStatus
				# pyData.iPreOpenInterest = cData[0].iPreOpenInterest
				# pyData.nPreClose = cData[0].nPreClose
				# pyData.nPreSettlePrice = cData[0].nPreSettlePrice
				# pyData.nOpen = cData[0].nOpen
				# pyData.nHigh = cData[0].nHigh
				# pyData.nLow = cData[0].nLow
				# pyData.nMatch = cData[0].nMatch
				# pyData.iVolume = cData[0].iVolume
				# pyData.iTurnover = cData[0].iTurnover
				# pyData.iOpenInterest = cData[0].iOpenInterest
				# pyData.nClose = cData[0].nClose
				# pyData.nSettlePrice = cData[0].nSettlePrice
				# pyData.nHighLimited = cData[0].nHighLimited
				# pyData.nLowLimited = cData[0].nLowLimited
				# pyData.nPreDelta = cData[0].nPreDelta
				# pyData.nCurrDelta = cData[0].nCurrDelta
				# pyData.lAuctionPrice = cData[0].lAuctionPrice
				# pyData.lAuctionQty = cData[0].lAuctionQty
				# pyData.lAvgPrice = cData[0].lAvgPrice

				# return pyData

    # ####################获取单个证券最新行情接口(废弃)####################
    # #0:失败，1：成功
    # #返回值：DataBase指针
    # def GetLatestData(self, szWindCode, eStockType):
				# cData = self.ffi.new("struct DataBase[]", 1)
				# for i in range(0, min(len(cData[0].szWindCode), len(szWindCode))):
						# cData[0].szWindCode[i] = szWindCode[i]
				# cData[0].eType = eStockType
				# self.dll_handler.GetLatestQuote(cData)
				
				# pyData = DataBase();
				# #memmove(pyData.szWindCode, self.ffi.string(cData[0].szWindCode), 32)
				# pyData.eType = cData[0].eType
				# char_buf_len = len(cData[0].szWindCode)
				# for i in range(0, char_buf_len-1):
						# pyData.szWindCode[i] = ord((cData[0].szWindCode)[i])
						# #pp = pyData.szWindCode[i]
						# #print "pp:",pp,",int:",chr(pp)
				# #TODO  quote needed to be copied
				# #quote = self.ffi.new("void*[1]", [cData[0].quote])
				# #print "quote object:", quote, ", quote type:", type(quote)
				# #memmove(byref(pyData.quote), self.ffi.buffer(cData[0].quote), sizeof(pyData.quote))
				# return pyData

    # ####################获取多个证券最新行情接口(废弃)####################
    # #0:失败，1：成功
    # #返回值：DataBase数组
    # def GetLatestDatas(self, maxNum):
				# cDatas = self.ffi.new("struct DataBase[]", maxNum)
				# self.dll_handler.GetLatestQuotes(cDatas, maxNum)

				# pyDatas = (DataBase * maxNum)();
				# for i in range(0, len(cDatas)):
						# char_buf_len = len(cDatas[i].szWindCode)
						# for j in range(0, char_buf_len-1):
								# pyDatas[i].szWindCode[j] = ord((cDatas[i].szWindCode)[j])
						# pyDatas[i].eType = cDatas[i].eType
						# #TODO
						# #pyDatas[i].quote = self.ffi._pointer_to(cDatas[i].quote)
				# return pyDatas

