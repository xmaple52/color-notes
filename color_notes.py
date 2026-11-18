import argparse


def rgb(value):
    value = value.removeprefix('#')
    if len(value) == 3:
        value = ''.join(c * 2 for c in value)
    if len(value) != 6 or any(c not in '0123456789abcdefABCDEF' for c in value):
        raise ValueError('Expected a 3- or 6-digit HEX color')
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


def luminance(color):
    def linear(n):
        s = n / 255
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = map(linear, color)
    return 0.2126*r + 0.7152*g + 0.0722*b


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def main():
    parser = argparse.ArgumentParser(description='HEX color inspection and text contrast.')
    parser.add_argument('foreground', help='HEX color; quote colors starting with #')
    parser.add_argument('--background', default='ffffff')
    args = parser.parse_args()
    try:
        fore, back = rgb(args.foreground), rgb(args.background)
    except ValueError as error:
        parser.error(str(error))
    ratio = contrast(fore, back)
    print(f'RGB: {fore[0]}, {fore[1]}, {fore[2]}')
    print(f'Contrast: {ratio:.2f}:1')
    for label, minimum in [('AA normal text', 4.5), ('AA large text', 3), ('AAA normal text', 7)]:
        print(f'{label}: {"PASS" if ratio >= minimum else "FAIL"}')


if __name__ == '__main__':
    main()
