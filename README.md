# A flask restful template

* [About The Project](#about-the-project)
* [Inspiration](#inspiration)
* [Contact](#contact)
* [Built with](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
    * [Add route](#add-route)
    * [Add model](#add-model)
    * [Apply model changes](#apply-model-changes)
* [Collaborative development](#collaborative-development)
* [License](#license)

## About The Project

This is a flask restful project structure template with a **Functional Based Structure**. It can be used to quickly
create a flask appliction with database migration and multi-environment configuration capabilities.

## Inspiration

This project mainly refers to **Lepture**'s artile: [Structure of a Flask Project]()

- Lepture: member of pallets team, core developer of Flask

## Contact

I am poor in English, so if there is any confusion about the doc, please contact me via [598959402@qq.com]().

## Built with

- [Flask-Migrate](): used for database initialization, migration, upgrade
- [Flasl-SQLAlchemy](): orm support

## Getting Started

1. Clone the repo
    ```shell
    git clone https://github.com/OnePetrichor/flask-restful-template.git
    ```
2. Install requirements
    ```shell
    pip install -r requirements.txt
    ```
3. Modify database connection information in `database.py`
   ```python
   # For development environment database
   class DevDatabase(object):
      
   ...
   
   # For production environment database
   class ProdDatabase(object):
   ```
   > **Tips**: if you want a test environment or more other environment configuration, you can add a `class xxxDatabase` similarly and then modify the `settings.py` and `manage.py` that will be mentioned later.

4. Modify information in `settings.py`
   > Here we use `inheritance` to get the corresponding database connection information.
   ```python
   # For development environment settings
   class DevSettings(DevDatabase):

   ...
   
   # For production environment settings
   class ProdSettings(ProdDatabase):
   ```
   ```python
   # e.g. change SERVER_NAME to inform the application what host and port it is bound to.
   SERVER_NAME = '127.0.0.1:8000'
   ```
   *For more configuration items, please refer to
   the [Flask Builtin Configuration Values Documentation](https://flask.palletsprojects.com/en/2.0.x/config/#builtin-configuration-values)*

5. Init database and migrations (Example of a development environment). For the production environment, directly set the
   option value to `prod`.
   ```shell
   python manage.py db --operate init --env dev
   # or
   python manage.py db -o init -e dev
   ```
   *For more `db operate` tips, you can just run **python manage.py db --help***
   > **Warning:** The initialization operation only needs to be performed once the first time you run the application, **never run this command when running the app in the future.**

6. Start the application (example of a development environment):
   ```shell
   python manage.py runserver --env dev
   # or
   python manage.py runserver -e dev
   ```
   *For more `runserver` tips, you can just run **python manage.py runserver --help***

## Usage

### Add route

Take adding routes `/user/` and `/user/bar` as an example.

1. Add `user.py` in directory `/app/routes`
   ```python
   from flask import Blueprint
   
   user_bp = Blueprint('user', __name__, url_prefix='/user')
   
   
   @user_bp.route('/', methods=['GET', 'POST'])
   def index():
       return 'what you want to return'
   
   
   @user_bp.route('/bar', methods=['GET', 'POST'])
   def bar():
       return 'what you want to return'
   ```

2. Register user blueprint in `/app/routes/__init__.py`
   ```python
   def init_app(app):
       # import blueprint to register
       from .user import user_bp
       app.register_blueprint(user_bp)
   ```

3. Now, you can get the corresponding content by visiting `/user/`, `/user/bar`

### Add model

Take adding model `User` as an example.

1. Add `user.py` in directory `/app/models`
   > Here, `User` is inherited from `Base` to get some common fields, such as `create_time`, `update_time`, etc.

   ```python
   from .base import Base, db
   
   class User(Base):
      __tablename__ = 'user'
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      username = db.Column(db.String(64), unique=True, nullable=False)
      password = db.Column(db.String(256), nullable=False)
      __mapper_args__ = {
          'concrete': True
      }
   ```
   > If you don't want to inherit form `Base`, you can do it like the following. However, **please don't forget import db from `.base` and inherit from `db.Model`**
   ```python
   from .base import db
   
   class User(db.Model):
      __tablename__ = 'user'
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      username = db.Column(db.String(64), unique=True, nullable=False)
      password = db.Column(db.String(256), nullable=False)
   ```

2. Import `User` model in `/app/models/__init__.py`
   ```python
   def init_app(app):
      db.init_app(app)
      from .user import User
   ```

3. Apply model changes to the database
   ```shell
   python manage.py db --operate migrate --env dev
   # or
   python manage.py db -o migrate -e dev
   ```

4. Now, check your database, if all goes well, you will see a `user` table with `id`, `username`, `password` fields

### Apply model changes

When you modify the data model and want to apply it to the database, you can directly execute the following command:

   ```shell
   python manage.py db --operate migrate --env dev
   # or
   python manage.py db -o migrate -e dev
   ```

> **Warning:** Please never set `--env` to `prod` in a development environment, or set `--env` to `dev` in a production environment. This will mess up migrations.

### Collaborative development

1. The `/migraions` folder is very import, don't forget submit when submitting the code. In fact, we set the directory
   to be `/migrations` for the development environment and `/prod_migrations` for the production environment. You can
   find it in `manage.py`.
2. Once the `model` is updated, don't forget to execute the database migration command.
3. Do not mistake the environment option `--env` when executing the migrate command.

### License

Distributed under the MIT License. See `LICENSE` for more information.