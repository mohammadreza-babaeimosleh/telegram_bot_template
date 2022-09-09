from types import SimpleNamespace

from src.utils.keyboard import create_keyboard

keys = SimpleNamespace(
    random_connect=":technologist: Random Connect",
    setting=":gear: Setting",
    send_message=":envelope: Send Messagee",
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.random_connect, keys.setting, keys.send_message)
)
