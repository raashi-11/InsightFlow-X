from app.pipeline.insightflow_pipeline import (
    InsightFlowPipeline
)

pipeline = (
    InsightFlowPipeline()
)

results = pipeline.run(

    "data/raw/customer_feedback.txt"

)

print("\n")

print(
    results["report"]
)