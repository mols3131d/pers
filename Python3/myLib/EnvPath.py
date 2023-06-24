import platform
import sys
import os


class envPath:
    def __init__(self, root_path=None, env=None):
        self.os = platform.uname().system

        if env == None:
            if self.os == "Linux":
                # Google_Colab
                if "google.colab" in sys.modules:
                    from google.colab import drive

                    drive.mount("/gdrive", force_remount=True)
                    self.env = "Google_Colab"
                    if root_path == None:
                        self.root = "../gdrive/MyDrive"

                # Kaggle_notebook
                elif list(os.walk("/kaggle/"))[0][1] == ["lib", "input", "working"]:
                    self.env = "Kaggle_notebook"
                    if root_path == None:
                        self.root = "./kaggle/input"
            else:
                self.env = self.os
                if root_path == None:
                    self.root = "."

    def __str__(self) -> str:
        return str(platform.uname())
