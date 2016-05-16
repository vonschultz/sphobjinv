
def main():
    import os, zlib, re

    # Go to work dir
    os.chdir('C:\\')

    # Pull the file, binary
    with open('objects.txt', 'rb') as f:
        b = f.read()

    # Convert any DOS newlines to Unix
    s = b.decode().replace('\r\n', '\n')

    # Pattern for comment lines
    p_comments = re.compile('^#.*$', re.M)

    # Pattern for not-comment lines
    p_data = re.compile('^[^#].*$', re.M)

    # Pull all of the lines
    m_comments = p_comments.findall(s)
    m_data = p_data.findall(s)

    # Assemble the binary header comments and data
    hb = "\n".join(m_comments).encode()
    db = "\n".join(m_data).encode() + b'\n'

    # Compress the data
    dbc = zlib.compress(db)

    # Output the result
    with open('objects.inv', 'wb') as f:
        f.write(hb + b'\n' + dbc)






if __name__ ==  '__main__':
    main()
