def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        reutrn data.decode('utf-8')
    else:
        raise TypeError('Must supply str or bytes,'
                        'found: %r' % data)

