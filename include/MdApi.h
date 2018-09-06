#pragma once
#include "MdApiData.h"

#ifdef _WIN32
#ifdef HZ_TDF_SRV_API_EXPORTS
#define HZ_TDF_SRV_API __declspec(dllexport)
#else
#define HZ_TDF_SRV_API __declspec(dllimport)
#endif

#define HZSTDCALL __stdcall			/* ensure stcall calling convention on NT */
#define CALLBACK __stdcall
#else
#define HZ_TDF_SRV_API
#define HZSTDCALL				    /* leave blank for other systems */
#define CALLBACK
#endif

using namespace MdApi;
using namespace std;

#ifdef __cplusplus
extern "C"
{
#endif
	// 定义回调
	typedef void(CALLBACK *StockQuoteCallback)(MdApi::StockQuote*);
	typedef void(CALLBACK *IndexQuoteCallback)(MdApi::IndexQuote*);
	typedef void(CALLBACK *FutureQuoteCallback)(MdApi::FutureQuote*);
	typedef void(CALLBACK *TransactionCallback)(MdApi::Transaction*);
	typedef void(CALLBACK *OrderCallback)(MdApi::Order*);
	typedef void(CALLBACK *OrderQueueCallback)(MdApi::OrderQueue*);
	typedef void(CALLBACK *CodeTableCallback)(MdApi::CodeTable*);
	// 设置回调
	HZ_TDF_SRV_API void HZSTDCALL SetStockQuoteCallback(StockQuoteCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetIndexQuoteCallback(IndexQuoteCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetFutureQuoteCallback(FutureQuoteCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetTransactionCallback(TransactionCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetOrderCallback(OrderCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetOrderQueueCallback(OrderQueueCallback cb);
	HZ_TDF_SRV_API void HZSTDCALL SetCodeTableCallback(CodeTableCallback cb);
	// 登录、退出
	HZ_TDF_SRV_API int HZSTDCALL HzTDFSrvApi_Connect(); // 0:失败，1：成功
	HZ_TDF_SRV_API void HZSTDCALL HzTDFSrvApi_Dispose();

	// 默认无订阅，必须订阅后才有数据传输，HzTDFSrvApi_Subscribe("")表示全订阅
	// 必需在Connect成功后订阅
	//HZ_TDF_SRV_API int HZSTDCALL HzTDFSrvApi_SubscribeList(vector<string>& subList);
	HZ_TDF_SRV_API int HZSTDCALL HzTDFSrvApi_Subscribe(const char* sub); // 0:失败，1：成功
	//HZ_TDF_SRV_API int HZSTDCALL HzTDFSrvApi_UnSubscribeList(vector<string>& subList);
	HZ_TDF_SRV_API int HZSTDCALL HzTDFSrvApi_UnSubscribe(const char* sub); // 0:失败，1：成功

	//// 主动获取最新价格
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestStockQuote(MdApi::StockQuote* pData);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestIndexQuote(MdApi::IndexQuote* pData);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestFutureQuote(MdApi::FutureQuote* pData);
	//HZ_TDF_SRV_API MdApi::Transaction* HZSTDCALL GetLatestTransactionQuote(const char* szWindCode);
	//HZ_TDF_SRV_API MdApi::Order* HZSTDCALL GetLatestOrderQuote(const char* szWindCode);
	//HZ_TDF_SRV_API MdApi::OrderQueue* HZSTDCALL GetLatestOrderQueueQuote(const char* szWindCode);

	//HZ_TDF_SRV_API void HZSTDCALL GetLatestData(MdApi::DataBase* pData);
	//HZ_TDF_SRV_API void HZSTDCALL GetLatestDatas(MdApi::DataBase** pDatas, int num);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestStockQuoteList(MdApi::StockQuote** pDatas, int num);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestIndexQuoteList(MdApi::IndexQuote** pDatas, int num);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestFutureQuoteList(MdApi::FutureQuote** pDatas, int num);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestTransactionList(vector<string>& szWindCodeList, vector<shared_ptr<MdApi::Transaction>>& vecRtn, string& errMsg);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestOrderList(vector<string>& szWindCodeList, vector<shared_ptr<MdApi::Order>>& vecRtn, string& errMsg);
	//HZ_TDF_SRV_API int HZSTDCALL GetLatestOrderQueueList(vector<string>& szWindCodeList, vector<shared_ptr<MdApi::OrderQueue>>& vecRtn, string& errMsg);

#ifdef __cplusplus
}
#endif

