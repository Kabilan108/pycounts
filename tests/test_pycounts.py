from pycounts_k108 import count_words, plot_words
from pycounts_k108.datasets import get_flatland
from collections import Counter
from matplotlib import container
import pytest


# Add a fixture to get the einstein counts
# this will help avoid repitition in the tests
@pytest.fixture
def einstein_counts():
    return Counter(
        {
            "insanity": 1,
            "is": 1,
            "doing": 1,
            "the": 1,
            "same": 1,
            "thing": 1,
            "over": 2,
            "and": 2,
            "expecting": 1,
            "different": 1,
            "results": 1,
        }
    )


def test_count_words(einstein_counts):
    """Test word counting from a file."""
    expected = einstein_counts
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"


def test_plot_words(einstein_counts):
    """Test plotting of word counts"""
    fig = plot_words(einstein_counts)
    assert isinstance(fig, container.BarContainer), "Wrong plot type"
    assert (
        len(fig.datavalues) == 10,  # type: ignore
        "Incorrect number of bars plotted",
    )


# Use a parametrized test to check different types of inputs
@pytest.mark.parametrize("obj", [3.141, "test.txt", ["list", "of", "words"]])
def test_plot_words_type(obj):
    """Check TypeError raised when Counter is not used"""
    with pytest.raises(TypeError):
        plot_words(obj)


def test_integration():
    """Test count_words() and plot_words() workflow"""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, container.BarContainer), "Wrong plot type"
    assert (
        len(fig.datavalues) == 10,  # type: ignore
        "Incorrect number of bars plotted",
    )
    assert max(fig.datavalues) == 2, "Incorrect max count"  # type: ignore


def test_regression():
    """Regression test for Flatland

    This will check that our code produces consistent results as opposed to
    checking for correctness.
    """
    top_word = count_words(get_flatland()).most_common(1)
    assert top_word[0][0] == "the", "Most common word is not 'the'"
    assert top_word[0][1] == 2263, "'the' count has changed"
