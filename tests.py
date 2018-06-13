from poetry_setup import PoetrySetup


def test_requirements():
    ps = PoetrySetup('example')
    rs = ps.get_requirements()
    assert 'toml>=0.9,<0.10\n' in rs