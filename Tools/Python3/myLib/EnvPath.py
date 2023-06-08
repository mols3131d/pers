def envPath(dict_path=None):
    import platform
    from pprint import pprint

    global root_path
    global data_path

    dict_path_default = {
        "Windows": {"root_path": ".", "data_path": "data"},
        "Google_Colab": {"root_path": "../gdrive/MyDrive", "data_path": "data"},
        "Kaggle_notebook": {"root_path": "..", "data_path": "input"},
    }
    # 추후에 dict_path에 Kaggle_notebook이 없으면 추가하는 코드 추가 요망
    if dict_path != None:
        for k, v in dict_path.items():
            dict_path_default[k] = v

    dict_path = dict_path_default


    env = platform.uname().system

    if env == "Windows":
        env = env

    elif env == "Linux":
        import sys

        # Google_Colab
        if "google.colab" in sys.modules:
            env = "Google_Colab"
            from google.colab import drive

            drive.mount("/gdrive", force_remount=True)

        # Kaggle_notebook
        else:
            import os

            if list(os.walk("/kaggle/"))[0][1] == ["lib", "input", "working"]:
                env = "Kaggle_notebook"

    root_path = dict_path[env]["root_path"]
    data_path = f"{root_path}/{dict_path[env]['data_path']}"
    print("▣ env :", env)
    print()
    print("▣ platform.uname()", "\n", platform.uname(), sep="")
    print()
    print("▣ data_path", "\n", data_path, sep="")


# path ---- ---- ---- ----
envPath()
# train_file = "train.csv"
# test_file = "test.csv"

# train_path = f"{data_path}/{train_file}"
# test_path = f"{data_path}/{test_file}"
# print()
# print("▣ train_path")
# print(train_path)
# print()
# print("▣ test_path")
# print(test_path)