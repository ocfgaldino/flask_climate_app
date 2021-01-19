

def test_app_is_created(app): # Dependency Injection
    assert app.name == 'climate.app'
    
    
def test_config_is_loaded(config):
    assert config["DEBUG"] is False
    
def test_request_returns_404(client):
    assert client.get("/url_not_exists").status_code == 404
    
