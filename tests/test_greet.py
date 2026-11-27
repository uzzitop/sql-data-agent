from sql_data_agent.greet import greet

def test_greet():
    assert greet("Uzzi") == "Hello, Uzzi!"