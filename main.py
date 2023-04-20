"""
"Case 2"
Group:
Fishchukova Sofia
Tsvykh Viktoria
"""




import datetime as DT
import ru_local as ru

# Resident or nor resident
print(ru.QSTN_1)
print(ru.CHOICE)
ans_1 = input()
if ans_1 == '1':
  print(ru.QSTN_2)
  print(ru.CHOICE)
  ans_2 = input()
  if ans_2 == '1' :
    print(ru.RSDNT)
  elif ans_2 == '2':
    print(ru.NOT_RSDNT)
elif ans_1 == '2':
  print(ru.QSTN_3)
  print(ru.CHOICE)
  ans_3 = input()
  if ans_3 == '1':
    print(ru.NOT_RSDNT)
  elif ans_3 == '2':
    print(ru.RSDNT)
# Tax property
print(ru.QSTN_4)
print(ru.CHOICE)
ans_4 = input()
if ans_4 == '1':
  print(ru.QSTN_4_1)
  print(ru.CHOIS_PRPRT)
  ans_4_1 = input()
  if ans_4_1 == '1':
    print(ru.QSTN_4_2)
    ans_4_2 = int(input())
    if 2023 - ans_4_2 > 5 :
      print(ru.NOT_TAKEN_2)
      incm_prprt = 0
      incm_prprt_2 = 0
    elif 2023 - ans_4_2 <= 5:
      print(ru.QSTN_4_3)
      incm_prprt = float(input())
      incm_prprt_2 = 0
  elif ans_4_1 == '2':
    print(ru.QSTN_4_2)
    ans_4_3 = int(input())
    if 2023 - ans_4_3 <= 3:
      print(ru.QSTN_4_3)
      incm_prprt_2 = float(input())
      incm_prprt = 0
    elif 2023 - ans_4_3 > 3:
      print(ru.NOT_TAKEN_2)
      incm_prprt_2 = 0
      incm_prprt = 0
  elif ans_4_1 == '3':
    print(ru.QSTN_4_4)
    ans_4_4 = int(input())
    if 2023 - ans_4_4 > 5:
      print(ru.NOT_TAKEN_3)
      incm_prprt = 0
    elif 2023 - ans_4_4 <= 5:
      print(ru.QSTN_4_3)
      incm_prprt = float(input())
    print(ru.QSTN_4_5)
    ans_4_5 = int(input())
    if 2023 - ans_4_5 <= 3:
      incm_prprt_2 = float(input(ru.QSTN_4_3))
    elif 2023 - ans_4_5 > 3:
      print(ru.NOT_TAKEN_4)
      incm_prprt_2 = 0
elif ans_4 == '2':
  print(ru.NOT_TAKEN)
  incm_prprt = 0
  incm_prprt_2 = 0
  incm_prprt_3 = 0
# Tax worker

# Tax devident

# Tax rent

# Tax prize

# Sum amount
if ans_1 == '1' and ans_2 == '2' or ans_1 == '2' and ans_3 == '1':
    gnrl_rslt_2 = incm_prprt + incm_prprt_2 + rslt_2 + rslt_4 + prz_1 + prz_2 + prz_3
    tx_incm = gnrl_rslt_2 * 0.3
    tx_dvdnt = rslt_3 * 0.15
    tx = tx_dvdnt + tx_incm
    print(ru.ANS_3, tx)
    print(ru.ANS_2)