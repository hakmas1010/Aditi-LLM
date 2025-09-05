# Placeholder – real implementation private.
from src.core.model import AditiModel
from src.conversation.dialogue import converse
import random
import time
import sys


def main():
    print("[Aditi-LLM] Booting... (placeholder)")
    model = AditiModel()
    print("[Aditi-LLM] Ready. Type 'exit' to quit.\n")

    prompts = [
        "mm-hmm...",
        "got it",
        "I hear you",
        "okay, so",
        "alright",
    ]

    # Non-interactive or demo mode fallback
    if (len(sys.argv) > 1 and sys.argv[1] == "--demo") or not sys.stdin.isatty():
        demo_inputs = [
            "hey aditi, how's your day?",
            "give me one tiny tip to focus better",
            "ok, got it, one more",
        ]
        for user in demo_inputs:
            time.sleep(0.2)
            pre = random.choice(prompts)
            stub = converse(user)
            gen = model.generate(user)
            reply = f"{pre} {gen if gen else stub}"
            print(f"you> {user}")
            print(f"aditi> {reply}")
        print("[demo] done.")
        return

    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[aditi] bye for now. (placeholder)")
            break

        if user.lower() in {"exit", "quit"}:
            print("[aditi] take care. (placeholder)")
            break

        # Simulate a natural pause
        time.sleep(min(0.8, 0.2 + len(user) * 0.01))

        # Placeholder response shaping
        pre = random.choice(prompts)
        stub = converse(user)
        gen = model.generate(user)
        reply = f"{pre} {gen if gen else stub}"
        print(f"aditi> {reply}")


if __name__ == "__main__":
    main()
