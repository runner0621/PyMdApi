# -*- coding: utf-8 -*-

from ctypes import *


#定义C enum 数据类型
DataType = c_int
#定义C enum 成员
eDataBase    = DataType(0)
eStockQuote  = DataType(1)
eFutureQuote = DataType(2)
eIndexQuote  = DataType(3)
eTransaction = DataType(4)
eOrder       = DataType(5)
eOrderQueue  = DataType(6)


class DataBase(Structure):
    _fields_=[("szWindCode", c_byte*32),
              ("eType",      DataType),
              ("quote",      c_void_p)]


class StockQuote(Structure):
    _fields_=[("szWindCode", c_byte*32),   #600001.SH
              ("szCode",      c_byte*32),  #原始Code
              ("nActionDay",      c_int),  #业务发生日(自然日)
              ("nTradingDay",     c_int),  #交易日
              ("nTime",           c_int),  #时间(HHMMSSmmm)
              ("nStatus",           c_int),  #状态
              ("nPreClose",           c_uint),  #前收盘价
              ("nOpen",           c_uint),  #开盘价
              ("nHigh",           c_uint),  #最高价
              ("nLow",           c_uint),  #最低价
              ("nMatch",           c_uint),  #最新价

              ("nAskPrice",           c_uint*10),  #申卖价
              ("nAskVol",           c_uint*10),  #申卖量
              ("nBidPrice",           c_uint*10),  #申买价
              ("nBidVol",           c_uint*10),  #申买量
              ("nNumTrades",           c_uint),  #成交笔数

              ("iVolume",           c_longlong),  #成交总量
              ("iTurnover",           c_longlong),  #成交总金额
              ("nTotalBidVol",           c_longlong),  #委托买入总量
              ("nTotalAskVol",           c_longlong),  #委托卖出总量
              ("nWeightedAvgBidPrice",           c_uint),  #加权平均委买价格
              ("nWeightedAvgAskPrice",           c_uint),  #加权平均委卖价格
              ("nIOPV",           c_int),  #IOPV净值估值
              ("nYieldToMaturity",           c_int),  #到期收益率
              ("nHighLimited",           c_uint),  #涨停价
              ("nLowLimited",           c_uint),  #跌停价
              ("chPrefix", c_byte*4),   #证券信息前缀
              ("nSyl1",           c_int),  #市盈率1
              ("nSyl2",           c_int),  #市盈率2
              ("nSD2",           c_int)  #升跌2（对比上一笔）
             ]

class FutureQuote(Structure):
    _fields_=[("szWindCode", c_byte*32),   #600001.SH
              ("szCode",      c_byte*32),  #原始Code
              ("nActionDay",      c_int),  #业务发生日(自然日)
              ("nTradingDay",     c_int),  #交易日
              ("nTime",           c_int),  #时间(HHMMSSmmm)
              ("nStatus",           c_int),  #状态
	      ("iPreOpenInterest",           c_longlong),  #昨持仓
              ("nPreClose",           c_uint),  #前收盘价
	      ("nPreSettlePrice",           c_uint),  #昨结算
              ("nOpen",           c_uint),  #开盘价
              ("nHigh",           c_uint),  #最高价
              ("nLow",           c_uint),  #最低价
              ("nMatch",           c_uint),  #最新价
              ("iVolume",           c_longlong),  #成交总量
              ("iTurnover",           c_longlong),  #成交总金额
	      ("iOpenInterest",           c_longlong),  #持仓总量
              ("nClose",           c_uint),  #今收盘
              ("nSettlePrice",           c_uint),  #今结算
              ("nHighLimited",           c_uint),  #涨停价
              ("nLowLimited",           c_uint),  #跌停价
              ("nPreDelta",           c_int),  #昨虚实度
              ("nCurrDelta",           c_int),  #今虚实度
	      ("nAskPrice",           c_uint*5),  #申卖价
              ("nAskVol",           c_uint*5),  #申卖量
              ("nBidPrice",           c_uint*5),  #申买价
              ("nBidVol",           c_uint*5),  #申买量
              ("lAuctionPrice",           c_int),  #波动性中断参考价
	      ("lAuctionQty",           c_int),  #波动性中断集合竞价虚拟匹配量
	      ("lAvgPrice",           c_int)  #郑商所期货均价
             ]
			 
class IndexQuote(Structure):
    _fields_=[("szWindCode", c_byte*32),   #600001.SH
              ("szCode",      c_byte*32),  #原始Code
              ("nActionDay",      c_int),  #业务发生日(自然日)
	      ("nTradingDay",     c_int),  #交易日
              ("nTime",           c_int),  #时间(HHMMSSmmm)
              ("nOpenIndex",           c_int),  #今开盘指数
              ("nHighIndex",           c_int),  #最高指数
              ("nLowIndex",           c_int),  #最低指数
              ("nLastIndex",           c_int),  #最新指数
              ("iTotalVolume",           c_longlong),  #参与计算相应指数的交易数量
              ("iTurnover",           c_longlong),  #成交总金额
              ("nPreCloseIndex",           c_int)  #前盘指数
             ]

class Transaction(Structure):
    _fields_=[("szWindCode", c_byte*32),   #600001.SH
              ("szCode",     c_byte*32),    #原始Code
              ("nActionDay",    c_int),     #业务发生日(自然日)
              ("nTime",         c_int),     #时间(HHMMSSmmm)
              ("nIndex",        c_int),     #成交编号
              ("nPrice",        c_int),     #成交价格
              ("nVolume",       c_int),     #成交数量
              ("nTurnover",     c_int),     #成交金额
              ("nBSFlag",       c_int),     #买卖方向(买：'B', 卖：'A', 不明：' ')
              ("chOrderKind",   c_char),    #成交类别
              ("chFunctionCode",c_char),    #成交代码
              ("nAskOrder",     c_int),     #叫卖方委托序号
              ("nBidOrder",     c_int)      #叫买方委托序号
             ]
    
class Order(Structure):
    _fields_=[("szWindCode", c_byte*32),   	#600001.SH
              ("szCode",     c_byte*32),    #原始Code
              ("nActionDay",    c_int),     #业务发生日(自然日)
              ("nTime",         c_int),     #时间(HHMMSSmmm)
              ("nOrder",        c_int),     #委托号
              ("nPrice",        c_int),     #委托价格
              ("nVolume",       c_int),     #委托数量
              ("chOrderKind",   c_char),    #委托类别
              ("chFunctionCode",c_char)     #委托代码('B','S','C')
             ]

class OrderQueue(Structure):
    _fields_=[("szWindCode", c_byte*32),   	#600001.SH
              ("szCode",     c_byte*32),    #原始Code
              ("nActionDay",    c_int),     #业务发生日(自然日)
              ("nTime",         c_int),     #时间(HHMMSSmmm)
              ("nSide",         c_int),     #买卖方向('B':Bid 'A':Ask)
              ("nPrice",        c_int),     #成交价格
              ("nOrders",       c_int),     #订单数量
              ("nABItems",      c_int),     #明细个数
              ("nABVolume",     c_int*200)  #订单明细
             ]
