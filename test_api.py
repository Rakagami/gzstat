from gzstat import analyze_buffer
import gzip
import json


TEST_FILE = "LICENSE"


if __name__ == "__main__":
    data_buffer = open(TEST_FILE, "rb").read()
    print("Length of uncompressed data buffer   :", len(data_buffer))

    compressed_data_buffer = gzip.compress(data_buffer, mtime=0, compresslevel=9)
    print("Length of compressed data buffer     :", len(compressed_data_buffer))

    stats = analyze_buffer(compressed_data_buffer, True, True, False, False)
    print(json.dumps(stats, indent=3))
