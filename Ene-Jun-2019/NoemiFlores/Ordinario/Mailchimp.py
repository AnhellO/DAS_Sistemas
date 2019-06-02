from mailchimp3 import MailChimp

client = MailChimp(mc_api='c01763c6ce32153a498813b2bc612d94-us20')
usuarios = [('angelica_marc@hotmail.com', 'ANGELICA MARÍA', 'RODRÍGUEZ CABELLO'),
('erikmontoya15@Icloud.com', 'ERIK EDUARDO', 'MONTOYA MARTÍNEZ'),
('luis_al_or@hotmail.com', 'LUIS ALBERTO', 'ORNELAS HINOJOSA'),
('joseaperaltav@hotmail.com', 'JOSE ALBERTO', 'PERALTA VALDÉS'),
('jdac_06@hotmail.com', 'JUAN DE DIOS', 'ALMAGUER CONSTANTE'),
('karla_berlanga28@hotmail.com', 'KARLA JANETH', 'BERLANGA VÁZQUEZ'),
('asjz2892@gmail.com', 'ANGEL SANTIAGO', 'JAIME ZAVALA')]
for email, first_name, last_name in usuarios:
    client.lists.members.create('561e838f6d', {
    'email_address': email,
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': first_name,
        'LNAME': last_name,
    },
})