# -*- coding: utf-8 -*-
# No.3

def main():
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    str = str.replace(',', '')
    str = str.replace('.', '')
    str = str.split()

    print map(lambda n: len(n), str)

main()
