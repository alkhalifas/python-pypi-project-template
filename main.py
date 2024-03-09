"""
Main.py File to Start Application
"""

import os
from project import project


if __name__ == '__main__':
    api_key = os.getenv("OPENAI_API_KEY")

    # Logic
    myproject = project.Project(api_key)

    something = myproject.my_method()

    print(something)


