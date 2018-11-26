import pytest
from pytest import raises
from unittest.mock import MagicMock
import os
import requests


def file_reader(path):
    if not os.path.exists(path):
        raise FileNotFoundError('wrong path')
    with open(path, 'r') as fh:
        return fh.readline()

def get_url(url):
    return requests.get(url)


def test_raise_exception_when_called_with_bad_path(monkeypatch):
    with raises(FileNotFoundError):
        file_reader('blah')


def test_throws_exception(monkeypatch):
    fh = MagicMock()
    fh.readline = MagicMock()
    fh.readline.return_value = 'test line'
    mock_open = MagicMock(return_value=True)
    monkeypatch.setattr('builtins.open', mock_open)
    mock_path = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_path)

    with raises(FileNotFoundError):
        file_reader('path')


def test_returns_correct_string(monkeypatch):

    fh = MagicMock()
    fh.readline = MagicMock()
    fh.readline.return_value = 'test line'
    # now always call to fh.readline() returns 'test line' value
    assert fh.readline() == 'test line'

    # we can mock any std/imported lib ie. os.path or requests.get this way
    mock_path = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_path)
    assert os.path.exists('blah')

    # in a simple form we would mock open with some bool value and be done with it.
    # but real example uses context manager so we need to mock its response value which is a file obj in this case
    # assert open()
    mock_open = MagicMock()
    mock_open.return_value.__enter__.return_value = fh
    monkeypatch.setattr('builtins.open', mock_open)

    result = file_reader('blah')
    # mock_open.assert_called_once_with('blah', 'r')
    mock_open.assert_called_with('blah', 'r')
    assert result == 'test line'


def test_get_url(monkeypatch):
    # example how to monkeypatch return value from requests library
    mock_result = MagicMock()
    mock_result.text = 'hello'
    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr('requests.get', mock_get)
    result = get_url('test')
    mock_get.assert_called_once_with('test')
    assert result.text == 'hello'

