import streamlit as st
from data_engine import fetch_all_data, get_yield_curve

# ページ設定
st.set_page_config(page_title="Mean Reversion Lab", layout="wide")

st.title("📈 Mean Reversion Lab")
st.caption("平均回帰の『窓』を統計的に解明し、ポートフォリオを最適化する")

# --- データの読み込み ---
with st.spinner('データをロード中...'):
    raw_data = fetch_all_data("^N225")
    data = get_yield_curve(raw_data)

# --- サイドバー：設定 ---
st.sidebar.header("Settings")
ticker = st.sidebar.selectbox("Target Index", ["^N225", "^GSPC", "^IXIC"], index=0)

# --- メイン画面：機能スイッチ（タブ） ---
tab1, tab2 = st.tabs(["🔍 Correlation Lab (相関探索)", "🔮 Predictive Forge (予測生成)"])

with tab1:
    st.header("相関探索モード")
    st.write("ここでは、どの変数が平均回帰に効いているかを分析します。")
    # 次のステップでここにグラフ機能を実装します
    st.dataframe(data.tail())

with tab2:
    st.header("予測生成モード")
    st.write("現在のベクトルから、過去の類似局面を検索し、未来の確率分布を作ります。")
    # さらにその次のステップでここにベクトル検索機能を実装します
