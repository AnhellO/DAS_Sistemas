def p_decorate_textonormal(func):

   def func_wrapper(*args,**kwargs):
       return "{0}".format(func(*args, **kwargs))
   return func_wrapper

def p_decorate_textoresultado(func):

   def func_wrapper(*args,**kwargs):
       return "<b>{0}</b>".format(func(*args, **kwargs))
   return func_wrapper

def p_decorate_textoreusltadoysub(func):

   def func_wrapper(*args,**kwargs):
       return "<b><u>{0}</u></b>".format(func(*args, **kwargs))
   return func_wrapper

def p_decorate_aplicando(func):

   def func_wrapper(*args,**kwargs):
       return "<b><u><i>{0}</i></u></b>".format(func(*args, **kwargs))
   return func_wrapper

class TextRenderer(object):
    def __init__(self):
        self.tn = "¡Texto normal!"
        self.tr = "¡Texto Resaltado!"
        self.trs = "¡Texto Resaltado y Subrayado!"
        self.ap = "¡Aplicando todos los formatos!"


    @p_decorate_textonormal
    def get_textosolo(self):
        return self.tn

    @p_decorate_textoresultado
    def get_textoresultado(self):
    	return self.tr

    @p_decorate_textoreusltadoysub
    def get_textoresultadoysub(self):
    	return self.trs

    @p_decorate_aplicando
    def get_aplicando(self):
    	return self.ap

if __name__ == '__main__':
	my_textrender = TextRenderer()

	print (my_textrender.get_textosolo())
	print (my_textrender.get_textoresultado())
	print (my_textrender.get_textoresultadoysub())
	print (my_textrender.get_aplicando())

