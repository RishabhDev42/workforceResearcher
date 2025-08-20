import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from _utils import load_csv, detect_weight_col

st.title("Word Frequencies")

def render_table_and_bar(df, title="Word Frequencies"):
    if df.empty:
        st.info("No data to display.")
        return
    word_col = next((c for c in df.columns if any(x in c.lower() for x in ["word", "term", "token", "text"])), None)
    freq_col = detect_weight_col(df)
    if not (word_col and freq_col):
        st.info(f"Detected columns: {list(df.columns)} — need a word column and a count/weight column.")
        st.dataframe(df.head(10))
        return
    topn = st.slider(f"Top N — {title}", 10, 100, 30, key=title)
    df2 = df.nlargest(topn, freq_col)
    st.dataframe(df2, use_container_width=True)
    fig, ax = plt.subplots()
    ax.barh(df2[word_col][::-1], df2[freq_col][::-1])
    ax.set_xlabel(freq_col.replace("_", " ").title())
    ax.set_ylabel("Word")
    ax.set_title(title)
    st.pyplot(fig)

st.subheader("Overall")
render_table_and_bar(load_csv("wordcloud_all"), "Overall Word Frequencies")

st.divider()
st.subheader("By Sentiment")
tabs = st.tabs(["Negative", "Neutral", "Positive"])
with tabs[0]:
    render_table_and_bar(load_csv("wordcloud_negative"), "Negative Word Frequencies")
with tabs[1]:
    render_table_and_bar(load_csv("wordcloud_neutral"), "Neutral Word Frequencies")
with tabs[2]:
    render_table_and_bar(load_csv("wordcloud_positive"), "Positive Word Frequencies")
