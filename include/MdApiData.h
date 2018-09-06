#pragma once
#include <string.h>

namespace MdApi
{
enum DataType
{
	eDataBase = 0,
	eStockQuote = 1,
	eFutureQuote = 2,
	eIndexQuote = 3,
	eTransaction = 4,
	eOrder = 5,
	eOrderQueue = 6,
	eCodeTable = 7,
	eHeartbeat = 8
};

struct DataBase
{
public:
	char szWindCode[32];
	DataType eType;
	void* data;

	DataBase(const char* szWindCode, DataType eType)
	{
		memcpy(this->szWindCode, szWindCode, sizeof(this->szWindCode));
		this->eType = eType;
		data = NULL;
	}

	DataBase()
	{
		memset(this->szWindCode, 0, sizeof(this->szWindCode));
		this->eType = eDataBase;
		data = NULL;
	}
};

struct StockQuote
{
public:
	char	szWindCode[32];				//600001.SH 
	char	szCode[32];					//原始Code
	int         nActionDay;             //业务发生日(自然日)
	int         nTradingDay;            //交易日
	int			 nTime;					//时间(HHMMSSmmm)
	int			 nStatus;				//状态
	unsigned int nPreClose;				//前收盘价
	unsigned int nOpen;					//开盘价
	unsigned int nHigh;					//最高价
	unsigned int nLow;					//最低价
	unsigned int nMatch;				//最新价

	unsigned int nAskPrice[10];			//申卖价
	unsigned int nAskVol[10];			//申卖量
	unsigned int nBidPrice[10];			//申买价
	unsigned int nBidVol[10];			//申买量
	unsigned int nNumTrades;			//成交笔数

	long long		 iVolume;			//成交总量
	long long		 iTurnover;			//成交总金额
	long long		 nTotalBidVol;		//委托买入总量
	long long		 nTotalAskVol;		//委托卖出总量

	unsigned int nWeightedAvgBidPrice;	//加权平均委买价格
	unsigned int nWeightedAvgAskPrice;  //加权平均委卖价格
	int			 nIOPV;					//IOPV净值估值
	int			 nYieldToMaturity;		//到期收益率
	unsigned int nHighLimited;			//涨停价
	unsigned int nLowLimited;			//跌停价
	char		 chPrefix[4];			//证券信息前缀
	int			 nSyl1;					//市盈率1
	int			 nSyl2;					//市盈率2
	int			 nSD2;					//升跌2（对比上一笔）
};

struct FutureQuote
{
public:
	char	szWindCode[32];				//600001.SH 
	char	szCode[32];					//原始Code
	int          nActionDay;            //业务发生日(自然日)
	int          nTradingDay;           //交易日
	int			 nTime;					//时间(HHMMSSmmm)	
	int			 nStatus;				//状态
	long long	 iPreOpenInterest;		//昨持仓
	unsigned int nPreClose;				//昨收盘价
	unsigned int nPreSettlePrice;		//昨结算
	unsigned int nOpen;					//开盘价	
	unsigned int nHigh;					//最高价
	unsigned int nLow;					//最低价
	unsigned int nMatch;				//最新价
	long long	 iVolume;				//成交总量
	long long	 iTurnover;				//成交总金额
	long long	 iOpenInterest;			//持仓总量
	unsigned int nClose;				//今收盘
	unsigned int nSettlePrice;			//今结算
	unsigned int nHighLimited;			//涨停价
	unsigned int nLowLimited;			//跌停价
	int			 nPreDelta;			    //昨虚实度
	int			 nCurrDelta;            //今虚实度
	unsigned int nAskPrice[5];			//申卖价
	unsigned int nAskVol[5];			//申卖量
	unsigned int nBidPrice[5];			//申买价
	unsigned int nBidVol[5];			//申买量

	//Add 20140605
	int			lAuctionPrice;			//波动性中断参考价
	int			lAuctionQty;			//波动性中断集合竞价虚拟匹配量
	int			lAvgPrice;				//郑商所期货均价
};

struct IndexQuote
{
public:
	char	szWindCode[32];		//600001.SH 
	char	szCode[32];			//原始Code
	int         nActionDay;		//业务发生日(自然日)
	int         nTradingDay;	//交易日
	int         nTime;			//时间(HHMMSSmmm)
	int		    nOpenIndex;		//今开盘指数
	int 	    nHighIndex;		//最高指数
	int 	    nLowIndex;		//最低指数
	int 	    nLastIndex;		//最新指数
	long long	iTotalVolume;	//参与计算相应指数的交易数量
	long long	iTurnover;		//参与计算相应指数的成交金额
	int		    nPreCloseIndex;	//前盘指数
};

struct Transaction
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//原始Code
	int     nActionDay;     //自然日
	int 	nTime;		    //成交时间(HHMMSSmmm)
	int 	nIndex;		    //成交编号
	int		nPrice;		    //成交价格
	int 	nVolume;	    //成交数量
	int		nTurnover;	    //成交金额
	int     nBSFlag;        //买卖方向(买：'B', 卖：'A', 不明：' ')
	char    chOrderKind;    //成交类别
	char    chFunctionCode; //成交代码
	int	    nAskOrder;	    //叫卖方委托序号
	int	    nBidOrder;	    //叫买方委托序号
};

struct Order
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//原始Code
	int 	nActionDay;	    //委托日期(YYMMDD)
	int 	nTime;			//委托时间(HHMMSSmmm)
	int 	nOrder;	        //委托号
	int		nPrice;			//委托价格
	int 	nVolume;		//委托数量
	char    chOrderKind;	//委托类别
	char    chFunctionCode;	//委托代码('B','S','C')
};

struct OrderQueue
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//原始Code
	int     nActionDay;     //自然日
	int 	nTime;			//时间(HHMMSSmmm)
	int     nSide;			//买卖方向('B':Bid 'A':Ask)
	int		nPrice;			//委托价格
	int 	nOrders;		//订单数量
	int 	nABItems;		//明细个数
	int 	nABVolume[200];	//订单明细
};

struct CodeTable
{
public:
	char szWindCode[32];    //Wind Code: AG1302.SHF
	char szMarket[8];       //market code: SHF
	char szCode[32];        //original code:ag1302
	char szENName[32];
	char szCNName[32];      //chinese name: 沪银1302
	int nType;
};
struct Heartbeat
{
public:
	long SrvStartTime;		//server启动时间戳，用于判断server是否已重启
	int nType;
};

}