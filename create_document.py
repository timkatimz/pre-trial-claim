from datetime import date

from docx import Document
from docx.shared import Cm
from docxtpl import DocxTemplate

date = date.today().strftime('%d.%m.%Y')
print(date)

doc = DocxTemplate('claim.docx')

context = {'document_number': f'ИСХ №985/55 от {date}', 'debtor_inn': 1454564564,
           'debtor_name': "Семенеев Тимур Наильевич",
           'debtor_address': "545646, Самарская обл., г.Тольятти, ул.Автостроителей, дом 36, кв. 85",
           'debtor_debt_sum': "8854 (восемь тысяч восемьсот пятьдесят черыре) рублей 00 копеек",
           'delivery_docs': "(УПД): №  1253 от 22.04.2019 г.", 'client_name': "ООО ПКПВА", 'client_inn': 6565653232,
           'client_kpp': 44564564456, 'client_bank_bik': 121231231231, 'client_current_account': 1465486542515486445423,
           'client_bank_name': "АО Сбербанк москва".upper(), 'client_correspondent_account': 546545341321454654234564}


doc.render(context)
doc.save('new_claim.docx')

document = Document('new_claim.docx')

#changing the page margins
sections = document.sections
for section in sections:
    section.top_margin = Cm(1)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(3)
    section.right_margin = Cm(2)

document.save('new_claim.docx')












