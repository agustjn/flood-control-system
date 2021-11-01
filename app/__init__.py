from os import path, environ
from flask import Flask, render_template, g, Blueprint,session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import config
from app import db
from app.resources import issue,user,point,configuration,auth
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers.auth import Auth
import logging
from app.helpers.routes import RoutesConfig
from app.helpers.configurations import format_background
from app.helpers.permission import PermissionDAO


#Activo los loggins en la terminal de las query generadas
logging.basicConfig()
logging.getLogger("sqlalchmy.engine").setLevel(logging.INFO)

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "NeedConfigureAn"

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/proyecto'
    # if environment=="production":
    #     Que hago
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://grupo3:YWMyMDEzYzE4OTY5@localhost:3306/grupo3'
    # else:
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/proyecto'


    Session(app)

    # Configure db
    db.init_app(app)


    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=Auth.is_authenticated)
    app.jinja_env.globals.update(format_background=format_background)

    app.jinja_env.globals.update(has_permission=PermissionDAO.has_permission)
    app.jinja_env.globals.update(has_rol = PermissionDAO.has_rol)

    # Autenticación
    app.add_url_rule("/iniciar_sesion/", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios

    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuario/delete/<user_id>", "user_delete", user.delete)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/edit/<user_id>", "user_edit", user.edit)
    app.add_url_rule("/usuarios/modification/<user_id>", "user_modification", user.modify,methods=["POST"])
    app.add_url_rule("/usuarios/desactivate_activate/<user_id>", "user_activate_desactivate", user.activate_desactivate,methods=["POST", "GET"])

    # Rutas de Puntos de encuentro
    app.add_url_rule("/puntos", "index_filtro", point.index_filtro, methods=["POST"])
    app.add_url_rule("/puntos", "point_index", point.index)
    app.add_url_rule("/puntos/delete/<point_id>", "point_delete", point.delete)
    app.add_url_rule("/puntos/nuevo", "point_create", point.create, methods=["POST"])
    app.add_url_rule("/puntos/nuevo", "point_new", point.new)
    app.add_url_rule("/puntos/edit/<point_id>", "point_edit", point.edit)
    app.add_url_rule("/puntos/modification/<point_id>", "point_modification", point.modify,methods=["POST"])



    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")


    app.add_url_rule("/configuraciones","config_index",configuration.index)
    app.add_url_rule("/configuraciones","config_update",configuration.update, methods=["POST"])

    # Instancio la clase para configurar las rutas

    RoutesConfig(app)

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
