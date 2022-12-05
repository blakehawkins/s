import sys

def main() -> None:
  in_ = sys.stdin.read()
  lines = in_.split('(')[1:]
  count = 0
  for ln, line in enumerate(lines):
    print(f"{' ' * (ln - count)}({line}")
    count += len([x for x in line if x == ')'])

if __name__ == '__main__':
    main()
