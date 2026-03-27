from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass


RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
CLEAR_SCREEN = "\033[2J\033[H"


@dataclass
class SortStep:
    values: list[int]
    pass_number: int
    compare_index: int | None
    swapped: bool
    done: bool = False


def parse_numbers(raw_numbers: list[str]) -> list[int]:
    if raw_numbers:
        tokens = raw_numbers
    else:
        user_input = input("Enter integers separated by spaces: ").strip()
        if not user_input:
            raise ValueError("No numbers were provided.")
        tokens = user_input.split()

    numbers: list[int] = []
    for token in tokens:
        try:
            numbers.append(int(token))
        except ValueError as exc:
            raise ValueError(f"'{token}' is not a valid integer.") from exc

    return numbers


def scaled_bar_length(value: int, max_value: int, max_width: int = 40) -> int:
    if max_value <= 0:
        return 1
    if value <= 0:
        return 1
    return max(1, round((value / max_value) * max_width))


def color_text(text: str, color: str, use_color: bool) -> str:
    if not use_color:
        return text
    return f"{color}{text}{RESET}"


def format_bar(
    index: int,
    value: int,
    max_value: int,
    active_left: int | None,
    use_color: bool,
) -> str:
    length = scaled_bar_length(value, max_value)
    bar = "#" * length

    prefix = f"{index:>2} | "
    suffix = f" ({value})"

    if active_left is None:
        return prefix + bar + suffix

    if index == active_left:
        return prefix + color_text(bar, YELLOW, use_color) + suffix

    if index == active_left + 1:
        return prefix + color_text(bar, CYAN, use_color) + suffix

    return prefix + bar + suffix


def render_terminal(
    step: SortStep,
    original: list[int],
    use_color: bool,
) -> None:
    current = step.values
    max_value = max(current) if current else 0

    print(CLEAR_SCREEN, end="")
    print("Bubble Sort Visualization")
    print("=" * 25)

    if step.compare_index is None:
        compare_text = "done"
    else:
        compare_text = f"{step.compare_index} and {step.compare_index + 1}"

    swapped_text = "True" if step.swapped else "False"
    if step.swapped:
        swapped_text = color_text(swapped_text, GREEN, use_color)
    else:
        swapped_text = color_text(swapped_text, RED, use_color)

    print(f"Pass: {step.pass_number} | Comparing indices: {compare_text} | Swapped: {swapped_text}")
    print()

    for index, value in enumerate(current):
        print(format_bar(index, value, max_value, step.compare_index, use_color))

    print()
    print(f"Original: {original}")
    print(f"Current : {current}")

    if step.done:
        print()
        print(color_text("Sorted successfully.", GREEN, use_color))


def bubble_sort_steps(numbers: list[int]) -> list[SortStep]:
    values = numbers.copy()
    steps: list[SortStep] = []

    if len(values) <= 1:
        steps.append(SortStep(values.copy(), 1, None, False, True))
        return steps

    last_pass_number = 1

    for pass_number in range(1, len(values)):
        last_pass_number = pass_number
        swapped_in_pass = False

        for j in range(len(values) - pass_number):
            swapped = False

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
                swapped_in_pass = True

            steps.append(
                SortStep(
                    values=values.copy(),
                    pass_number=pass_number,
                    compare_index=j,
                    swapped=swapped,
                    done=False,
                )
            )

        if not swapped_in_pass:
            break

    steps.append(SortStep(values.copy(), last_pass_number, None, False, True))
    return steps


def run_visualization(numbers: list[int], delay: float, use_color: bool) -> None:
    original = numbers.copy()
    steps = bubble_sort_steps(numbers)

    for step in steps:
        render_terminal(step, original, use_color)
        if not step.done:
            time.sleep(delay)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bubble sort terminal visualization."
    )
    parser.add_argument(
        "numbers",
        nargs="*",
        help="Integers to sort. If omitted, the program will ask for input.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.35,
        help="Delay in seconds between animation frames.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI colors in the terminal output.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.delay < 0:
        print("Error: --delay must be a non-negative number.", file=sys.stderr)
        return 1

    try:
        numbers = parse_numbers(args.numbers)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    run_visualization(numbers, delay=args.delay, use_color=not args.no_color)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

