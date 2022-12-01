from XianDai.Vector import Vector


if __name__ == '__main__':
    vec1 =Vector([1,3])
    vec2 = Vector([4, 3])
    print(vec1.normalize().norm())
    zero=Vector.zero(2)
    print(zero.normalize())
