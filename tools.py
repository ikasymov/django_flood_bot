def dump_telegram_object(msg):
    ret = {}
    for key, val in msg.__dict__.items():
        if isinstance(val, (int, str, dict)):
            pass
        elif val is None:
            pass
        elif isinstance(val, (tuple, list)):
            val = [dump_telegram_object(x) for x in val]
        else:
            val = dump_telegram_object(val)
        if val is not None:
            ret[key] = val
    return ret