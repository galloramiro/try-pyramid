def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_wiki', '/')
    config.add_route('view_page', '/{pagename}')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

