--Obtener/seleccionar todos los emails existentes en la base de datos
select email from users;

--Contar cuantas mujeres existen al final en la base de datos
select count(*) from users where gender = 0;

--Contar cuantos hombres existen al final en la base de datos
select count(*) from users where gender = 1;

--Obtener todos usuarios existentes en la base de datos mostrando solamente su nombre completo, su email, y su dirección
select (title ||' ' || first ||' '||last) as name, email, ('Street: ' ||street||' | City: '||city||' | State: '||state) as location from users;