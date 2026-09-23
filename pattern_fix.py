"""
Fixed pattern — secure + readable
n=5 decreasing stars with increasing indent.
Fixes: input validation, DoS cap, correct spacing (no double end=' '), O(n) string build.
"""
def print_pattern(n: int = 5) -> None:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if not 1 <= n <= 50:
        raise ValueError("n must be 1..50 (cap to prevent DoS / terminal flood)")
    # control never gets lost: explicit n, validated, single loop
    for i in range(n):
        indent = "  " * (i + 1)          # increasing space (2 chars per indent, matches original intent)
        stars = "* " * (n - i)           # decreasing stars
        print(f"{indent}{stars.rstrip()}")

if __name__ == "__main__":
    import sys
    try:
        val = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    except ValueError:
        print("usage: python pattern_fix.py [n]", file=sys.stderr)
        sys.exit(2)
    print_pattern(val)
