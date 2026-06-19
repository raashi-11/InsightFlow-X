import streamlit as st

from pathlib import Path

from app.pipeline.insightflow_pipeline import (
    InsightFlowPipeline
)

from app.dashboard.dashboard_state import (
    DashboardState
)


class UploadPage:

    @staticmethod
    def render():

        st.title(
            "📂 Upload Organizational Data"
        )

        st.write(
            """
            Upload organizational documents
            for intelligence analysis.
            Supported formats:

            TXT, CSV, PDF, MP3, WAV, M4A
            """
        )

        uploaded_files = st.file_uploader(

            "Upload files",

            accept_multiple_files=True,

            type=[
                "txt",
                "csv",
                "pdf",
                "mp3",
                "wav",
                "m4a"
            ]
        )

        if uploaded_files:

            st.success(

                f"{len(uploaded_files)} files selected"

            )

        if st.button(

            "🚀 Run Analysis",

            use_container_width=True

        ):

            if not uploaded_files:

                st.warning(

                    "Please upload files first."
                )

                return

            upload_dir = Path(
                "data/uploads"
            )

            upload_dir.mkdir(

                parents=True,

                exist_ok=True

            )

            for file in uploaded_files:

                file_path = (

                    upload_dir
                    /
                    file.name

                )

                with open(

                    file_path,

                    "wb"

                ) as f:

                    f.write(
                        file.getbuffer()
                    )

            with st.spinner(

                "Analyzing organization..."

            ):

                pipeline = (

                    InsightFlowPipeline()

                )

                results = (

                    pipeline.run_folder(
                        "data/uploads"
                    )

                )

                DashboardState.set_results(
                    results
                )

            st.success(

                "Analysis completed successfully!"
            )

            st.info(

                "Navigate to Analysis, Trends, or Recommendations pages."
            )