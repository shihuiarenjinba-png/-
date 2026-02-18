import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_analysis_dataset(df, horizon_days=60):
    """
    Module 2で作った特徴量データフレームに対し、
    「未来の結果（正解ラベル）」を付与して分析用データセットを作成する。
    
    Parameters:
    - df: feature_factory.py で作成したデータフレーム
    - horizon_days: 何日後のリターンを予測対象とするか（デフォルト60日＝約3ヶ月）
    
    Returns:
    - analysis_df: 特徴量と未来のリターンが紐付いたデータ（直近の未来がない期間は除外済み）
    """
    data = df.copy()
    
    # 1. 未来のリターン (Target) の計算
    # shift(-horizon_days) を使うことで、
    # 「今日の行」に「N日後の価格」を持ってきて計算する
    # 未来の価格 / 今日の価格 - 1 = リターン率
    future_price = data['Price'].shift(-horizon_days)
    data['Future_Return'] = (future_price / data['Price']) - 1
    
    # 2. データのクリーニング（慎重な処理）
    # 直近の horizon_days 分のデータは、まだ未来が来ていないため NaN になる。
    # これを分析に含めるとエラーの原因になるため、確実に除外する。
    valid_data = data.dropna()
    
    return valid_data

def calculate_correlation_matrix(df):
    """
    主要な変数間の相関係数を計算して返す。
    これが「1」や「-1」に近いほど、予測の確度が高いことを意味する。
    """
    # 分析に必要なカラムだけを抽出
    target_cols = ['Price_Deviation', 'Time_Deviation', 'Future_Return']
    
    # 存在しないカラムがあれば無視して計算（エラー回避）
    available_cols = [c for c in target_cols if c in df.columns]
    
    return df[available_cols].corr()
