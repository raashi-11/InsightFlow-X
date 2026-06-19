from app.pipeline.insightflow_pipeline import (
    InsightFlowPipeline
)

pipeline = (
    InsightFlowPipeline()
)

results = (

    pipeline.run_folder(
        "data/raw"
    )

)

print("\n")

print(
    "FILES PROCESSED:",
    results["processed_files"]
)

print("\nTHEMES\n")

print(
    results["theme_counts"]
)

print("\nSENTIMENT\n")

print(
    results["sentiment"]
)

print("\nRISK SCORE\n")

print(
    results["risk_score"]
)

print("\nREPORT\n")

print(
    results["report"]
)