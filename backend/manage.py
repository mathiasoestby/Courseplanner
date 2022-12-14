
def deploy():
  """ run deployment tasks """
  from app import create_app, db
  from flask_migrate import upgrade, migrate, init, stamp
  from models import Articles

  app = create_app()
  app.app_context().push()


  db.create_all()

  stamp()
  migrate()
  upgrade()


deploy()
