# Common configuration items to be used across Strategies

from freqtrade.strategy.interface import IStrategy

exchange_name = "binanceus"
informative_pair = "BTC/USD"

# ROI table:
minimal_roi = {
    "0": 0.265,
    "73": 0.066,
    "95": 0.013,
    "319": 0
}

# Stoploss:
stoploss = -0.264

# Trailing stop:
trailing_stop = True
trailing_stop_positive = 0.01
trailing_stop_positive_offset = 0.068
trailing_only_offset_is_reached = True

# Optimal timeframe for the strategy
timeframe = '5m'

# run "populate_indicators" only for new candle
process_only_new_candles = False

# Experimental settings (configuration will overide these if set)
use_sell_signal = True
sell_profit_only = False
ignore_roi_if_buy_signal = True

# Optional order type mapping
order_types = {
    'buy': 'limit',
    'sell': 'limit',
    'stoploss': 'market',
    'stoploss_on_exchange': False
}

# Optional order time in force.
order_time_in_force = {
    'buy': 'gtc',
    'sell': 'gtc'
}

# HYPERPARAMETERS FOR STRATEGIES

# These are typically generated with hyperopt

# To update strategy parameters, just cut&paste the "buy_params" contents from the strategy into the entry of the
# dictionary indexed by strategy name.
# It's done this way to make it easier to update (frequently)

strategyParameters = {}

# EMABounce presents an issue since sometimes there just is no solution. Set a default set of values:
strategyParameters["EMABounce"] = {
    "buy_diff": 0.065,
    "buy_long_period": 50,
    "buy_macd_enabled": False,
    "buy_short_period": 10,
}
#====== AUTO-GENERATED PARAMETERS =========

# ComboHold
strategyParameters["ComboHold"] = {
    "buy_bbbhold_enabled": False,
    "buy_bigdrop_enabled": False,
    "buy_btcjump_enabled": False,
    "buy_btcndrop_enabled": False,
    "buy_btcnseq_enabled": False,
    "buy_emabounce_enabled": True,
    "buy_fisherbb_enabled": True,
    "buy_macdcross_enabled": True,
    "buy_ndrop_enabled": True,
    "buy_nseq_enabled": True,
}

# BBBHold
strategyParameters["BBBHold"] = {
        "buy_bb_gain": 0.04,
        "buy_fisher": -0.81,
        "buy_fisher_enabled": True,
        "buy_mfi": 32.0,
        "buy_mfi_enabled": False,
}
# BigDrop
strategyParameters["BigDrop"] = {
        "buy_bb_enabled": False,
        "buy_drop": 0.04,
        "buy_fisher": -0.68,
        "buy_fisher_enabled": True,
        "buy_mfi": 29.0,
        "buy_mfi_enabled": False,
        "buy_num_candles": 9,
}

# BTCBigDrop
strategyParameters["BTCBigDrop"] = {
        "buy_bb_enabled": False,
        "buy_drop": 0.055,
        "buy_fisher": -0.02,
        "buy_fisher_enabled": False,
        "buy_mfi": 20.0,
        "buy_mfi_enabled": True,
        "buy_num_candles": 8,
}

# BTCJump
strategyParameters["BTCJump"] = {
        "buy_bb_gain": 0.11,
        "buy_btc_jump": 0.014,
        "buy_fisher": -0.28,
}

# BTCNDrop
strategyParameters["BTCNDrop"] = {
    "buy_bb_enabled": True,
    "buy_drop": 0.059,
    "buy_fisher": -0.98,
    "buy_fisher_enabled": True,
    "buy_mfi": 20.0,
    "buy_mfi_enabled": True,
    "buy_num_candles": 6,
}

# BTCNSeq
strategyParameters["BTCNSeq"] = {
        "buy_bb_enabled": False,
        "buy_bb_gain": 0.08,
        "buy_drop": 0.01,
        "buy_fisher": 0.56,
        "buy_fisher_enabled": True,
        "buy_num_candles": 2,
}

# EMABounce
strategyParameters["EMABounce"] = {
        "buy_diff": 0.033,
        "buy_long_period": 75,
        "buy_macd_enabled": True,
        "buy_short_period": 9,
}

# FisherBB
strategyParameters["FisherBB"] = {
        "buy_bb_gain": 0.06,
        "buy_fisher": 0.01,
}

# FisherBB2
strategyParameters["FisherBB2"] = {
        "buy_bb_gain": 0.06,
        "buy_fisher": -0.68,
}

# MACDCross
strategyParameters["MACDCross"] = {
        "buy_adx": 55.0,
        "buy_adx_enabled": False,
        "buy_bb_enabled": True,
        "buy_bb_gain": 0.04,
        "buy_dm_enabled": True,
        "buy_fisher": 0.07,
        "buy_fisher_enabled": False,
        "buy_mfi": 32.0,
        "buy_mfi_enabled": False,
        "buy_neg_macd_enabled": True,
        "buy_period": 8,
        "buy_sar_enabled": False,
}

# NDrop
strategyParameters["NDrop"] = {
        "buy_bb_enabled": False,
        "buy_drop": 0.027,
        "buy_fisher": -0.09,
        "buy_fisher_enabled": True,
        "buy_mfi": 34.0,
        "buy_mfi_enabled": False,
        "buy_num_candles": 2,
}

# NSeq
strategyParameters["NSeq"] = {
        "buy_bb_enabled": True,
        "buy_drop": 0.016,
        "buy_fisher": 0.72,
        "buy_fisher_enabled": False,
        "buy_mfi": 36.0,
        "buy_mfi_enabled": False,
        "buy_num_candles": 3,
}

