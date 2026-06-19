import streamlit as st

from app.dashboard.dashboard_state import (
    DashboardState
)


class AnalysisPage:

    @staticmethod
    def render():

        st.title(
            "📊 Organizational Analysis"
        )

        results = (
            DashboardState.get_results()
        )

        if results is None:

            st.warning(
                "Run an analysis first from the Upload page."
            )

            return

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Files Processed",

                results[
                    "processed_files"
                ]
            )

        with col2:

            sentiment = results[
                "sentiment"
            ]

            st.metric(

                "Sentiment",

                sentiment[
                    "label"
                ]
            )

        with col3:

            st.metric(

                "Risk Score",

                results[
                    "risk_score"
                ]
            )

        st.divider()

        st.subheader(
            "Theme Counts"
        )

        st.json(

            results[
                "theme_counts"
            ]
        )