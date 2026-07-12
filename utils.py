import pandas as pd


def load_data(file):
    return pd.read_csv(file)


def detect_review_column(df):
    possible_columns = [
        "Review",
        "Reviews",
        "review",
        "reviews",
        "Feedback",
        "feedback",
        "Comment",
        "Comments",
        "comment",
        "comments",
        "Text",
        "text",
        "Review Text",
        "Customer Review",
        "Customer Feedback",
        "Content",
        "Message",
        "Opinion"
    ]

    for col in possible_columns:
        if col in df.columns:
            return col

    for col in df.columns:
        if df[col].dtype == "object":
            return col

    return None


def detect_rating_column(df):
    possible_columns = [
        "Rating",
        "rating",
        "Ratings",
        "ratings",
        "Score",
        "score",
        "Stars",
        "stars",
        "Star Rating",
        "Sentiment Score"
    ]

    for col in possible_columns:
        if col in df.columns:
            return col

    return None


def get_sentiment(rating):
    try:
        rating = float(rating)
    except:
        rating = 3

    if rating >= 4:
        return "Positive"
    elif rating >= 3:
        return "Neutral"
    else:
        return "Negative"


def prepare_dataframe(df):

    review_col = detect_review_column(df)
    rating_col = detect_rating_column(df)

    if review_col is None:
        raise Exception("No review column found in the uploaded CSV.")

    if rating_col is not None:

        df = df.rename(columns={
            review_col: "Review",
            rating_col: "Rating"
        })

    else:

        df = df.rename(columns={
            review_col: "Review"
        })

        df["Rating"] = 3

    df["Review"] = df["Review"].astype(str)

    df["Rating"] = pd.to_numeric(
        df["Rating"],
        errors="coerce"
    ).fillna(3)

    df["Sentiment"] = df["Rating"].apply(get_sentiment)

    return df


def calculate_metrics(df):

    return {
        "total_reviews": len(df),
        "average_rating": round(df["Rating"].mean(), 2),
        "positive_reviews": len(df[df["Sentiment"] == "Positive"]),
        "neutral_reviews": len(df[df["Sentiment"] == "Neutral"]),
        "negative_reviews": len(df[df["Sentiment"] == "Negative"])
    }