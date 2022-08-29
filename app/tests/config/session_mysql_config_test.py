

from re import M
from unittest.mock import MagicMock, patch


class TestConfigSetup(unittest.TestCase):
    _logger = AppLogger().create_logger(__name__)

    @patch.object(Session, 'client')
    @patch.object(pymysql, 'connect')
    def test_connect(self, mock_client, mock_connect):
        # Arranges
        mock_client.return_value = MagicMock()
        mock_client.get_secret_value.return_value = MagicMock()
        mock_connect.return_value = MagicMock()

        #Act
        retorno = ConfigSetup(self._logger).connect()

        #Asserts
        assert retorno is not False
        assert mock_connect.called
        assert mock_client.called

    @patch.object(pymysql, 'connect')
    def test_connect_exception(self, mock_connect):
        with self.assertRaises(Exception):
            mock_connect.return_value = Mock(side_effect=pymysql.MySQLError)
            ConfigSetup(self._logger).connect()