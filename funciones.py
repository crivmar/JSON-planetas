def leer_documento(d):
    import json
    with open(d) as f:
        l=json.load(f)
    return l



