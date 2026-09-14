class Solicitud:
    def __init__(
        self,
        id,
        codigo,
        fecha,
        descripcion,
        prioridad,
        estado,
        cliente_id,
        servicio_id,
        tecnico_id
    ):
        self.id = id
        self.codigo = codigo
        self.fecha = fecha
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.cliente_id = cliente_id
        self.servicio_id = servicio_id
        self.tecnico_id = tecnico_id