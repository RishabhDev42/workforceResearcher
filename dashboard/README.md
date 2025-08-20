
# Text Sentiment Dashboard (Streamlit)

A simple, multipage Streamlit app to explore sentiment analysis results.
It expects 12 CSV files with the following names:

**Examples by sentiment**
- `examples_negative.csv`
- `examples_neutral.csv`
- `examples_positive.csv`

**Message-level data**
- `messages_enriched.csv`
- `message_length_summary.csv`

**Keywords / N-grams**
- `top_keywords.csv`
- `top_ngrams_all.csv`
- `top_ngrams_by_sentiment.csv`

**Wordclouds (precomputed frequencies)**
- `wordcloud_all.csv`
- `wordcloud_negative.csv`
- `wordcloud_neutral.csv`
- `wordcloud_positive.csv`

## How to run

1) Put 12 CSVs into `data/` (or keep the ones already placed there).
2) (Optional) Create a virtual environment.
3) Install dependencies:
```bash
pip install -r requirements.txt
```
4) Launch the app:
```bash
streamlit run Home.py
```

## 📁 Structure
```
text-sentiment-dashboard/
├─ Home.py
├─ _utils.py
├─ requirements.txt
├─ pages/
│  ├─ 1_SentimentExplorer.py
│  ├─ 2_KeywordsNgrams.py
│  └─ 3_Wordclouds.py
└─ data/
   └─ (CSVs go here)
```

## 🔧 Notes
- If your filenames differ, you can change them in `_utils.py`.
- The app uses **matplotlib** for simple charts and **Streamlit** tables/filtering.
- All plots are intentionally minimal to keep the skeleton clean.
