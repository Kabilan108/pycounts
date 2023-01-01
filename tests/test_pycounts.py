from pycounts_k108 import count_words, plot_words
from collections import Counter
from matplotlib import container
import pytest

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


def test_plot_words_type():
    """Check TypeError raised when Counter is not used"""
    with pytest.raises(TypeError):
        list_object = ["Pythons", "are", "non", "venomous"]
        plot_words(list_object)


def test_integration():
    """Test count_words() and plot_words() workflow"""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, container.BarContainer), \
        "Wrong plot type"
    assert (len(fig.datavalues) == 10,  # type: ignore
        "Incorrect number of bars plotted")
    assert max(fig.datavalues) == 2, "Incorrect max count"  # type: ignore
