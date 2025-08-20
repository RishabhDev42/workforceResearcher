
import streamlit as st
import pandas as pd

from _utils import load_csv, get_sentiment_column_name, get_text_column_name

st.title("Sentiment Explorer")

# Examples by sentiment
st.subheader("Examples by Sentiment")
tabs = st.tabs(["Negative", "Neutral", "Positive"])

with tabs[0]:
    eg_neg = load_csv("examples_negative")
    st.dataframe(eg_neg, use_container_width=True)

with tabs[1]:
    eg_neu = load_csv("examples_neutral")
    st.dataframe(eg_neu, use_container_width=True)

with tabs[2]:
    eg_pos = load_csv("examples_positive")
    st.dataframe(eg_pos, use_container_width=True)

st.divider()

# Full dataset filter/search
st.subheader("Filter Full Dataset")
df = load_csv("messages_enriched")

if df.empty:
    st.info("Upload your `messages_enriched.csv` into `data/` to enable filtering.")
else:
    sent_col = get_sentiment_column_name(df)
    text_col = get_text_column_name(df)

    # Filters
    c1, c2 = st.columns([1,3])
    with c1:
        sentiments = sorted(df[sent_col].dropna().unique()) if sent_col else []
        selected_sent = st.multiselect("Sentiment", sentiments, default=sentiments[:])
    with c2:
        query = st.text_input("Search text contains (case-insensitive)")

    # Apply filters
    filtered = df.copy()
    if sent_col and selected_sent:
        filtered = filtered[filtered[sent_col].isin(selected_sent)]
    if query and text_col:
        filtered = filtered[filtered[text_col].str.contains(query, case=False, na=False)]

    st.write(f"Showing {len(filtered):,} / {len(df):,} rows")
    st.dataframe(filtered, use_container_width=True)

    # Download
    st.download_button("Download filtered CSV", data=filtered.to_csv(index=False), file_name="filtered_messages.csv", mime="text/csv")
