from mailchimp3 import MailChimp

cliente = MailChimp(mc_api='a077d47e4472399e14776a6a56019392-us20')
usuarios = [('nooemii.chaaparra@gmail.com', 'NOEMI ESTHER', 'FLORES PARDO'),
('angelica_marc@hotmail.com', 'ANGELICA MARÍA', 'RODRÍGUEZ CABELLO'),
('erikmontoya15@Icloud.com', 'ERIK EDUARDO', 'MONTOYA MARTÍNEZ'),
#('luis_al_or@hotmail.com', 'LUIS ALBERTO', 'ORNELAS HINOJOSA'),
('joseaperaltav@hotmail.com', 'JOSE ALBERTO', 'PERALTA VALDÉS'),
('jdac_06@hotmail.com', 'JUAN DE DIOS', 'ALMAGUER CONSTANTE'),
('karla_berlanga28@hotmail.com', 'KARLA JANETH', 'BERLANGA VÁZQUEZ'),
('asjz2892@gmail.com', 'ANGEL SANTIAGO', 'JAIME ZAVALA')]
for email, first_name, last_name in usuarios:
    cliente.lists.members.create('ee90e4fbab', {
    'email_address': email,
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': first_name,
        'LNAME': last_name,
    },
})
