import streamlit as st

import pandas as pd

from app.dashboard.dashboard_state import (
    DashboardState
)


class TrendsPage:

    @staticmethod
    def render():

        st.title(
            "📈 Organizational Trends"
        )

        results = (
            DashboardState.get_results()
        )

        if results is None:

            st.warning(
                "Run an analysis first from the Upload page."
            )

            return

        theme_counts = (

            results[
                "theme_counts"
            ]
        )

        df = pd.DataFrame(

            {

                "Theme":
                list(
                    theme_counts.keys()
                ),

                "Count":
                list(
                    theme_counts.values()
                )
            }

        )

        st.subheader(
            "Theme Frequency"
        )

        st.bar_chart(

            df.set_index(
                "Theme"
            )
        )

        st.subheader(
            "Theme Table"
        )

        st.dataframe(
            df
        )