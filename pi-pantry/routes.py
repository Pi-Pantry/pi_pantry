def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.add_route('manage_item', '/manage_item')
    config.add_route('pantry', '/pantry')
    config.add_route('shopping_list', '/shopping')
    config.add_route('details', '/details')
    config.add_route('logout', '/logout')
