import yfinance as yf
import pandas as pd

def get_synced_market_data(ticker="^N225"):
    """
    分析に必要な「表の変数（価格）」と「裏の変数（VIX・金利）」を
    取得し、日付インデックスを完全に同期させて返す。
    """
    # 1. データの取得
    # ^N225: 日経平均
    # ^VIX: 恐怖指数 (市場の心理)
    # ^TNX: 米国10年債利回り (長期金利)
    # ^FVX: 米国5年債利回り (中期金利 - イールドカーブ算出用)
    tickers = {
        "Price": ticker,
        "VIX": "^VIX",
        "Bond_10Y": "^TNX",
        "Bond_5Y": "^FVX"
    }
    
    # データを一括ダウンロード
    raw_data = yf.download(list(tickers.values()), period="max")['Adj Close']
    
    # カラム名をわかりやすくリネーム
    # yfinanceのダウンロード順を辞書の逆引きでマッピング
    inv_tickers = {v: k for k, v in tickers.items()}
    df = raw_data.rename(columns=inv_tickers)
    
    # 2. データの整形
    # 市場によって休場日が異なるため、前日終値で補完（ffill）し、
    # 全ての変数が揃わない古い期間は削除する
    df = df.fillna(method='ffill').dropna()
    
    return df
