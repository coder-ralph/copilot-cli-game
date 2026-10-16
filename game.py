def choose(prompt, options):
    """Display numbered options and return the selected option's index."""
    print(f"\n{prompt}")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        answer = input("Choose an option: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer) - 1
        print(f"Please enter a number from 1 to {len(options)}.")


def play():
    print("The Last Light\n")
    print("A storm rolls over the coast, and the lighthouse has gone dark.")
    print("A ship is struggling to find its way through the fog.")

    path = choose(
        "Where will you go?",
        ["Climb the hill to the lighthouse", "Follow the beach to the old boathouse"],
    )

    if path == 0:
        action = choose(
            "At the lighthouse, you find a locked door and a narrow path to a window.",
            ["Search the keeper's desk for a key", "Climb in through the window"],
        )
        if action == 0:
            print("\nYou find the key, light the beacon, and guide the ship safely home.")
            print("ENDING: The Guiding Light")
        else:
            print("\nYou climb inside and restart the lamp just in time. The grateful crew")
            print("rescues you from the storm at dawn.")
            print("ENDING: A Narrow Escape")
        return

    action = choose(
        "The boathouse is nearly flooded. You spot a small boat and a signal flare.",
        ["Launch the boat and row toward the ship", "Fire the flare from the shore"],
    )
    if action == 0:
        print("\nYou row through the waves and lead the ship toward the safe harbor.")
        print("ENDING: The Brave Rescue")
    else:
        print("\nThe flare glows through the fog. The ship changes course and reaches")
        print("the harbor safely, while you watch from dry land.")
        print("ENDING: The Clever Signal")


if __name__ == "__main__":
    play()