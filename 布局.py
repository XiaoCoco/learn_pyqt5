import os
import shutil
import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import *

from base_api import BaseApi
from strategyPolicy import StrategyPolicy

strategy_path = r'C:\Users\xiaok\Desktop\purepython\strategy'

_all_func_ = {

    'K线数据': [
        ['BarCount', 'Bar总数'],
        ['Open', '开盘价,简写O'],
        ['Close', '收盘价,简写C'],
        ['High', '最高价,简写H'],
        ['Low', '最低价,简写L'],
        ['OpenD', 'N天前的开盘价'],
        ['CloseD', 'N天前的收盘价'],
        ['HighD', 'N天前的最高价'],
        ['LowD', 'N天前的最低价'],
        ['Vol', '成交量,简写V'],
        ['OpenInt', '持仓量'],
        ['BarStatus', '当前Bar状态值'],
        ['CurrentBar', '当前Bar索引值'],
        ['Date', '当前Bar日期,简写D'],
        ['Time', '当前Bar时间,简写T'],
        ['TradeDate', '当前Bar的交易日'],
        ['HistoryDataExist', '历史数据是否存在'],
        ['HisData', '获取各种历史数据数组'],
        ['HisBarsInfo', '获取历史K线详细数据'],
    ],

    '即时行情': [
        ['Q_UpdateTime', '即时行情更新时间'],
        ['Q_AskPrice', '最新卖价'],
        # ['Q_AskPriceFlag'      , '卖价变化标志'],
        ['Q_AskVol', '最新卖量'],
        ['Q_AvgPrice', '实时均价'],
        ['Q_BidPrice', '最新买价'],
        # ['Q_BidPriceFlag'      , '买价变化标志'],
        ['Q_BidVol', '最新买量'],
        ['Q_Close', '当日收盘价'],
        ['Q_High', '当日最高价'],
        ['Q_HisHigh', '历史最高价'],
        ['Q_HisLow', '历史最低价'],
        # ['Q_InsideVol'         , '内盘'],
        ['Q_Last', '最新价'],
        ['Q_LastDate', '最新成交日期'],
        ['Q_LastTime', '最新成交时间'],
        # ['Q_LastVol'           , '现手'],
        ['Q_Low', '当日最低价'],
        ['Q_LowLimit', '当日跌停价'],
        ['Q_Open', '当日开盘价'],
        ['Q_OpenInt', '持仓量'],
        # ['Q_OpenIntFlag'       , '持仓变化标志'],
        # ['Q_OutsideVol'        , '外盘量'],
        ['Q_PreOpenInt', '昨持仓'],
        ['Q_PreSettlePrice', '昨结算'],
        ['Q_PriceChg', '当日涨跌'],
        ['Q_PriceChgRadio', '当日涨跌幅'],
        # ['Q_TodayEntryVol'     , '当日开仓量'],
        # ['Q_TodayExitVol'      , '当日平仓量'],
        ['Q_TotalVol', '当日成交量'],
        ['Q_TurnOver', '当日成交金额'],
        ['Q_UpperLimit', '当日涨停价'],
        ['Q_TheoryPrice', '当日期权理论价'],
        ['Q_Sigma', '当日期权波动率'],
        ['Q_Delta', '当日期权Delta'],
        ['Q_Gamma', '当日期权Gamma'],
        ['Q_Vega', '当日期权Vega'],
        ['Q_Theta', '当日期权Theta'],
        ['Q_Rho', '当日期权Rho'],
        ['QuoteDataExist', '行情数据是否有效'],
        ['CalcTradeDate', '计算所属交易日'],
    ],

    '策略交易': [
        ['Buy', '多头建仓'],
        ['BuyToCover', '空头平仓'],
        ['Sell', '多头平仓'],
        ['SellShort', '空头建仓'],
        ['StartTrade', '开启实盘交易'],
        ['StopTrade', '暂停实盘交易'],
        ['IsTradeAllowed', '是否允许实盘交易'],
    ],

    '属性函数': [
        ['BarInterval', '图表周期数值'],
        ['BarType', '图表周期类型'],
        ['BidAskSize', '买卖盘个数'],
        # ['CanTrade'            , '是否支持交易'],
        ['ContractUnit', '每手乘数'],
        ['ExchangeName', '交易所名称'],
        ['ExchangeTime', '交易所系统时间'],
        ['ExchangeStatus', '交易所状态'],
        # ['ExpiredDate'         , '最后交易日'],
        ['GetSessionCount', '交易时段个数'],
        ['GetSessionStartTime', '交易时段起始时间'],
        ['GetSessionEndTime', '交易时段结束时间'],
        ['GetNextTimeInfo', '获取下一个时间点信息'],
        ['CurrentDate', '获取当前日期'],
        ['CurrentTime', '获取当前时间'],
        ['TimeDiff', '返回两个时间之间的间隔秒数'],
        ['IsInSession', '当前时间是否为交易时间'],
        ['MarginRatio', '保证金比例'],
        ['MaxBarsBack', '最大回溯Bar数'],
        ['MaxSingleTradeSize', '单笔交易限量'],
        ['PriceTick', '最小变动价'],
        # ['OptionStyle'         , '期权类型'],
        ['OptionType', '看涨看跌'],
        ['PriceScale', '价格精度'],
        # ['RelativeSymbol'      , '关联合约'],
        # ['StrikePrice'         , '期权行权价'],
        ['Symbol', '合约编号'],
        ['SymbolName', '合约名称'],
        ['SymbolType', '品种编号'],
        ['GetTrendContract', '获取主连/近月对应的合约'],
    ],

    '策略状态': [
        ['AvgEntryPrice', '当前持仓平均建仓价格'],
        ['BarsSinceEntry', '当前持仓的第一个建仓位置到当前位置的Bar计数'],
        ['BarsSinceExit', '最近平仓位置到当前位置的Bar计数'],
        ['BarsSinceLastEntry', '当前持仓的最后一个建仓位置到当前位置的Bar计数'],
        ['BarsSinceToday', '当天的第一根Bar到当前的Bar个数'],
        ['ContractProfit', '当前持仓位置的每手浮动盈亏'],
        ['CurrentContracts', '当前持仓的持仓合约数'],
        ['BuyPosition', '当前持仓的买入持仓量'],
        ['SellPosition', '当前持仓的卖出持仓量'],
        #                 ['CurrentEntries'      , '当前持仓的建仓次数'],
        ['EntryDate', '当前持仓的第一个建仓位置的日期'],
        ['EntryPrice', '当前持仓的第一个建仓价格'],
        ['EntryTime', '当前持仓的第一个建仓位置的时间'],
        ['ExitDate', '最近平仓位置Bar日期'],
        ['ExitPrice', '最近平仓位置的平仓价格'],
        ['ExitTime', '最近平仓位置Bar时间'],
        ['LastEntryDate', '当前持仓的最后一个建仓位置的日期'],
        ['LastEntryPrice', '当前持仓的最后一个建仓价格'],
        ['LastEntryTime', '当前持仓的最后一个建仓位置的时间'],
        ['MarketPosition', '当前持仓状态'],
        ['PositionProfit', '当前持仓的浮动盈亏'],
        ['BarsLast', '获取最后一次满足条件时距离当前的bar数'],
        #                 ['MaxContracts'        , '当前持仓的最大持仓合约数'],
        #                 ['MaxEntries'          , '最大的建仓次数'],
        #                 ['MaxPositionLoss'     , '当前持仓的最大浮动亏损数'],
        #                 ['MaxPositionProfit'   , '当前持仓的最大浮动盈利数'],
        #                 ['PositionProfit'      , '当前持仓位置的浮动盈亏'],
    ],

    '策略性能': [
        ['Available', '策略当前可用虚拟资金'],
        ['CurrentEquity', '账户权益'],
        ['FloatProfit', '浮动盈亏'],
        ['GrossLoss', '累计总亏损'],
        ['GrossProfit', '累计总利润'],
        ['Margin', '持仓保证金'],
        ['NetProfit', '平仓盈亏'],
        # ['NumEvenTrades'       , '保本交易总手数'],
        # ['NumLosTrades'        , '亏损交易总手数'],
        # ['NumWinTrades'        , '盈利交易总手数'],
        ['NumAllTimes', '开仓次数'],
        ['NumWinTimes', '盈利次数'],
        ['NumLoseTimes', '亏损次数'],
        ['NumEventTimes', '保本次数'],
        ['PercentProfit', '盈利成功率'],
        ['TradeCost', '交易产生的手续费'],
        ['TotalTrades', '交易总开仓手数'],
    ],

    '账户函数': [
        ['A_AccountID', '交易账户ID'],
        ['A_AllAccountID', '所有交易账户ID'],
        ['A_GetAllPositionSymbol', '所有持仓合约'],
        ['A_Cost', '手续费'],
        ['A_Assets', '账户权益'],
        ['A_Available', '可用资金'],
        ['A_Margin', '持仓保证金'],
        ['A_ProfitLoss', '浮动盈亏'],
        ['A_CoverProfit', '平仓盈亏'],
        ['A_TotalFreeze', '冻结资金'],
        ['A_BuyAvgPrice', '买入均价'],
        ['A_BuyPosition', '买持仓量'],
        ['A_BuyPositionCanCover', '买仓可平数量'],
        ['A_BuyProfitLoss', '买浮动盈亏'],
        ['A_SellAvgPrice', '卖出均价'],
        ['A_SellPosition', '卖持仓量'],
        ['A_SellPositionCanCover', '卖仓可平数量'],
        ['A_SellProfitLoss', '卖浮动盈亏'],
        ['A_TotalAvgPrice', '总持仓均价'],
        ['A_TotalPosition', '总持仓量'],
        ['A_TotalProfitLoss', '总浮动盈亏'],
        ['A_TodayBuyPosition', '当日买持仓'],
        ['A_TodaySellPosition', '当日卖持仓'],
        ['A_OrderBuyOrSell', '买卖方向'],
        ['A_OrderEntryOrExit', '开平标识'],
        ['A_OrderFilledLot', '定单成交数量'],
        ['A_OrderFilledPrice', '定单成交价格'],
        ['A_OrderLot', '委托数量'],
        ['A_OrderPrice', '委托价格'],
        ['A_OrderStatus', '定单状态'],
        ['A_OrderTime', '下单时间'],
        # ['A_OrderUpdateTime'   , '定单更新时间'],
        ['A_FirstOrderNo', '当前账户第一个订单号'],
        ['A_NextOrderNo', '当前账户下一个订单号'],
        ['A_LastOrderNo', '当前账户最后一个订单号'],
        ['A_FirstQueueOrderNo', '当前账户第一个排队(可撤)订单'],
        ['A_NextQueueOrderNo', '当前账户下一个排队(可撤)订单'],
        ['A_AllQueueOrderNo', '当前账户所有排队(可撤)订单'],
        ['A_LatestFilledTime', '当前账户最新一笔成交委托对应的时间'],
        ['A_OrderContractNo', '订单的合约号'],
        ['A_SendOrder', '下单'],
        ['A_DeleteOrder', '撤单'],
        ['A_GetOrderNo', '获取定单号和委托号'],
        ['DeleteAllOrders', '批量撤单'],
    ],

    '枚举函数': [
        ['Enum_Buy', '买卖类型_买入'],
        ['Enum_Sell', '买卖类型_卖出'],
        ['Enum_Entry', '开平类型_开仓'],
        ['Enum_Exit', '开平类型_平仓'],
        ['Enum_ExitToday', '开平类型_平今'],
        ['Enum_EntryExitIgnore', '开平类型_不区分开平'],
        ['Enum_Sended', '已发送'],
        ['Enum_Accept', '已受理'],
        ['Enum_Triggering', '待触发'],
        ['Enum_Active', '已生效'],
        ['Enum_Queued', '已排队'],
        ['Enum_FillPart', '部分成交'],
        ['Enum_Filled', '完全成交'],
        ['Enum_Canceling', '待撤'],
        ['Enum_Modifying', '待改'],
        ['Enum_Canceled', '已撤单'],
        ['Enum_PartCanceled', '已撤余单'],
        ['Enum_Fail', '指令失败'],
        ['Enum_Suspended', '已挂起'],
        ['Enum_Apply', '已申请'],

        ['Enum_Period_Tick', '周期类型_分笔'],
        # ['Enum_Period_Dyna'    , '周期类型_分时'],
        # ['Enum_Period_Second'  , '周期类型_秒线'],
        ['Enum_Period_Min', '周期类型_分钟'],
        # ['Enum_Period_Hour'    , '周期类型_小时'],
        ['Enum_Period_Day', '周期类型_日线'],
        # ['Enum_Period_Week'    , '周期类型_周线'],
        # ['Enum_Period_Month'   , '周期类型_月线'],
        # ['Enum_Period_Year'    , '周期类型_年线'],
        # ['Enum_Period_DayX'    , '周期类型_多日'],

        ['RGB_Red', '颜色类型_红色'],
        ['RGB_Green', '颜色类型_绿色'],
        ['RGB_Blue', '颜色类型_蓝色'],
        ['RGB_Yellow', '颜色类型_黄色'],
        ['RGB_Purple', '颜色类型_紫色'],
        ['RGB_Gray', '颜色类型_灰色'],
        ['RGB_Brown', '颜色类型_褐色'],

        ['Enum_Order_Market', '订单类型_市价单'],
        ['Enum_Order_Limit', '订单类型_限价单'],
        ['Enum_Order_MarketStop', '订单类型_市价止损单'],
        ['Enum_Order_LimitStop', '订单类型_限价止损单'],
        ['Enum_Order_Execute', '订单类型_行权单'],
        ['Enum_Order_Abandon', '订单类型_弃权单'],
        ['Enum_Order_Enquiry', '订单类型_询价单'],
        ['Enum_Order_Offer', '订单类型_应价单'],
        ['Enum_Order_Iceberg', '订单类型_冰山单'],
        ['Enum_Order_Ghost', '订单类型_影子单'],
        ['Enum_Order_Swap', '订单类型_互换'],
        ['Enum_Order_SpreadApply', '订单类型_套利申请'],
        ['Enum_Order_HedgApply', '订单类型_套保申请'],
        ['Enum_Order_OptionAutoClose', '订单类型_行权前期权自对冲申请'],
        ['Enum_Order_FutureAutoClose', '订单类型_履约期货自对冲申请'],
        ['Enum_Order_MarketOptionKeep', '订单类型_做市商留仓'],

        ['Enum_GFD', '订单有效类型_当日有效'],
        ['Enum_GTC', '订单有效类型_当日有效'],
        ['Enum_GTD', '订单有效类型_限期有效'],
        ['Enum_IOC', '订单有效类型_即时部分'],
        ['Enum_FOK', '订单有效类型_即时全部'],

        ['Enum_Speculate', '订单投保标记_投机'],
        ['Enum_Hedge', '订单投保标记_套保'],
        ['Enum_Spread', '订单投保标记_套利'],
        ['Enum_Market', '订单投保标记_做市'],

        ['Enum_Data_Close', '收盘价'],
        ['Enum_Data_Open', '开盘价'],
        ['Enum_Data_High', '最高价'],
        ['Enum_Data_Low', '最低价'],
        ['Enum_Data_Median', '中间价'],
        ['Enum_Data_Typical', '标准价'],
        ['Enum_Data_Weighted', '加权收盘价'],
        ['Enum_Data_Vol', '成交量'],
        ['Enum_Data_Opi', '持仓量'],
        ['Enum_Data_Time', 'K线时间'],
    ],

    '设置函数': [
        ['SetUserNo', '设置交易账号'],
        ['SetBarInterval', '设置K线类型'],
        ['SetInitCapital', '设置初始资金'],
        ['SetMargin', '设置保证金'],
        ['SetTradeFee', '设置手续费'],
        ['SetActual', '设置实盘运行'],
        # ['SetTradeMode'        , '设置运行方式'],
        ['SetOrderWay', '设置发单方式'],
        ['SetTradeDirection', '设置交易方向'],
        ['SetMinTradeQuantity', '设置最小下单量'],
        ['SetHedge', '设置投保标志'],
        ['SetSlippage', '设置滑点损耗'],
        ['SetTriggerType', '设置触发方式'],
        ['SetWinPoint', '设置策略的止盈点'],
        ['SetStopPoint', '设置策略的止损点'],
        ['SetFloatStopPoint', '设置策略的浮动止损点'],
        ['SubQuote', '订阅指定合约即时行情'],
        ['UnsubQuote', '退订指定合约即时行情'],
    ],

    '绘图函数': [
        ['PlotNumeric', '绘制指标线'],
        ['PlotIcon', '绘制系统图标'],
        ['PlotDot', '绘制点'],
        ['PlotBar', '绘制柱子'],
        ['PlotText', '绘制字符串'],
        ['PlotVertLine', '绘制竖线'],
        ['PlotPartLine', '绘制斜线段'],
        ['PlotStickLine', '绘制竖线段'],
        ['UnPlotText', '取消绘制的字符串'],
        ['UnPlotIcon', '取消绘制的图标'],
        ['UnPlotDot', '取消绘制的点'],
        ['UnPlotBar', '取消绘制的柱子'],
        ['UnPlotNumeric', '取消绘制的指标线'],
        ['UnPlotVertLine', '取消绘制竖线'],
        ['UnPlotPartLine', '取消绘制斜线段'],
        ['UnPlotStickLine', '取消绘制竖线段'],
    ],

    '统计函数': [
        ['SMA', '计算加权移动平均值'],
        ['ParabolicSAR', '计算抛物线转向'],
        ['REF', '求N周期前数据的值'],
        ['Highest', '求最高'],
        ['Lowest', '求最低'],
        ['CountIf', '获取最近N周期满足条件的计数'],
        ['CrossOver', '求是否上穿'],
        ['CrossUnder', '求是否下穿'],
        ['SwingHigh', '求波峰点'],
        ['SwingLow', '求波谷点'],
    ],

    '日志函数': [
        ['LogDebug', '打印调试信息'],
        ['LogInfo', '打印普通信息'],
        ['LogWarn', '打印警告信息'],
        ['LogError', '打印错误信息'],
        ['Alert', '弹出警告提醒'],
    ],

    'context函数': [
        ['strategyStatus', '获取当前策略状态'],
        ['triggerType', '获取当前触发类型'],
        ['contractNo', '获取当前触发合约'],
        ['kLineType', '获取当前触发的K线类型'],
        ['kLineSlice', '获取当前触发的K线周期'],
        ['tradeDate', '获取当前触发的交易日'],
        ['dateTimeStamp', '获取当前触发的时间戳'],
        ['triggerData', '获取当前触发类型对应的数据'],
    ],

}


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.topLayout = QGridLayout()  # 上方布局
        self.bottomLayout = QGridLayout()  # 下方布局
        self.create_stragety_vbox()
        self.create_content_vbox()
        self.create_func_vbox()
        self.create_tab()
        self.create_func_doc()
        self.mainLayout = QGridLayout()  # 主布局为垂直布局
        self.mainLayout.setSpacing(5)  # 主布局添加补白

        # 顶部布局
        self.topLayout.addWidget(self.strategy_vbox, 0, 0, 1, 1)
        self.topLayout.addWidget(self.content_vbox, 0, 1, 1, 1)
        self.topLayout.addWidget(self.func_vbox, 0, 2, 1, 1)

        self.topLayout.setColumnStretch(0, 2)
        self.topLayout.setColumnStretch(1, 5)
        self.topLayout.setColumnStretch(2, 2)

        # 底部布局
        self.bottomLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        self.bottomLayout.addWidget(self.func_doc, 0, 1, 1, 1)

        self.bottomLayout.setColumnStretch(0, 7)
        self.bottomLayout.setColumnStretch(1, 2)

        self.mainLayout.addLayout(self.topLayout, 0, 0, 1, 1)  # 主布局添加top布局
        self.mainLayout.addLayout(self.bottomLayout, 1, 0, 1, 1)  # 也可以不创建上面下方布局，直接addWidget液效果相同

        self.mainLayout.setRowStretch(0, 3)
        self.mainLayout.setRowStretch(1, 1)

        self.setLayout(self.mainLayout)
        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle('极星量化')
        self.show()

        # 策略信息
        self.strategy_path = None

    def create_stragety_vbox(self):
        # 策略树
        self.strategy_vbox = QGroupBox('策略')
        self.strategy_layout = QHBoxLayout()
        self.strategy_tree = QTreeWidget()
        self.strategy_tree.setColumnCount(1)
        self.strategy_tree.setHeaderLabels(['策略'])
        self.strategy_tree.setHeaderHidden(True)

        self.strategy_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.strategy_tree.customContextMenuRequested[QPoint].connect(self.strategy_tree_right_menu)

        for d in os.listdir(strategy_path):
            root = QTreeWidgetItem(self.strategy_tree)
            root.setText(0, d)
            for file in os.listdir(os.path.join(strategy_path, d)):
                child = QTreeWidgetItem(root)
                child.setText(0, file)
        self.strategy_tree.doubleClicked.connect(self.strategy_tree_clicked)
        self.strategy_layout.addWidget(self.strategy_tree)
        self.strategy_vbox.setLayout(self.strategy_layout)

    # 策略右键菜单
    def strategy_tree_right_menu(self, point):
        self.strategy_tree.popMenu = QMenu()
        self.strategy_tree.addType = QMenu(self.strategy_tree.popMenu)
        self.strategy_tree.addType.setTitle('新建')
        rename = QAction('重命名', self.strategy_tree)
        delete = QAction('删除', self.strategy_tree)
        add_strategy = QAction('新建策略')
        add_group = QAction('新建分组')
        refresh = QAction('刷新', self.strategy_tree)
        self.strategy_tree.popMenu.addMenu(self.strategy_tree.addType)
        self.strategy_tree.addType.addAction(add_strategy)
        self.strategy_tree.addType.addAction(add_group)
        self.strategy_tree.popMenu.addAction(rename)
        self.strategy_tree.popMenu.addAction(delete)
        self.strategy_tree.popMenu.addAction(refresh)

        # 右键动作
        action = self.strategy_tree.popMenu.exec_(self.strategy_tree.mapToGlobal(point))
        if action == add_strategy:
            item = self.strategy_tree.currentItem()
            if item and not item.parent():
                value = ''
                while True:
                    value, ok = QInputDialog.getText(self, '新建文件', '策略名称',  QLineEdit.Normal)
                    path = os.path.join(os.path.join(strategy_path, item.text(0)), value+'.py')
                    if os.path.exists(path) and ok:
                        QMessageBox.warning(self, '提示', '策略名在选择的分组%s已经存在！！！' % value, QMessageBox.Yes)
                    elif not ok:
                        break
                    else:
                        with open(path, 'w', encoding='utf-8') as w:
                            pass
                        break

            else:
                QMessageBox.warning(self, '提示', '请选择分组！！！', QMessageBox.Yes)
            self.refresh_strategy()

        elif action == add_group:
            value = ''
            while True:
                value, ok = QInputDialog.getText(self, '新建文件夹', '分组名称', QLineEdit.Normal, value)
                path = os.path.join(strategy_path, value)
                if os.path.exists(path) and ok:
                    QMessageBox.warning(self, '提示', '分组%s已经存在！！！' % value, QMessageBox.Yes)
                elif not ok:
                    break
                else:
                    os.mkdir(path)
                    break

            self.refresh_strategy()

        elif action == refresh:
            self.refresh_strategy()
        elif action == rename:
            item = self.strategy_tree.currentItem()
            if item.parent():  # 修改策略名
                path = os.path.join(os.path.join(strategy_path, item.parent().text(0)), item.text(0))
                value = ''
                while True:
                    value, ok = QInputDialog.getText(self, '修改文%s策略名' % item.text(0), '策略名称', QLineEdit.Normal, value)
                    new_path = os.path.join(os.path.join(strategy_path, item.parent().text(0)), value)
                    if os.path.exists(path) and ok:
                        QMessageBox.warning(self, '提示', '策略名在此分组中%s已经存在！！！' % value, QMessageBox.Yes)
                    elif not ok:
                        break
                    else:
                        os.rename(path, new_path)
                        break
            else:
                path = os.path.join(strategy_path, item.text(0))
                value = ''
                while True:
                    value, ok = QInputDialog.getText(self, '修改%s文件夹' % item.text(0), '分组名称', QLineEdit.Normal, value)
                    new_path = os.path.join(strategy_path, value)
                    if os.path.exists(path) and ok:
                        QMessageBox.warning(self, '提示', '分组%s已经存在！！！' % value, QMessageBox.Yes)
                    elif not ok:
                        break
                    else:
                        os.rename(path, new_path)
                        break
            self.refresh_strategy()
        elif action == delete:
            item = self.strategy_tree.currentItem()
            if item and not item.parent():
                reply = QMessageBox.question(self, '提示',  '确定删除分组及目录下的所有文件吗？', QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    shutil.rmtree(os.path.join(strategy_path, item.text(0)))
            elif item and item.parent():
                reply = QMessageBox.question(self, '提示', '确定删除文件%s吗？' % item.text(0), QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    os.remove(os.path.join(os.path.join(strategy_path, item.parent().text(0)), item.text(0)))
            else:
                pass
            self.refresh_strategy()
        else:
            pass

    def create_content_vbox(self):
        self.content_vbox = QGroupBox('内容')
        self.content_layout = QGridLayout()
        self.save_btn = QPushButton('保存')
        self.run_btn = QPushButton('运行')
        self.contentEdit = QTextEdit()
        self.save_btn.setMaximumSize(80, 60)
        self.run_btn.setMaximumSize(80, 60)
        self.content_layout.addWidget(self.run_btn, 0, 1, 1, 1)
        self.content_layout.addWidget(self.save_btn, 0, 2, 1, 1)
        self.content_layout.addWidget(self.contentEdit, 2, 0, 1, 3)
        self.content_vbox.setLayout(self.content_layout)
        self.run_btn.clicked.connect(self.create_strategy_policy_win)

    def create_func_vbox(self):
        # 函数列表
        self.func_vbox = QGroupBox('函数列表')
        self.func_layout = QVBoxLayout()
        self.func_tree = QTreeWidget()
        self.func_tree.setColumnCount(2)
        self.func_tree.setHeaderLabels(['函数名', '函数介绍'])
        # self.func_tree.setHeaderHidden(True)
        for k, v in _all_func_.items():
            root = QTreeWidgetItem(self.func_tree)
            root.setText(0, k)
            root.setText(1, '')
            for i in v:
                child = QTreeWidgetItem(root)
                child.setText(0, i[0])
                child.setText(1, i[1])
        self.func_tree.clicked.connect(self.func_tree_clicked)
        self.func_layout.addWidget(self.func_tree)
        self.func_vbox.setLayout(self.func_layout)

    def create_tab(self):
        self.tab_widget = QTabWidget()
        # 策略运行table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)  # 行数
        self.tableWidget.setColumnCount(4)  # 列数
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '地址', '年龄', '工资'])
        items = [['JONES', 'Beijing', '23', 2300], ['SMITH', 'SHAngHai', '23', '3000'], ['ZY', 'Tianjin', '23', '2000'],
                 ['Smith', 'SJT', '22', '1030']]
        for i in range(len(items)):  # 注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
            item = items[i]
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(i, j, item)

        self.tab_widget.addTab(self.tableWidget, "策略运行")

    def create_func_doc(self):
        self.func_doc = QTabWidget()
        self.func_content = QTextBrowser()

        self.func_doc.addTab(self.func_content, '函数简介')

    def strategy_tree_clicked(self):
        item = self.strategy_tree.currentItem()
        if item.parent():
            path = os.path.join(os.path.join(strategy_path, item.parent().text(0)), item.text(0))
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.contentEdit.setText(content)
            self.strategy_path = path

    def func_tree_clicked(self):
        item = self.func_tree.currentItem()
        item_text = globals()['BaseApi'].__dict__.get(item.text(0), None).__doc__
        text = item_text.lstrip("\n") if item_text else ''
        self.func_content.setText(text.replace(' ', ''))
        self.func_doc.setTabText(0, item.text(0))

    def refresh_strategy(self):
        # 刷新策略树
        self.strategy_tree.clear()
        for d in os.listdir(strategy_path):
            root = QTreeWidgetItem(self.strategy_tree)
            root.setText(0, d)
            for file in os.listdir(os.path.join(strategy_path, d)):
                child = QTreeWidgetItem(root)
                child.setText(0, file)

    def create_strategy_policy_win(self):
        if self.strategy_path:
            self.strategy_policy_win = StrategyPolicy()
            self.strategy_policy_win.show()
        else:
            QMessageBox.warning(self, '提示', '请选择策略！！！', QMessageBox.Yes)


class StrategyManager(object):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.exit(app.exec_())
