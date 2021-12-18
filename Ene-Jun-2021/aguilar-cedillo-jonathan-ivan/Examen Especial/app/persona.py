class Persona: 
    def __init__(self, id, first_name, last_name, company, email, ip_address, phone_number): 
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.email = email
        self.ip_address = ip_address
        self.phone_number = phone_number

    def persona(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'company':self.company,
            'email':self.email,
            'ip_address':self.ip_address,
            'phone_number':self.phone_number
        }

# p= Persona('1','jonathan','Aguilar','trabajo','correo@correo.com', '172.0.0.1','8888888888')
# print(p.persona())