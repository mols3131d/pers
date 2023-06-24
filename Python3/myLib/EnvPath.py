import platform
import sys
import os


class envPath:
    def __init__(self):
        self.os = platform.uname().system

        if self.os == "Linux":
            # Google_Colab
            if "google.colab" in sys.modules:
                from google.colab import drive

                drive.mount("/gdrive", force_remount=True)
                self.env = "Google_Colab"
                self.root = "../gdrive/MyDrive"

            # Kaggle_notebook
            elif list(os.walk("/kaggle/"))[0][1] == ["lib", "input", "working"]:
                self.env = "Kaggle_notebook"
                self.root = "./kaggle/input"
        else:
            self.env = self.os
            self.root = "./"

    def __str__(self) -> str:
        return str(platform.uname())
