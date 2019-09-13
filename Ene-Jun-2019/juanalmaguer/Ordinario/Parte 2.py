from mailchimp3 import MailChimp

client = MailChimp(mc_api='f712656d158a38831674570ed92f04e3-us20')
users = [('nooemii.chaaparra@gmail.com', 'NOEMI ESTHER', 'FLORES PARDO'),
('angelica_marc@hotmail.com', 'ANGELICA MARÍA', 'RODRÍGUEZ CABELLO'),
('erikmontoya15@Icloud.com', 'ERIK EDUARDO', 'MONTOYA MARTÍNEZ'),
('luis_al_or@hotmail.com', 'LUIS ALBERTO', 'ORNELAS HINOJOSA'),
('joseaperaltav@hotmail.com', 'JOSE ALBERTO', 'PERALTA VALDÉS'),
#('jdac_06@hotmail.com', 'JUAN DE DIOS', 'ALMAGUER CONSTANTE')
('karla_berlanga28@hotmail.com', 'KARLA JANETH', 'BERLANGA VÁZQUEZ'),
('asjz2892@gmail.com', 'ANGEL SANTIAGO', 'JAIME ZAVALA')]
for mail, f_name, l_name in users:
    client.lists.members.create('c0df0707ec', {
    'email_address': mail,
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': f_name,
        'LNAME': l_name,
    },
})
