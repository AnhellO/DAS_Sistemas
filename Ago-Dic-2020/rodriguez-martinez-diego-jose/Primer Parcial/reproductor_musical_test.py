import unittest
from Ejercicio1 import ReproductorMusical, Pista

class ReproductorMusical_test(unittest.TestCase):
    def test_getCanciones_vacia(self):
        canciones = []
        my_reproductor = ReproductorMusical(canciones)

        self.assertEqual(my_reproductor.get_canciones(), [])

    def test_agregarPista_queueVacia(self):
        canciones = []
        my_reproductor = ReproductorMusical(canciones)
        my_reproductor.agregar_pista(Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31))

        self.assertEqual(my_reproductor.get_canciones(), [["Godzilla","Eminem", 3.31]])
    
    def test_agregarPistaVacia_queueVacia(self):
        canciones = []
        my_reproductor = ReproductorMusical(canciones)
        my_reproductor.agregar_pista(Pista())

        self.assertEqual(my_reproductor.get_canciones(), [["Untitled","Artista Desconocido", 0.0]])

    def test_informacionCanciones(self):
        informacion = "##### INFORMACION DE GODZILLA #####\nNombre: Godzilla\nFavorita: True\nDuracion: 3.31\nArtista: Eminem\n"
        my_reproductor = ReproductorMusical([Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31)])

        self.assertEqual(my_reproductor.informacion_de_pistas(), informacion)
    
    def test_cancionesFavoritas_vacia(self):
        my_reproductor = ReproductorMusical( [Pista(nombre = "Godzilla", artista = "Eminem", favorita= False, duracion = 3.31),
                                            Pista(nombre = "Cancion1", favorita = False),
                                            Pista() ] )

        self.assertEqual(my_reproductor.get_canciones_favoritas(), [])
    
    def test_cancionesFavoritas(self):
        my_reproductor = ReproductorMusical( [Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31),
                                            Pista(nombre = "Cancion1", favorita = True),
                                            Pista() ] )

        self.assertEqual(my_reproductor.get_canciones_favoritas(),["Godzilla","Cancion1"])        

    def test_quitarCancion(self):
        my_reproductor = ReproductorMusical( [Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31),
                                            Pista(nombre = "Cancion1", favorita = True),
                                            Pista() ] )
        
        esperado = [["Cancion1","Artista Desconocido", 0.0],["Untitled","Artista Desconocido", 0.0]]

        my_reproductor.quitar_pista()
        self.assertEqual(my_reproductor.get_canciones(), esperado)
    
    def test_quitarCancion_Indice(self):
        my_reproductor = ReproductorMusical( [Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31),
                                            Pista(nombre = "Cancion1", favorita = True),
                                            Pista() ] )
        
        esperado = [["Untitled","Artista Desconocido", 0.0],["Godzilla","Eminem", 3.31]]

        my_reproductor.quitar_pista(1)
        self.assertEqual(my_reproductor.get_canciones(), esperado)
    
    def test_quitarCancion_Nombre(self):
        my_reproductor = ReproductorMusical( [Pista(nombre = "Godzilla", artista = "Eminem", favorita= True, duracion = 3.31),
                                            Pista(nombre = "Cancion1", favorita = True),
                                            Pista() ] )
        
        esperado = [["Cancion1","Artista Desconocido",0.0],["Untitled","Artista Desconocido", 0.0]]

        my_reproductor.quitar_pista(nombre="Godzilla")
        self.assertEqual(my_reproductor.get_canciones(), esperado)
    
    def test_quitarCancion_vacia(self):
        canciones = []
        my_reproductor = ReproductorMusical(canciones)

        with self.assertRaises(ValueError):
            my_reproductor.quitar_pista()


