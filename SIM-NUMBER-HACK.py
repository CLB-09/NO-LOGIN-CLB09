import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
