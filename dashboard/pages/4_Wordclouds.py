import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from _utils import load_csv, detect_weight_col

st.title("Wordclouds")

def build_freq_dict(df):
    if df.empty:
        return {}
    word_col = next((c for c in df.columns if any(x in c.lower() for x in ["word", "term", "token", "text"])), None)
    freq_col = detect_weight_col(df)
    if not (word_col and freq_col):
        return {}
    tmp = df[[word_col, freq_col]].dropna()
    try:
        tmp[freq_col] = tmp[freq_col].astype(float).clip(lower=0.0)
    except Exception:
        pass
    return dict(zip(tmp[word_col].astype(str), tmp[freq_col]))

def render_wc(df, title):
    freqs = build_freq_dict(df)
    if not freqs:
        st.info(f"No usable frequencies for {title}.")
        return
    wc = WordCloud(width=900, height=500, background_color="white")
    wc.generate_from_frequencies(freqs)
    fig, ax = plt.subplots(figsize=(9,5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title)
    st.pyplot(fig)

st.subheader("Overall")
render_wc(load_csv("wordcloud_all"), "Overall Wordcloud")

st.divider()
st.subheader("By Sentiment")
tabs = st.tabs(["Negative", "Neutral", "Positive"])
with tabs[0]:
    render_wc(load_csv("wordcloud_negative"), "Negative Wordcloud")
with tabs[1]:
    render_wc(load_csv("wordcloud_neutral"), "Neutral Wordcloud")
with tabs[2]:
    render_wc(load_csv("wordcloud_positive"), "Positive Wordcloud")
