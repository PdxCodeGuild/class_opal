# Lab 14: Test ARI

from ARI import ARI

def test_ARI():
    contents = "string of words here for testing."
    assert type(ARI(contents)) is str
    # How would I check a variable like num_of_characters?
    # Does soemthing else need to be imported?
    # Will probably have to refactor code to return the
    #variables I need?