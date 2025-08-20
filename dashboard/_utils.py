
import os
import pandas as pd
import streamlit as st

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

FILENAMES = {
    # examples
    "examples_negative": "examples_negative.csv",
    "examples_neutral": "examples_neutral.csv",
    "examples_positive": "examples_positive.csv",
    # messages
    "messages_enriched": "messages_enriched.csv",
    "message_length_summary": "message_length_summary.csv",
    # keywords & ngrams
    "top_keywords": "top_keywords.csv",
    "top_ngrams_all": "top_ngrams_all.csv",
    "top_ngrams_by_sentiment": "top_ngrams_by_sentiment.csv",
    # wordclouds
    "wordcloud_all": "wordcloud_all.csv",
    "wordcloud_negative": "wordcloud_negative.csv",
    "wordcloud_neutral": "wordcloud_neutral.csv",
    "wordcloud_positive": "wordcloud_positive.csv",
}

@st.cache_data(show_spinner=False)
def load_csv(name: str) -> pd.DataFrame:
    """Load a CSV by logical name defined in FILENAMES."""
    if name not in FILENAMES:
        raise KeyError(f"Unknown dataset key: {name}")
    path = os.path.join(DATA_DIR, FILENAMES[name])
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        st.warning(f"Missing file: {FILENAMES[name]} (expected in data/)")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading {FILENAMES[name]}: {e}")
        return pd.DataFrame()
    return df

def get_sentiment_column_name(df: pd.DataFrame) -> str:
    """Try to infer the sentiment column name from common variants."""
    for cand in ["sentiment", "label", "predicted_sentiment", "sentiment_label"]:
        if cand in df.columns:
            return cand
    return ""

def get_text_column_name(df: pd.DataFrame) -> str:
    """Try to infer the text column name from common variants."""
    for cand in ["text", "message", "content", "body"]:
        if cand in df.columns:
            return cand
    return ""

def detect_weight_col(df):
    for c in df.columns:
        lc = c.lower()
        if any(x in lc for x in ["count", "frequency", "freq", "occurrence", "total", "tfidf_sum", "tfidf"]):
            return c
    return ""

def number_fmt(n):
    try:
        return f"{int(n):,}"
    except Exception:
        return str(n)
