
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from _utils import load_csv, get_sentiment_column_name, number_fmt

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")
st.title("Sentiment Analysis — Overview")

# Load main dataset
df = load_csv("messages_enriched")
sent_col = get_sentiment_column_name(df)

# KPIs Row
col1, col2, col3 = st.columns(3)
with col1:
    total = len(df)
    st.metric("Total Messages", number_fmt(total))
with col2:
    # unique authors if available
    author_col = None
    for c in ["author", "user", "speaker", "sender"]:
        if c in df.columns:
            author_col = c
            break
    st.metric("Unique Authors", number_fmt(df[author_col].nunique()) if author_col else "—")
with col3:
    st.metric("Columns", number_fmt(len(df.columns) if not df.empty else 0))

st.divider()

# Sentiment distribution
st.subheader("Sentiment Distribution")
if not df.empty and sent_col:
    counts = df[sent_col].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    ax.set_title("Number of Texts per Sentiment")
    st.pyplot(fig)
else:
    st.info("Couldn't find a sentiment column in `messages_enriched.csv`.")

# Message length summary (by sentiment)
st.subheader("Average Message Length by Sentiment")
ml = load_csv("message_length_summary")
if not ml.empty:
    # Expecting columns like: sentiment, avg_length (robust to variations)
    # Try to infer column names
    s_col = None
    for c in ["sentiment", "label", "sentiment_label"]:
        if c in ml.columns:
            s_col = c
            break
    v_col = None
    for c in ["avg_length", "mean_length", "avg_tokens", "avg_chars"]:
        if c in ml.columns:
            v_col = c
            break

    if s_col and v_col:
        fig2, ax2 = plt.subplots()
        ax2.bar(ml[s_col].astype(str), ml[v_col])
        ax2.set_xlabel("Sentiment")
        ax2.set_ylabel(v_col.replace("_", " ").title())
        ax2.set_title("Average Length by Sentiment")
        st.pyplot(fig2)
        st.dataframe(ml)
    else:
        st.info("`message_length_summary.csv` found, but expected columns not detected.")
else:
    st.info("`message_length_summary.csv` not found or empty.")
