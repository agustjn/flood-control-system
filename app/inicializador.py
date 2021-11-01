from app.models.permission import Role, Permission
from app.models.user import User
from app.db import db

usuario_index = Permission(name="usuario_index")

#Configuracion_index permite a un admin y solo a un admin ingresar a la seccion de configuracin y a todas las acciones
configuracion_index = Permission(name="configuracion_index")

#Punto_encuentro_index: Permite acceder al index (listado) del modulo
punto_encuentro_index = Permission(name="puntos_encuentro_index")

#puntos_encuentro_update: Permite actualizar una zona inundable-
puntos_encuentro_update = Permission(name = "puntos_encuentro_update")


#puntos_encuentro_destroy: Permite borrar una zona inundable
puntos_encuentro_destroy = Permission(name = "puntos_encuentro_destroy")

#puntos_encuentro_new: Permite cargar una sona inundable:
puntos_encuentro_new = Permission(name = "puntos_encuentro_new")

#Agrego los permisos a la base de datos
db.session.add(usuario_index)
db.session.add(configuracion_index)
db.session.add(puntos_encuentro_update)
db.session.add(punto_encuentro_index)
db.session.add(puntos_encuentro_destroy)
db.session.add(puntos_encuentro_new)
db.session.commit()

#Creo roles

#Rol del administrador
rol_administrador = Role(name="administrador")

#Relacion del rol administrador con sus permisos
rol_administrador.permission.append(usuario_index)
rol_administrador.permission.append(configuracion_index)
rol_administrador.permission.append(punto_encuentro_index)
rol_administrador.permission.append(puntos_encuentro_new)
rol_administrador.permission.append(puntos_encuentro_destroy)
rol_administrador.permission.append(puntos_encuentro_update)
db.session.commit()





usuario_admin = User('cosme', 'Fulanito', 'admin', 'admin', '123123')
usuario_admin.role.append(rol_administrador)
db.session.commit()
