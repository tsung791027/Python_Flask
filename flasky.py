import os  #導入環境
from app import create_app, db  #從app導入 create_app & database((app---->__init__初始化資料夾
from app.models import User, Role  #從app內的models導入 User,Role
from flask_migrate import Migrate #導入Migrate 將database 做遷移備份用


app = create_app(os.getenv('FLASK_CONFIG') or 'default')  #建立app，從環境變數取得組態設置，如果他有定義的話，否則使用預設值
migrate = Migrate(app, db) #初始化Migrate

@app.shell_context_processor #與python shell整合shell 環境處理常式
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command() #單元測試啟動命令
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)