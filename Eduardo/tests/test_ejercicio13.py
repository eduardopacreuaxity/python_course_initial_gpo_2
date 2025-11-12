from src.ejercicio13 import Servicio


def test_servicio(mocker):
    mock_logger = mocker.Mock()
    service = Servicio(logger = mock_logger)
    service.procesar_data()
    mock_logger.info.assert_called_once_with("Prosesando data...")