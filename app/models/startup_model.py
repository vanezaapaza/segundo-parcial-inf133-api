from database import db

class startup(db.Model):
    __tablename__ = "startup"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)

    def __init__(self, title, descripcion, status, created_at, assigned_to):
        self.title = title
        self.descripcion = descripcion
        self.status = status
        self.created_at = created_at
        self.assigned_to = assigned_to

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return startup.query.all()

    @staticmethod
    def get_by_id(id):
        return startup.query.get(id)

    def update(self, title=None, descripcion=None, status=None, created_at=None, assigned_to=None):
        if title is not None:
            self.title = title
        if descripcion is not None:
            self.descripcion = descripcion
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None:
            self.assigned_to = assigned_to
        db.session.commit() 
    def delete(self):
        db.session.delete(self)
        db.session.commit()