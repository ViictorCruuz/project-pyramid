def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('victor', '/victor')
    config.add_route('outra', '/victor/outra')
