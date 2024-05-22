def render_startup_list(startup):
    return [
        {
            "id": startup.id,
            "title": startup.title,
            "descripcion": startup.descripcion,
            "status": startup.status,
            "created_at": startup.created_at,
            "assigned_to": startup.assigned_to,
        }
        for startup in startup
    ]


def render_startup_detail(startup):
    return {
        "id": startup.id,
        "title": startup.title,
        "descripcion": startup.descripcion,
        "status": startup.status,
        "created_at": startup.created_at,
        "assigned_to": startup.assigned_to,    }