import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def DP_after_DC(
    df: pd.DataFrame,
    colName_dict: dict = None,  # type: ignore
    colName_order_list: list = None,  # type: ignore
) -> pd.DataFrame:

    """함수 설명
    DC(데이터 수집) 후, DP(데이터 전처리)하는 함수
    """

    # 1. 컬럼명 재선언
    def DPrename_col(
        df: pd.DataFrame, colName_dict: dict = None  # type: ignore
    ) -> pd.DataFrame:

        if colName_dict is not None:
            col_list = colName_dict.keys()
            dict = {}
            for k, v in colName_dict.items():
                if k in col_list:
                    dict[k] = v
            df.rename(columns=dict, inplace=True)
        return df

    # 2. 컬럼명 재배치
    def DPreplace_col(
        df: pd.DataFrame, colName_order_list: list = None  # type: ignore
    ) -> pd.DataFrame:

        if colName_order_list is not None:
            tmp_list_1 = []
            tmp_list_2 = []
            for i in df.columns():  # type: ignore
                if i in colName_order_list:
                    tmp_list_1.append(i)
                else:
                    tmp_list_2.append(i)
            tmp_list = tmp_list_1 + tmp_list_2
            df = df[tmp_list]
        return df

    df = DPrename_col(df, colName_dict)
    df = DPreplace_col(df, colName_order_list)

    return df


def DP_after_read_csv(
    df: pd.DataFrame,
    colType_dict: dict = None,  # type: ignore
    col_zfill_dict: dict = None,  # type: ignore
) -> pd.DataFrame:

    """함수 설명
    CSV로 불러온 Pandas.DataFrame을 DP(데이터 전처리)하는 함수
    """

    # 컬럼값 타입 재설정
    def DPretype_col(
        df: pd.DataFrame, colType_dict: dict = None  # type: ignore
    ) -> pd.DataFrame:

        if colType_dict is not None:

            col_list = colType_dict.keys()

            for i in col_list:
                if i in df.columns():  # type: ignore
                    df[i] = df[i].astype(colType_dict[i])

        return df

    # zfill
    def DPzfill_coll(
        df: pd.DataFrame, col_zfill_dict: dict = None  # type: ignore
    ) -> pd.DataFrame:

        if col_zfill_dict is not None:

            col_list = colType_dict.keys()

            for i in col_list:
                if i in df.columns():  # type: ignore
                    df[i] = df[i].astype(str).zfill(col_zfill_dict[i])

        return df

    df = DPretype_col(df, colType_dict)
    df = DPzfill_coll(df, col_zfill_dict)

    return df


# def fn(dict: dict, list: list = []):
#     if list == []:
#         list = dict.keys()

#     tmp = {}
#     for k, v in dict_agg.items():
#         if k in list:
#             tmp[k] = v
#     return tmp

# df1 = df
# df1 = df1.groupby(options1)[options2].aggregate(fn(dict_agg))


# df["corp_code"] = df["corp_code"].astype(str).apply(lambda x: x.zfill(8))
# df["stock_code"] = df["stock_code"].astype(str).apply(lambda x: x.zfill(6))


# 귀찮은거
def CheckDf(df: pd.DataFrame):

    # vnames = [name for name in globals() if globals()[name] is df][0]
    vnames = "df"

    line = " ----- " * 10

    print(f"┌▣ {vnames}.shape" + line)
    display(df.shape)

    print("\n\n" + f"┌▣ {vnames}.sample" + line + "\n|")
    display(df.sample(10))

    print("\n\n" + f"┌▣ {vnames}.info()" + line + "\n|")
    display(df.info())

    print("\n\n" + f"┌▣ {vnames}.describe()" + line + "\n|")
    display(df.describe())

    if "object" in df.dtypes.values:
        print("\n\n" + f"┌▣ {vnames}.describe(include='object')" + line + "\n|")
        display(df.describe(include="object"))

    if "category" in df.dtypes.values:
        print("\n\n" + f"┌▣ {vnames}.describe(include='category')" + line + "\n|")
        display(df.describe(include="category"))

    print("\n\n" + f"┌▣ {vnames}.isnull().sum()" + line + "\n|")
    display(df.isnull().sum())

    print("\n\n" + f"┌▣ {vnames}.isnull().mean()" + line + "\n|")
    display(df.isnull().mean())

    sns.heatmap(df.isnull(), cmap="gray")

    print(
        "\n\n" + f"┌▣ {vnames}[{vnames}.duplicated()].shape[0] & head(5)" + line + "\n|"
    )
    display(df[df.duplicated()].shape[0])
    display(df[df.duplicated()].head())



# 환경
import platform
env = platform.uname().system

workdir_path = r"."
data_path = fr"{workdir_path}/data"
if env == "Windows":
    env = env
    # if platform.uname().node == '':

elif env == "Linux":
    import sys

    if 'google.colab' in sys.modules:
        env = "Google Colab"

        from google.colab import drive
        drive.mount('/gdrive', force_remount=True)

        workdir_path = r"/gdrive/MyDrive/[2022_0914~2023_0113]    Likelion AI School 7/_1_corazzon - Data Analytics with Python/_project/Monthly Daycon Psychological Prediction AI Competition"
        data_path = fr"{workdir_path}/data"
    elif:
        import os
        list(os.walk('/kaggle/'))[0][0] == '/kaggle/'
        env = "Kaggle notebook"