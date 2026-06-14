import importlib.util
import os
import sys

ROOT_DIR = os.path.dirname(__file__)
INNER_APP_DIR = os.path.join(ROOT_DIR, "LEGACY_DIGITAL_FOREVER_PROTOTYP")
if INNER_APP_DIR not in sys.path:
    sys.path.insert(0, INNER_APP_DIR)

INNER_APP_PATH = os.path.join(INNER_APP_DIR, "app.py")

try:
    spec = importlib.util.spec_from_file_location("legacy_app", INNER_APP_PATH)
    legacy_app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(legacy_app)
    app = legacy_app.app
except Exception as e:
    raise RuntimeError(f"Failed to import legacy app from {INNER_APP_PATH}") from e

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
