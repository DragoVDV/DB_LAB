from instagram.auth.controller.user_controller import user_bp
from  instagram.auth.controller.enrollment_controller import enrollment_bp
def init_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(enrollment_bp)