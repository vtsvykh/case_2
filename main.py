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
print(ru.QSTN_5)
print(ru.CHOICE)
ans_5 = input()
if ans_5 == '1':
  print(ru.QSTN_5_1)
  slr = float(input())
  print(ru.QSTN_5_2)
  time = float(input())
  rslt_2 = slr * time
elif ans_5 == '2':
  print(ru.NOT_TAKEN)
  rslt_2 = 0

# Tax devident
print(ru.QSTN_6)
print(ru.CHOICE)
ans_6 = input()
if ans_6 == '1':
  print(ru.QSTN_6_1)
  rslt_3 = float(input())
elif ans_6 == '2':
  print(ru.NOT_TAKEN)
  rslt_3 = 0
# Tax rent
print(ru.QSTN_7)
print(ru.CHOICE)
ans_7 = input()
if ans_7 == '1':
  print(ru.QSTN_7_1)
  rslt_4 = float(input())
elif ans_7 == '2':
  print(ru.NOT_TAKEN)
  rslt_4 = 0

# Tax prize
print(ru.QSTN_8)
print(ru.CHOICE)
ans_8 = input()
if ans_8 == '1':
  print(ru.QSTN_8_1)
  ans_8_1 = input()
  if ans_8_1 == '1':
    print(ru.QSTN_8_2)
    prz_1 = float(input())
    print(ru.QSTN_8_1_2)
    ans_8_1_2 = input()
    if ans_8_1_2 == '1':
      print(ru.QSTN_8_2)
      prz_2 = float(input())
      prz_1 = prz_1
      prz_3 = 0
      print(ru.QSTN_8_1_6)
      print(ru.CHOICE)
      ans_8_1_3 = input()
      if ans_8_1_3 == '1':
        print(ru.QSTN_8_2)
        prz_1 = prz_1
        prz_2 = prz_2
        prz_3 = float(input())
      elif ans_8_1_3 == '2':
        prz_1 = prz_1
        prz_2 = prz_2
        prz_3 = 0
    elif ans_8_1_2 == '2':
      print(ru.QSTN_8_2)
      prz_3 = float(input())
      prz_1 = prz_1
      prz_2 = 0
      print(ru.QSTN_8_1_7)
      print(ru.CHOICE)
      ans_8_1_7 = input()
      if ans_8_1_7 == '1':
        print(ru.QSTN_8_2)
        prz_1 = prz_1
        prz_2 = float(input())
        prz_3 = 0
      elif ans_8_1_7 == '2':
        prz_1 = prz_1
        prz_2 = 0
        prz_3 = prz_3
    elif ans_8_1_2 == '3':
      prz_1 = prz_1
      prz_2 = 0
      prz_3 = 0
  elif ans_8_1 == '2':
    print(ru.QSTN_8_2)
    prz_2 = float(input())
    print(ru.QSTN_8_1_3)
    ans_8_1_3 = input()
    if ans_8_1_3 == '1':
      print(ru.QSTN_8_2)
      prz_1 = float(input())
      prz_2 = prz_2
      prz_3 = 0
      print(ru.QSTN_8_1_6)
      print(ru.CHOICE)
      ans_8_1_6 = input()
      if ans_8_1_6 == '1':
        print(ru.QSTN_8_2)
        prz_1 = prz_1
        prz_2 = prz_2
        prz_3 = float(input())
    elif ans_8_1_3 == '2':
      print(ru.QSTN_8_2)
      prz_3 = float(input())
      prz_2 = prz_2
      prz_1 = 0
      print(ru.QSTN_8_1_5)
      print(ru.CHOICE)
      ans_8_1_5 = input()
      if ans_8_1_5 == '1':
        print(ru.QSTN_8_2)
        prz_1 = float(input())
        prz_2 = prz_2
        prz_3 = prz_3
      elif ans_8_1_5 == '2':
        prz_1 = 0
        prz_2 = prz_2
        prz_3 = prz_3
    elif ans_8_1_3 == '3':
      prz_1 = 0
      prz_2 = prz_2
      prz_3 = 0
  elif ans_8_1 == '3':
    print(ru.QSTN_8_2)
    prz_3 = float(input())
    print(ru.QSTN_8_1_4)
    ans_8_1_4 = input()
    if ans_8_1_4 == '1':
      print(ru.QSTN_8_2)
      prz_1 = float(input())
      prz_3 = prz_3
      prz_2 = 0
      print(ru.QSTN_8_1_7)
      print(ru.CHOICE)
      ans_8_1_8 = input()
      if ans_8_1_8 == '1':
        print(ru.QSTN_8_2)
        prz_1 = prz_1
        prz_2 = float(input())
        prz_3 = prz_3
      elif ans_8_1_8 == '2':
        prz_1 = prz_1
        prz_2 = 0
        prz_3 = prz_3
    elif ans_8_1_4 == '2':
      print(ru.QSTN_8_2)
      prz_2 = float(input())
      prz_3 = prz_3
      prz_1 = 0
      print(ru.QSTN_8_1_5)
      print(ru.CHOICE)
      ans_8_1_9 = input()
      if ans_8_1_9 == '1':
        print(ru.QSTN_8_2)
        prz_1 = float(input())
        prz_2 = prz_2
        prz_3 = prz_3
    elif ans_8_1_4 == '3':
      prz_1 = 0
      prz_2 = 0
      prz_3 = prz_3
elif ans_8 == '2':
  prz_1 = 0
  prz_2 = 0
  prz_3 = 0

# Sum amount
if ans_1 == '1' and ans_2 == '2' or ans_1 == '2' and ans_3 == '1':
    gnrl_rslt_2 = incm_prprt + incm_prprt_2 + rslt_2 + rslt_4 + prz_1 + prz_2 + prz_3
    tx_incm = gnrl_rslt_2 * 0.3
    tx_dvdnt = rslt_3 * 0.15
    tx = tx_dvdnt + tx_incm
    print(ru.ANS_3, tx)
    print(ru.ANS_2)
elif ans_1 == '1' and ans_2 == '1' or ans_1 == '2' and ans_3 == '2':
    gnrl_rslt_1 = incm_prprt + incm_prprt_2 + rslt_2 + rslt_3 + rslt_4 + prz_1 + prz_2 + prz_3
    if gnrl_rslt_1 >= 5000000:
        part_1 = (incm_prprt + incm_prprt_2 + rslt_2 + rslt_3 + prz_3) * 0.15
        part_2 = (rslt_4 + prz_2) * 0.13
        part_3 = prz_1 * 0.35
        tx = part_1 + part_2 + part_3
        print(ru.ANS_1, tx)
        print(ru.ANS_2)
    elif gnrl_rslt_1 < 5000000:
        part_1_1 = (incm_prprt + incm_prprt_2 + rslt_2 + rslt_3 + rslt_4 + prz_2 + prz_3) * 0.13
        part_3_1 = prz_1 * 0.35
        gnrl_part_1 = part_1_1 + part_3_1
        print(ru.ANS_1, gnrl_part_1)
        print(ru.ANS_2)