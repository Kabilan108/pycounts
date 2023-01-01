from pycounts_k108 import count_words, plot_words
from collections import Counter
from matplotlib import container

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                        'the': 1, 'same': 1, 'thing': 1, 
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"

def test_plot_words():
    """Test plotting of word counts"""
    counts = Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                      'the': 1, 'same': 1, 'thing': 1, 
                      'over': 2, 'and': 2, 'expecting': 1,
                      'different': 1, 'results': 1})
    fig = plot_words(counts)
    assert isinstance(fig, container.BarContainer), \
           "Wrong plot type"
    assert (len(fig.datavalues) == 10,  # type: ignore
           "Incorrect number of bars plotted")
