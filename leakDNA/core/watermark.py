def embed_marker(file_path, marker):
    try:
        with open(file_path, "a") as f:
            f.write(f"\n<!--LEAKDNA:{marker}-->")
        return True
    except:
        return False


def extract_marker(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        if "<!--LEAKDNA:" in content:
            start = content.find("<!--LEAKDNA:") + len("<!--LEAKDNA:")
            end = content.find("-->", start)
            return content[start:end]

        return None
    except:
        return None