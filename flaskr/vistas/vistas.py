from flask import request
from ..modelos import db, Cancion, CancionSchema, Usuario, UsuarioSchema, Album, AlbumSchema, Album
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

cancion_schema = CancionSchema()
usuario_schema = UsuarioSchema()
album_schema = AlbumSchema()


class VistaCanciones(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]

class VistaCanciones2(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    

class VistaCanciones3(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones4(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones5(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones6(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones7(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones8(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones9(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones10(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    
    class VistaCanciones11(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones12(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones13(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones14(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
    class VistaCanciones15(Resource):
    #Se modifica el servicio de post de canciones para que se asocien a los usuarios
    @jwt_required()
    def post(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        usuario.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
    #Se modifica el servicio de get de canciones para que traiga las canciones del usuario en sesion
    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        return [cancion_schema.dump(al) for al in usuario.canciones]
    
class VistaCancion(Resource):

    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get("titulo",cancion.titulo)
        cancion.minutos = request.json.get("minutos",cancion.minutos)
        cancion.segundos = request.json.get("segundos",cancion.segundos)
        cancion.interprete = request.json.get("interprete",cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return '',204

class VistaAlbumesCanciones(Resource):
    def get(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        return [album_schema.dump(al) for al in cancion.albumes]

class VistaValidarUsuarios(Resource):
    
    def post(self):
        userId = request.json["usuario"]
        usuarios = request.json["correos"].split(',')
        compartir = []
        errores = []
        for user in usuarios:
            usuario = Usuario.query.filter(Usuario.nombre == user).first()
            if usuario is None:
                errores.append(user)
            else:
                if userId != usuario.id:
                    compartir.append(usuario.id)
        return {"errores":errores,"compartir":compartir}

class VistaSignIn(Resource):
    
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"], contrasena=request.json["contrasena"])
        db.session.add(nuevo_usuario)
        db.session.commit()
        token_de_acceso = create_access_token(identity = nuevo_usuario.id)
        return {"mensaje":"usuario creado exitosamente", "token":token_de_acceso}


    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '',204

class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre == request.json["nombre"], Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity = usuario.id)
            return {"mensaje":"Inicio de sesión exitoso", "token": token_de_acceso}

class VistaAlbumsUsuario(Resource):
    @jwt_required()
    def post(self, id_usuario):
        nuevo_album = Album(titulo=request.json["titulo"], anio=request.json["anio"], descripcion=request.json["descripcion"], medio=request.json["medio"])
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.albumes.append(nuevo_album)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return 'El usuario ya tiene un album con dicho nombre',409

        return album_schema.dump(nuevo_album)

    @jwt_required()
    def get(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        albumes_user = set(usuario.albumes)
        print(albumes_user)
        albumes_shared = set(usuario.albumesCompartidos)
        print(albumes_shared)
        only_shared = albumes_shared - albumes_user
        print(only_shared)
        result = usuario.albumes + list(only_shared)
        print(result[0].usuario)
        return [album_schema.dump(al) for al in result]

class VistaCancionesAlbum(Resource):

    def post(self, id_album):
        album = Album.query.get_or_404(id_album)
        
        if "id_cancion" in request.json.keys():
            
            nueva_cancion = Cancion.query.get(request.json["id_cancion"])
            if nueva_cancion is not None:
                album.canciones.append(nueva_cancion)
                db.session.commit()
            else:
                return 'Canción errónea',404
        else: 
            nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
            album.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
       
    def get(self, id_album):
        album = Album.query.get_or_404(id_album)
        return [cancion_schema.dump(ca) for ca in album.canciones]

class VistaAlbum(Resource):

    def get(self, id_album):
        return album_schema.dump(Album.query.get_or_404(id_album))

    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get("titulo",album.titulo)
        album.anio = request.json.get("anio", album.anio)
        album.descripcion = request.json.get("descripcion", album.descripcion)
        album.medio = request.json.get("medio", album.medio)
        db.session.commit()
        return album_schema.dump(album)

    def delete(self, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return '',204

class VistaCompartirAlbum(Resource):

    def post(self, id_album):
        idUsuario = request.json["idUsuario"]
        nombresUsuario = request.json["nombresUsuario"].split(',')
        errores = []        
        album = Album.query.get_or_404(id_album)
        Usuario.query.get_or_404(idUsuario)

        for nombreUsuario in nombresUsuario:
            usuario = Usuario.query.filter(Usuario.nombre == nombreUsuario).first()

            if usuario is None:
                errores.append(nombreUsuario)
            else:
                usuario.albumesCompartidos.append(album)
        
        if len(errores) == 0:
            db.session.commit()

        return '',204

