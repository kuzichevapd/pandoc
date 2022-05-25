from panflute import *
import sys

headers = {}


def action(elem, doc):
    if type(elem) == Header:
        if stringify(elem) in headers.keys() and headers.get(stringify(elem)) == elem.level:
            sys.stderr.write("duplicate headers: level - " + str(elem.level) + ", text - " + stringify(elem))
        else:
            headers[stringify(elem)] = elem.level
    if type(elem) == Header:
        if elem.level <= 3:
            title = [Str(stringify(elem).upper())]
            return Header(*title, level=elem.level)

    if type(elem) == Str:
        if str(elem.text).upper() == "BOLD":
            title = [Str(elem.text)]
            return Strong(*title)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
