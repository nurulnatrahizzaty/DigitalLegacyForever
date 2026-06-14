import base64
import sys
import zlib

if len(sys.argv) < 2:
    print("Usage: python encode_mermaid.py <file.mmd>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    data = f.read()

# compress with zlib and base64 urlsafe encode
compressed = zlib.compress(data.encode("utf-8"))
encoded = base64.urlsafe_b64encode(compressed).decode("ascii").rstrip("=")
print(encoded)
