def init_app(app):
    app.config['SECRET_KEY'] = '123456'

    if app.debug: #toolbar just work in debugmode
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
