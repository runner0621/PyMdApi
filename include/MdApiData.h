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
	char	szCode[32];					//ԭʼCode
	int         nActionDay;             //ҵ������(��Ȼ��)
	int         nTradingDay;            //������
	int			 nTime;					//ʱ��(HHMMSSmmm)
	int			 nStatus;				//״̬
	unsigned int nPreClose;				//ǰ���̼�
	unsigned int nOpen;					//���̼�
	unsigned int nHigh;					//��߼�
	unsigned int nLow;					//��ͼ�
	unsigned int nMatch;				//���¼�

	unsigned int nAskPrice[10];			//������
	unsigned int nAskVol[10];			//������
	unsigned int nBidPrice[10];			//�����
	unsigned int nBidVol[10];			//������
	unsigned int nNumTrades;			//�ɽ�����

	long long		 iVolume;			//�ɽ�����
	long long		 iTurnover;			//�ɽ��ܽ��
	long long		 nTotalBidVol;		//ί����������
	long long		 nTotalAskVol;		//ί����������

	unsigned int nWeightedAvgBidPrice;	//��Ȩƽ��ί��۸�
	unsigned int nWeightedAvgAskPrice;  //��Ȩƽ��ί���۸�
	int			 nIOPV;					//IOPV��ֵ��ֵ
	int			 nYieldToMaturity;		//����������
	unsigned int nHighLimited;			//��ͣ��
	unsigned int nLowLimited;			//��ͣ��
	char		 chPrefix[4];			//֤ȯ��Ϣǰ׺
	int			 nSyl1;					//��ӯ��1
	int			 nSyl2;					//��ӯ��2
	int			 nSD2;					//����2���Ա���һ�ʣ�
};

struct FutureQuote
{
public:
	char	szWindCode[32];				//600001.SH 
	char	szCode[32];					//ԭʼCode
	int          nActionDay;            //ҵ������(��Ȼ��)
	int          nTradingDay;           //������
	int			 nTime;					//ʱ��(HHMMSSmmm)	
	int			 nStatus;				//״̬
	long long	 iPreOpenInterest;		//��ֲ�
	unsigned int nPreClose;				//�����̼�
	unsigned int nPreSettlePrice;		//�����
	unsigned int nOpen;					//���̼�	
	unsigned int nHigh;					//��߼�
	unsigned int nLow;					//��ͼ�
	unsigned int nMatch;				//���¼�
	long long	 iVolume;				//�ɽ�����
	long long	 iTurnover;				//�ɽ��ܽ��
	long long	 iOpenInterest;			//�ֲ�����
	unsigned int nClose;				//������
	unsigned int nSettlePrice;			//�����
	unsigned int nHighLimited;			//��ͣ��
	unsigned int nLowLimited;			//��ͣ��
	int			 nPreDelta;			    //����ʵ��
	int			 nCurrDelta;            //����ʵ��
	unsigned int nAskPrice[5];			//������
	unsigned int nAskVol[5];			//������
	unsigned int nBidPrice[5];			//�����
	unsigned int nBidVol[5];			//������

	//Add 20140605
	int			lAuctionPrice;			//�������жϲο���
	int			lAuctionQty;			//�������жϼ��Ͼ�������ƥ����
	int			lAvgPrice;				//֣�����ڻ�����
};

struct IndexQuote
{
public:
	char	szWindCode[32];		//600001.SH 
	char	szCode[32];			//ԭʼCode
	int         nActionDay;		//ҵ������(��Ȼ��)
	int         nTradingDay;	//������
	int         nTime;			//ʱ��(HHMMSSmmm)
	int		    nOpenIndex;		//����ָ��
	int 	    nHighIndex;		//���ָ��
	int 	    nLowIndex;		//���ָ��
	int 	    nLastIndex;		//����ָ��
	long long	iTotalVolume;	//���������Ӧָ���Ľ�������
	long long	iTurnover;		//���������Ӧָ���ĳɽ����
	int		    nPreCloseIndex;	//ǰ��ָ��
};

struct Transaction
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//ԭʼCode
	int     nActionDay;     //��Ȼ��
	int 	nTime;		    //�ɽ�ʱ��(HHMMSSmmm)
	int 	nIndex;		    //�ɽ����
	int		nPrice;		    //�ɽ��۸�
	int 	nVolume;	    //�ɽ�����
	int		nTurnover;	    //�ɽ����
	int     nBSFlag;        //��������(��'B', ����'A', ������' ')
	char    chOrderKind;    //�ɽ����
	char    chFunctionCode; //�ɽ�����
	int	    nAskOrder;	    //������ί�����
	int	    nBidOrder;	    //����ί�����
};

struct Order
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//ԭʼCode
	int 	nActionDay;	    //ί������(YYMMDD)
	int 	nTime;			//ί��ʱ��(HHMMSSmmm)
	int 	nOrder;	        //ί�к�
	int		nPrice;			//ί�м۸�
	int 	nVolume;		//ί������
	char    chOrderKind;	//ί�����
	char    chFunctionCode;	//ί�д���('B','S','C')
};

struct OrderQueue
{
public:
	char	szWindCode[32];	//600001.SH 
	char	szCode[32];		//ԭʼCode
	int     nActionDay;     //��Ȼ��
	int 	nTime;			//ʱ��(HHMMSSmmm)
	int     nSide;			//��������('B':Bid 'A':Ask)
	int		nPrice;			//ί�м۸�
	int 	nOrders;		//��������
	int 	nABItems;		//��ϸ����
	int 	nABVolume[200];	//������ϸ
};

struct CodeTable
{
public:
	char szWindCode[32];    //Wind Code: AG1302.SHF
	char szMarket[8];       //market code: SHF
	char szCode[32];        //original code:ag1302
	char szENName[32];
	char szCNName[32];      //chinese name: ����1302
	int nType;
};
struct Heartbeat
{
public:
	long SrvStartTime;		//server����ʱ����������ж�server�Ƿ�������
	int nType;
};

}