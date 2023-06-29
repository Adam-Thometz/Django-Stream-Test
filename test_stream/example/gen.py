def test_gen():
    yield 'Hello '
    yield 'World '

    n = 0
    while n < 1000000:
        yield f'{n} '
        n += 1