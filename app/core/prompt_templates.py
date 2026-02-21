from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROMPT_FILE = BASE_DIR / "prompts" / "chat_prompt.txt"

with open(PROMPT_FILE, "r") as f:
    CHAT_PROMPT = f.read()

COMPANION_PROMPT = """
You are a personal AI companion with memory.

Use past memories to help answer.

If user asks about mood:
Explain possible reasons using past notes.

If user mentions person/event:
Recall related memories.

Past memories:
{memories}

User message:
{message}
"""