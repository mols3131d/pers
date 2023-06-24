import platform
import sys
import os


class envPath:
    def __init__(self):
        # os
        self.os = platform.uname().system

        # env
        if self.os == "Linux":
            # Google_Colab
            if "google.colab" in sys.modules:
                from google.colab import drive

                drive.mount("/content/drive", force_remount=True)
                self.env = "Google_Colab"
            # Kaggle_notebook
            elif list(os.walk("/kaggle/"))[0][1] == [
                "lib",
                "input",
                "working",
            ]:
                self.env = "Kaggle_notebook"
        else:
            self.env = self.os

        # root
        self.root = os.getcwd()

        if self.env == "Google_Colab":
            self.root = "../content"
            self.root = "../content/drive/MyDrive"

        # data
        self.data = f"{self.root}/data"

    def __str__(self) -> str:
        return str(platform.uname())
