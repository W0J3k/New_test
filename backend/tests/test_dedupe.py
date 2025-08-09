from app.utils.simhash import simhash


def test_simhash_near_duplicates() -> None:
    h1 = simhash("hello world")
    h2 = simhash("hello world!")
    assert h1 == h2
