def p_decorateNormal(func):
   def func_decorate(self,):
       return "<¡>{0}<!>".format(func(self))
   return func_decorate

def p_decorateResaltado(func):
   def func_decorate(self,):
       return "<p>{0}</p>".format(func(self))
   return func_decorate

def p_decorateCursiva(func):
   def func_decorate(self,):
       return "<i>{0}</i>".format(func(self))
   return func_decorate

def p_decorateSubrayado(func):
   def func_decorate(self,):
       return "<u>{0}</u>".format(func(self))
   return func_decorate

def p_decorateAll(func):
   def func_decorate(self,):
       return "<b><u><i>{0}</i></u></b>".format(func(self))
   return func_decorate
##############################################################
class TextRenderer(object):
    def __init__(self, text):
        self._text = text
    @p_decorateNormal
    def renderNorm(self):
        return self._text

    @p_decorateResaltado
    def renderRes(self):
        return self._text

    @p_decorateCursiva
    def renderCur(self):
        return self._text

    @p_decorateSubrayado
    def renderSub(self):
        return self._text

    @p_decorateAll
    def renderAll(self):
        return self._text
###############################################################
if __name__ == '__main__':
    renderer = TextRenderer("hola")
    print(renderer.renderNorm())
    print(renderer.renderRes())
    print(renderer.renderCur())
    print(renderer.renderSub())
    print(renderer.renderAll())
