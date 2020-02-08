from mailchimp3 import MailChimp

# Este codigo esta diseñado para ser ejecutado solamente una vez.
# Para volver a ejecutarlo sería necesario eliminar a todos los usuarios cuyos correos ya están registrados.
# Otra alternativa es cambiar las credenciales e inscribir a los usuarios a una lista (audiencia) diferente.

client = MailChimp(mc_api='c4426529cccf0937dc4d3cb058e72917-us20')
users = [('nooemii.chaaparra@gmail.com', 'NOEMI ESTHER', 'FLORES PARDO'),
('angelica_marc@hotmail.com', 'ANGELICA MARÍA', 'RODRÍGUEZ CABELLO'),
('erikmontoya15@Icloud.com', 'ERIK EDUARDO', 'MONTOYA MARTÍNEZ'),
('luis_al_or@hotmail.com', 'LUIS ALBERTO', 'ORNELAS HINOJOSA'),
('joseaperaltav@hotmail.com', 'JOSE ALBERTO', 'PERALTA VALDÉS'),
('jdac_06@hotmail.com', 'JUAN DE DIOS', 'ALMAGUER CONSTANTE'),
('karla_berlanga28@hotmail.com', 'KARLA JANETH', 'BERLANGA VÁZQUEZ'),
('asjz2892@gmail.com', 'ANGEL SANTIAGO', 'JAIME ZAVALA')]
for mail, f_name, l_name in users:
    client.lists.members.create('b2ebb38ade', {
    'email_address': mail,
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': f_name,
        'LNAME': l_name,
    },
})
