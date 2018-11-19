from app import create_app
from flask_script import Manager, Server
from app.models import User,db,Role

app = create_app('development')
manager = Manager(app)
# migrate = Migrate(app,db)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )
    
if __name__ == '__main__':
    manager.run()