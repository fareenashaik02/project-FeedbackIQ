import streamlit as st
import plotly.express as px


def show_dashboard(df, metrics):


    c1,c2,c3,c4 = st.columns(4)


    c1.metric(
        "Total Reviews",
        metrics["total_reviews"]
    )


    c2.metric(
        "Average Rating",
        metrics["average_rating"]
    )


    c3.metric(
        "Positive",
        metrics["positive_reviews"]
    )


    c4.metric(
        "Negative",
        metrics["negative_reviews"]
    )


    st.divider()


    col1,col2 = st.columns(2)


    with col1:

        if "Rating" in df.columns:

            chart=df["Rating"].value_counts()

            fig=px.bar(
                chart,
                title="Rating Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        sentiment=df["Sentiment"].value_counts()


        fig=px.pie(
            values=sentiment.values,
            names=sentiment.index,
            title="Sentiment Analysis"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.divider()


    st.subheader("Customer Data")

    st.dataframe(
        df,
        use_container_width=True
    )