class Cliente:
    def __init__(
        self,
        id,
        tipo_documento,
        numero_documento,
        nombre,
        empresa,
        telefono,
        correo
    ):
        self.id = id
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.nombre = nombre
        self.empresa = empresa
        self.telefono = telefono
        self.correo = correo