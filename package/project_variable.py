import os

workDir = os.path.abspath("../")

name = {"data": "data", "DART_corpCode": "DART_corpCode"}

dir = {"workDir": workDir, "data": rf"""{workDir}/{name["data"]}"""}

# def get_relpath




# ---------------------------------------------------------------------------------
colName_dict = {
    # corpCode
    "stock_code": "종목코드",
    "corp_code": "DART_고유번호",
    "corp_name": "종목명",
    "modify_date": "DART_고유번호_최근변경일자",
    "jurir_no": "법인등록번호",
    # finaInfo
    "basDt": "기준일자",
    "crno": "법인등록번호",
    "bizYear": "사업연도",
    "fnclDcd": "재무제표구분코드",
    "fnclDcdNm": "재무제표구분코드명",
    "enpSaleAmt": "기업매출금액",
    "enpBzopPft": "기업영업이익",
    "iclsPalClcAmt": "포괄손익계산금액",
    "enpCrtmNpf": "기업당기순이익",
    "enpTastAmt": "기업총자산금액",
    "enpTdbtAmt": "기업총부채금액",
    "enpTcptAmt": "기업총자본금액",
    "enpCptlAmt": "기업자본금액",
    "fnclDebtRto": "재무제표부채비율"
}


# important
#   index_date
#   index_corp
# not important
#   index_corp
#   finaStatInfo
colName_order_list = [
    colName_dict["stock_code"],
    colName_dict["corp_name"],
    colName_dict["jurir_no"],
    colName_dict["corp_code"],
    colName_dict["modify_date"],
    "사업연도",
    "재무제표구분코드",
    "재무제표구분코드명",
    "기업매출금액",
    "기업영업이익",
    "포괄손익계산금액",
    "기업당기순이익",
    "기업총자산금액",
    "기업총부채금액",
    "기업총자본금액",
    "기업자본금액",
    "재무제표부채비율",
]

col_zfill_dict = {"종목코드": 6, "DART_고유번호": 8, "법인등록번호": 13}
