import streamlit as st

from app.dashboard.views.upload_page import (
    UploadPage
)

from app.dashboard.views.analysis_page import (
    AnalysisPage
)

from app.dashboard.views.trends_page import (
    TrendsPage
)

from app.dashboard.views.recommendations_page import (
    RecommendationsPage
)


st.set_page_config(

    page_title="InsightFlow X",

    page_icon="📊",

    layout="wide"
)

st.title(
    "📊 InsightFlow X"
)

st.sidebar.title(
    "Navigation"
)

page = st.sidebar.radio(

    "Select Page",

    [

        "Upload",

        "Analysis",

        "Trends",

        "Recommendations"

    ]
)

if page == "Upload":

    UploadPage.render()

elif page == "Analysis":

    AnalysisPage.render()

elif page == "Trends":

    TrendsPage.render()

elif page == "Recommendations":

    RecommendationsPage.render()