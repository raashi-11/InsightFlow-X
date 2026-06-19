import streamlit as st

from app.dashboard.dashboard_state import (
    DashboardState
)


class RecommendationsPage:

    @staticmethod
    def render():

        st.title(
            "🧠 Executive Intelligence Report"
        )

        results = (
            DashboardState.get_results()
        )

        if results is None:

            st.warning(
                "Run an analysis first from the Upload page."
            )

            return

        st.text_area(

            "Executive Report",

            value=results[
                "report"
            ],

            height=700

        )

        st.download_button(

            label=
            "⬇ Download Report",

            data=
            results[
                "report"
            ],

            file_name=
            "executive_report.txt",

            mime=
            "text/plain"
        )