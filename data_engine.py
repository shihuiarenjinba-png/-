import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data(ttl=3600)  # 1時間はキャッシュを保持して高速化
def fetch_all_data(benchmark_ticker="^N225"):
    """
    株価・VIX・金利データを一括で取得して統合する
    """
    print(f"Fetching data for {benchmark_ticker}...")
    
    # 1. ベンチマーク（日経平均）の取得
    indices = yf.download(benchmark_ticker, period="max")['Adj Close']
    df = pd.DataFrame(indices)
    df.columns = ['Close']
    
    # 2. VIX指数の取得（恐怖指数）
    vix = yf.download("^VIX", period="max")['Adj Close']
    df['VIX'] = vix
    
    # 3. 米国債利回りの取得（イールドカーブ用）
    # 10年債 (^TNX), 2年債 (^IRXは13週なので、2年債は^ZTYなどを使うか、10Y-3Mにする)
    # ここでは一般的によく使われる10年債と、短期の代用として5年債や13週などを検討
    bond_10y = yf.download("^TNX", period="max")['Adj Close']
    bond_5y = yf.download("^FVX", period="max")['Adj Close']
    
    df['Bond_10Y'] = bond_10y
    df['Bond_5Y'] = bond_5y
    
    # 4. 欠損値の処理（土日のズレなどを埋める）
    df = df.fillna(method='ffill').dropna()
    
    return df

def get_yield_curve(df):
    """イールドカーブ（10Y - 5Yのスプレッド）を計算"""
    df['Yield_Spread'] = df['Bond_10Y'] - df['Bond_5Y']
    return df
