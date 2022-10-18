from datetime import date
from docxtpl import DocxTemplate

date = date.today().strftime('%d.%m.%Y')

doc = DocxTemplate('claim.docx')

context = {'docnum': f'ИСХ №985/55 от {date}',
           'debtor_inn': 1454564564,
           'debtor_name': "Иванов Иван Иванович",
           'debtor_address': "545646, Самарская обл., г.Тольятти, ул.Улица, дом 36, кв. 85",
           'debtor_debt_sum': "8854 (восемь тысяч восемьсот пятьдесят черыре) рублей 00 копеек",
           'delivery_docs': "(УПД): №  1253 от 22.04.2019 г.",
           'client_name': "ООО ПКПВА", 'client_inn': 6565653232,
           'client_kpp': 44564564456, 'client_bank_bik': 121231231231,
           'client_current_account': 1465486542515486445423,
           'client_bank_name': "АО Сбербанк москва".upper(),
           'client_correspondent_account': 546545341321454654234564,
           'debtor_email': 'tim@semeneev.ru'
           }

doc.render(context)
doc.save('final.docx')
#
# doc = Document('final.doc')
#
# sections = doc.sections
#
# for section in sections:
#     section.headers_distance = Cm(1)
#     section.footers_distance = Cm(1)
#     section.top_margin = Cm(1)
#     section.bottom_margin = Cm(1)
#     section.left_margin = Cm(1)
#     section.right_margin = Cm(1)
#
# doc.save('final.docx')
