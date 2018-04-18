def includeme(config):
<<<<<<< HEAD
    config.add_static_view('static', 'static', cache_max_age=10)
=======
    config.add_static_view('static', 'static', cache_max_age=0)
>>>>>>> b52fc3b2a1a70be2673f3a37b33c7f0e3486f969
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.add_route('pantry', '/pantry')
    config.add_route('detail', '/detail/{upc}')
    config.add_route('lookup_item', '/lookup_item')
    config.add_route('logout', '/logout')
