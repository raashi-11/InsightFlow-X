class DashboardState:

    analysis_results = None

    @classmethod
    def set_results(

        cls,

        results

    ):

        cls.analysis_results = (
            results
        )

    @classmethod
    def get_results(
        cls
    ):

        return (
            cls.analysis_results
        )