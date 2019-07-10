# prosdelamaison

<div>
.
└── project_name # top level, everything under here is in git repo
    ├── Dockerfile
    ├── apps
    │   └── app_name
    │       ├── admin.py
    │       ├── forms.py
    │       ├── models.py
    │       ├── templates # app specific templates
    │       ├── urls.py
    │       └── views.py
    ├── assets
    ├── requirements # dependencies for the project: prod, test etc
    ├── docs # documentation, if any
    ├── project_name # inner project directory
    |   ├── urls.py
    |   ├── views.py
    |   └── wsgi.py    
    ├── scripts # CI scripts, manage.py, etc
    ├── settings # settings for the project: prod, test etc.
    |   ├── base.py
    |   ├── prod.py
    |   └── test.py
    ├── setup.py
    ├── templates # top level templates
    └── tests # tests specific to every app
        ├── app_name
        └── app_name_1
</div>
