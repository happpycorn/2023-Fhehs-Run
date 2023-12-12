2023 芳和越野路跑 參與紀錄

import gramin_run官網 # https://www.garmin.com.tw/event/2023/garmin-run/index.html
import 協作平台
import gcp_function
import ChatGPT
import 過去失敗的Line機器人 as 過去的經驗

作者 = 許博智
組別 = 競賽組

def 負責工作():

  網頁搭建 = [
    "網頁架構":協作平台.匯入(garmin_run官網.網站架構),
    "網頁內容":"協助製作",
    "成績查詢":成績查詢()
    ]

def 成績查詢():

  code = ChatGPT.詢問()
  嘗試(code)
  協作平台.發布測試()

def 嘗試(code):
  try:
    協作平台.嵌入(gcp_function.伺服器(code))
    return OK!
  except:
    除錯的方法 = 過去的經驗.排除(引入的錯誤) + ChatGPT.詢問(兩周)
    code.gcp_function.程式(除錯的方法)
    return 嘗試(code)

print(gramin_run官網.網址)
