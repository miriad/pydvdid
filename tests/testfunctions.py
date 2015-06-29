"""Implements tests for the pydvdid.functions module.
"""


from __future__ import absolute_import
from mock import patch
from nose.tools import eq_, istest, ok_
from pydvdid.exceptions import DvdPathDoesNotExistException, VideoTsPathDoesNotExistException
from pydvdid.functions import _check_dvd_path_exists, _check_video_ts_path_exists


@istest
@patch("pydvdid.functions.isdir")
def _check_dvd_path_exists_does_not_raise_exception_when_path_exists(mock_isdir): # pylint: disable=locally-disabled, invalid-name
    """Test that invocation with a valid path does not throw an exception.
    """

    mock_isdir.return_value = True

    try:
        _check_dvd_path_exists("DVD_PATH")
    except Exception as exception: # pylint: disable=locally-disabled, broad-except
        template = "_check_dvd_path_exists raised an exception of type {0} unexpectedly!"
        assert_message = template.format(type(exception).__name__)
        ok_(False, assert_message)

    mock_isdir.assert_called_once_with("DVD_PATH")


@istest
@patch("pydvdid.functions.isdir")
def _check_dvd_path_exists_does_raise_exception_when_path_does_not_exist(mock_isdir): # pylint: disable=locally-disabled, invalid-name
    """Test that invocation with an invalid path throws a DvdPathDoesNotExistException exception.
    """

    mock_isdir.return_value = False

    try:
        _check_dvd_path_exists("DVD_PATH")
    except DvdPathDoesNotExistException as expected:
        eq_("Path 'DVD_PATH' does not exist.", str(expected))
    except Exception as unexpected: # pylint: disable=locally-disabled, broad-except
        ok_(False, "An unexpected {0} exception was raised.".format(type(unexpected).__name__))
    else:
        ok_(False, "An exception was expected but was not raised.")

    mock_isdir.assert_called_once_with("DVD_PATH")


@istest
@patch("pydvdid.functions.isdir")
def _check_video_ts_path_exists_does_not_raise_exception_when_path_exists(mock_isdir): # pylint: disable=locally-disabled, invalid-name
    """Test that invocation with a valid path does not throw an exception.
    """

    mock_isdir.return_value = True

    try:
        _check_video_ts_path_exists("DVD_PATH")
    except Exception as exception: # pylint: disable=locally-disabled, broad-except
        template = "_check_video_ts_path_exists raised an exception of type {0} unexpectedly!"
        assert_message = template.format(type(exception).__name__)
        ok_(False, assert_message)

    mock_isdir.assert_called_once_with("DVD_PATH/VIDEO_TS")


@istest
@patch("pydvdid.functions.isdir")
def _check_video_ts_path_exists_does_raise_exception_when_path_does_not_exist(mock_isdir): # pylint: disable=locally-disabled, invalid-name
    """Test that invocation with an invalid path throws a VideoTsPathDoesNotExistException
       exception.
    """

    mock_isdir.return_value = False

    try:
        _check_video_ts_path_exists("DVD_PATH")
    except VideoTsPathDoesNotExistException as expected:
        eq_("Path 'DVD_PATH/VIDEO_TS' does not exist.", str(expected))
    except Exception as unexpected: # pylint: disable=locally-disabled, broad-except
        ok_(False, "An unexpected {0} exception was raised.".format(type(unexpected).__name__))
    else:
        ok_(False, "An exception was expected but was not raised.")

    mock_isdir.assert_called_once_with("DVD_PATH/VIDEO_TS")
