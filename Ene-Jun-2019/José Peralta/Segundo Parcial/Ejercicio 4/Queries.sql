SELECT Correo FROM Users;

SELECT COUNT(Genero) AS Mujeres FROM Users WHERE Genero='F';
SELECT COUNT(Genero) AS Hombres FROM Users WHERE Genero='M';

SELECT Nombre, Apellido, Correo, Direccion FROM Users;