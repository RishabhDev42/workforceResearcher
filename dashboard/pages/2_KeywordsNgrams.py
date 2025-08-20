
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from _utils import load_csv

st.title("Keywords & N-grams")

# Top Keywords
st.subheader("Top Keywords")
kw = load_csv("top_keywords")
if not kw.empty:
    # Try to detect text column
    term_col = None
    for c in kw.columns:
        lc = c.lower()
        if any(x in lc for x in ["term", "keyword", "token", "word", "text"]):
            term_col = c
            break
    
    # Try to detect frequency column
    count_col = None
    for c in kw.columns:
        lc = c.lower()
        if any(x in lc for x in ["count", "frequency", "freq", "occurrence", "total", "tfidf_sum", "tfidf"]):
            count_col = c
            break
    
    if term_col and count_col:
        topn = st.slider("Top N", 5, 50, 20)
        kw2 = kw.nlargest(topn, count_col)
        fig, ax = plt.subplots()
        ax.barh(kw2[term_col][::-1], kw2[count_col][::-1])
        ax.set_xlabel("Count")
        ax.set_ylabel("Term")
        ax.set_title("Top Keywords")
        st.pyplot(fig)
        st.dataframe(kw2, use_container_width=True)
    else:
        st.info(f"Detected columns: {list(kw.columns)} — please rename one to match text/freq")
else:
    st.info("`top_keywords.csv` not found or empty.")

st.divider()

# Top N-grams (overall)
st.subheader("Top N-grams — Overall")
ng_all = load_csv("top_ngrams_all")
if not ng_all.empty:
    # Expect columns like: ngram, count
    ngram_col = None
    count_col = None
    for c in ng_all.columns:
        lc = c.lower()
        if lc in ["ngram", "term", "token", "text"] and ngram_col is None:
            ngram_col = c
        if lc in ["count", "frequency", "freq"] and count_col is None:
            count_col = c
    if ngram_col and count_col:
        topn2 = st.slider("Top N (Overall)", 5, 50, 20, key="overall")
        ng2 = ng_all.nlargest(topn2, count_col)
        fig2, ax2 = plt.subplots()
        ax2.barh(ng2[ngram_col][::-1], ng2[count_col][::-1])
        ax2.set_xlabel("Count")
        ax2.set_ylabel("N-gram")
        ax2.set_title("Top N-grams (Overall)")
        st.pyplot(fig2)
        st.dataframe(ng2, use_container_width=True)
    else:
        st.info("`top_ngrams_all.csv` found, but expected columns not detected.")
else:
    st.info("`top_ngrams_all.csv` not found or empty.")

st.divider()

# Top N-grams by Sentiment
st.subheader("Top N-grams — By Sentiment")
ng_by = load_csv("top_ngrams_by_sentiment")
if not ng_by.empty:
    # Expect columns like: sentiment, ngram, count
    sent_col = None
    ngram_col = None
    count_col = None
    for c in ng_by.columns:
        lc = c.lower()
        if lc in ["sentiment", "label"] and sent_col is None:
            sent_col = c
        if lc in ["ngram", "term", "token", "text"] and ngram_col is None:
            ngram_col = c
        if lc in ["count", "frequency", "freq"] and count_col is None:
            count_col = c

    if sent_col and ngram_col and count_col:
        sentiments = sorted(ng_by[sent_col].dropna().unique())
        chosen = st.selectbox("Pick a sentiment", sentiments)
        topn3 = st.slider("Top N (By Sentiment)", 5, 50, 20, key="by_sent")
        part = ng_by[ng_by[sent_col] == chosen].nlargest(topn3, count_col)
        fig3, ax3 = plt.subplots()
        ax3.barh(part[ngram_col][::-1], part[count_col][::-1])
        ax3.set_xlabel("Count")
        ax3.set_ylabel("N-gram")
        ax3.set_title(f"Top N-grams — {chosen}")
        st.pyplot(fig3)
        st.dataframe(part, use_container_width=True)
    else:
        st.info("`top_ngrams_by_sentiment.csv` found, but expected columns not detected.")
else:
    st.info("`top_ngrams_by_sentiment.csv` not found or empty.")
