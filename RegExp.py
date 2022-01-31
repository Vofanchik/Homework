from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for contact in contacts_list:
  contact[0:3] = ' '.join(contact[0:3]).split(' ')[0:3]
  phone_pattern = re.compile("\+?7?8?\s?\(?([0-9]{3})\)?\-?\s?([0-9]{3})\-?([0-9]{2})\-?([0-9]{2})")
  new_phone_pattern = "+7(\\1)\\2-\\3-\\4"
  add_phone_pattern = re.compile("\(?(доб\.\s[0-9]{4})\)?")
  new_add_phone_pattern = "\\1"
  contact[5] = re.sub(phone_pattern, new_phone_pattern, contact[5])
  contact[5] =re.sub(add_phone_pattern, new_add_phone_pattern, contact[5])

del_list=[]
for i in range(len(contacts_list)):
  for j in range(i + 1, len(contacts_list)):
      if contacts_list[i][0] == contacts_list[j][0]:
          del_list.append(j)
          for b,c in enumerate(contacts_list[i]):
              if c == '':
                  contacts_list[i][b]= contacts_list[j][b]

for p,s in enumerate(del_list):
    s-=p
    contacts_list.pop(s)





with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    datawriter.writerows(contacts_list)