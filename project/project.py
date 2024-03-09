import openai


class Project:
    """
    Project Class
    """

    def __init__(self, api_key):
        openai.api_key = api_key

    def my_method(self):
        """
        Some Method
        """
        results = "results!"

        return {
            "results": results,
        }