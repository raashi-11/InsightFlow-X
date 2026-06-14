class SourceTracker:

    @staticmethod
    def build_source_record(
        metadata,
        chunk_id
    ):

        return {

            "filename":
            metadata["filename"],

            "chunk_id":
            chunk_id,

            "processed_at":
            metadata["processed_at"]
        }