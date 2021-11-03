from app.models.permission import Role, Permission
from app.models.user import User
from app.db import db
from app.models.point import Point
from app.models.configuration import Configuration
from app.models.views_sort import View

#Creo y agregago la configuraicon

config = Configuration("Amarillo",5)
db.session.add(config)
db.session.commit()

#Creo y agrego las vistas


view_user = View("user","last_name","asc")
view_issue = View("issue","email","desc")
view_meeting_point = View("point","nombre","asc")

db.session.add(view_user)
db.session.add(view_issue)
db.session.add(view_meeting_point)
db.session.commit()



usuario_index = Permission("usuario_index")

usuario_new = Permission("usuario_new")
usuario_update = Permission("usuario_update")
usuario_destroy = Permission("usuario_destroy")


#Configuracion_index permite a un admin y solo a un admin ingresar a la seccion de configuracin y a todas las acciones
configuracion_index = Permission("configuracion_index")

#Punto_encuentro_index: Permite acceder al index (listado) del modulo
punto_encuentro_index = Permission("puntos_encuentro_index")

#puntos_encuentro_update: Permite actualizar una zona inundable-
puntos_encuentro_update = Permission("puntos_encuentro_update")


#puntos_encuentro_destroy: Permite borrar una zona inundable
puntos_encuentro_destroy = Permission("puntos_encuentro_destroy")

#puntos_encuentro_new: Permite cargar una sona inundable:
puntos_encuentro_new = Permission("puntos_encuentro_new")

#Agrego los permisos a la base de datos
db.session.add(usuario_index)
db.session.add(configuracion_index)
db.session.add(puntos_encuentro_update)
db.session.add(punto_encuentro_index)
db.session.add(puntos_encuentro_destroy)
db.session.add(puntos_encuentro_new)

db.session.add(usuario_new)
db.session.add(usuario_update)
db.session.add(usuario_destroy)

db.session.commit()

#Creo roles

#Defino rol administrador
rol_administrador = Role("administrador")

#Relacion del rol administrador con sus permisos
rol_administrador.permission.append(usuario_index)
rol_administrador.permission.append(configuracion_index)
rol_administrador.permission.append(punto_encuentro_index)
rol_administrador.permission.append(puntos_encuentro_new)
rol_administrador.permission.append(puntos_encuentro_destroy)
rol_administrador.permission.append(puntos_encuentro_update)

rol_administrador.permission.append(usuario_new)
rol_administrador.permission.append(usuario_update)
rol_administrador.permission.append(usuario_destroy)

db.session.commit()



# Defino el rol operador
rol_operador = Role("operador")

#Relacion del rol operador con sus permisos
rol_operador.permission.append(usuario_index)
rol_operador.permission.append(configuracion_index)
rol_operador.permission.append(punto_encuentro_index)
rol_operador.permission.append(puntos_encuentro_new)
rol_operador.permission.append(puntos_encuentro_update)
db.session.commit()


usuario_admin = User('cosme', 'Fulanito', 'admin', 'admin', '123123')
usuario_admin.role.append(rol_administrador)
db.session.commit()


#Creo usuario de prueba
usuario1 = User('Juan', 'Rodriguez','juancito@gmail.com', 'user1' , '21883')
usuario2 = User('Pedro', 'Rodriguez','ElRodri@unMail.com', 'rodri12' , 'libro23')
usuario3 = User('Pedro Luis', 'Juanpe','auris@unMail.com', 'ElJuanpe' , 'tomaco')
usuario4 = User('Jose Luis', 'sabili','sabilis@unMail.com', 'sabi23' , 'contra12')
usuario5 = User('Ignacio', 'linbilis','linbilis@unMail.com', 'limbis56' , 'tomaAAAc54')
usuario6 = User('Marcelo', 'umbrale','umb@unMail.com', 'usuario6' , 'Jose12')
usuario7 = User('Pedro', 'peresoso','peres@unMail.com', 'unPeresoso' , '454856458')

#Agrego los usuarios a la base
db.session.add(usuario7)
db.session.add(usuario6)
db.session.add(usuario5)
db.session.add(usuario4)
db.session.add(usuario3)
db.session.add(usuario2)
db.session.add(usuario1)
db.session.commit()


#Creo los puntos de encuentro de prueba
puntos_encuentro1 = Point('punto2','46 entre 26 y 27', '2546 545', '2213645852','point1@unEmail.com', 'Publicado')
puntos_encuentro2 = Point('punto13','46 entre 55 y 56', '122 545', '2156485745','point1@unEmail.com', 'Despublicado')
puntos_encuentro3 = Point('punto14','524 entre 12 y 13', '32 545', '4564579656','point2@unEmail.com', 'Publicado')
puntos_encuentro4 = Point('punto15','centenario entre 26 y 27', '23 54565', '656686','point4@unEmail.com', 'Publicado')
puntos_encuentro5 = Point('punto133','belgrano entre 26 y 27', '65 545', '2213654215','point5@unEmail.com', 'Publicado')
puntos_encuentro6 = Point('punto3','66 entre 26 y 27', '253246 65', '5454455454','poin61@unEmail.com', 'Despublicado')
puntos_encuentro7 = Point('punto4','55 entre 11 y 12', '158 545', '5454546525','point7@unEmail.com', 'Publicado')
puntos_encuentro8 = Point('punto5','14 esquina 22', '2546 65', '4546838547','point10@unEmail.com', 'Despublicado')
puntos_encuentro9 = Point('punto6','100 entre 10 y 11', '2325 32', '54668975678','point11@unEmail.com', 'Publicado')
puntos_encuentro10 = Point('punto7','calle falsa 123', '256546 87', '5648684883','point21@unEmail.com', 'Despublicado')
puntos_encuentro11 = Point('punto8','Belgrano 1800', '568 1', '456469838','point13@unEmail.com', 'Publicado')
puntos_encuentro12 = Point('punto9','55 entre 12 y 13', '34 65', '4457866546','point13@unEmail.com', 'Despublicado')
puntos_encuentro13 = Point('punto10','44 esquina 10', '875 5415', '569+4768','point12@unEmail.com', 'Publicado')

#Agrego los puntos de encuentro a la base de datos
db.session.add(puntos_encuentro1)
db.session.add(puntos_encuentro2)
db.session.add(puntos_encuentro3)
db.session.add(puntos_encuentro4)
db.session.add(puntos_encuentro5)
db.session.add(puntos_encuentro6)
db.session.add(puntos_encuentro7)
db.session.add(puntos_encuentro8)
db.session.add(puntos_encuentro9)
db.session.add(puntos_encuentro10)
db.session.add(puntos_encuentro11)
db.session.add(puntos_encuentro12)
db.session.add(puntos_encuentro13)
db.session.commit()
