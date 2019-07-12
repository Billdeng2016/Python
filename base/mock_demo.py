import mock


def mock_test(mock_method, request_data, url, method, reponse_data):
    mock_method = mock.Mock(return_value = reponse_data)
    res = mock_method(url, method, request_data)
    return res