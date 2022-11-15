# Lab 14: Test ARI

from ARI import ARI

def test_ARI():
    contents = "string of words here for testing."
    assert type(ARI(contents)) is str
    ...