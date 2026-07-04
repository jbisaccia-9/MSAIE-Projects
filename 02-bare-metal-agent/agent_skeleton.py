"""
Bare-metal agent skeleton.

Scaffolding is done for you: tool definitions, tool implementations, config.
The engine — the agent loop — is yours to write. It's ~30 lines. Those 30
lines are the entire concept of "an AI agent."

Usage:
    python agent_skeleton.py "What is (17 * 43) + 2026?"
    python agent_skeleton.py "Read notes.txt and summarize it"
"""

import json
import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

MODEL = "claude-sonnet-5"   # good balance of capability/cost for learning
MAX_TURNS = 10              # circuit breaker — a confused model must not loop forever

# --------------------------------------------------------------- tools --
# A "tool" is two things: a JSON-schema DESCRIPTION the model reads, and a
# Python function YOU run when the model asks for it. The model never runs
# anything — it only asks. You are the hands. Internalize that; it's also
# why agent security (module 07) is entirely your problem.

TOOLS = [
    {
        "name": "calculator",
        "description": "Evaluate a basic arithmetic expression, e.g. '(17 * 43) + 2026'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "Arithmetic expression"}
            },
            "required": ["expression"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a text file from the current directory and return its contents.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string", "description": "Name of the file to read"}
            },
            "required": ["filename"],
        },
    },
]


def run_calculator(expression):
    # eval() is dangerous in general; the allowlist makes it tolerable for a toy.
    if not set(expression) <= set("0123456789+-*/(). "):
        return "Error: only basic arithmetic is allowed."
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def run_read_file(filename):
    if "/" in filename or filename.startswith("."):
        return "Error: plain filenames in the current directory only."
    try:
        with open(filename) as f:
            return f.read()[:5000]
    except FileNotFoundError:
        return f"Error: {filename} not found."


def execute_tool(name, tool_input):
    """Dispatch a tool call from the model to the matching Python function."""
    if name == "calculator":
        return run_calculator(tool_input["expression"])
    if name == "read_file":
        return run_read_file(tool_input["filename"])
    return f"Error: unknown tool '{name}'"


# ---------------------------------------------------------- the engine --
def run_agent(user_message):
    """The agent loop. YOU write this. The shape:

    1. Start a messages list containing the user's message.
    2. Call client.messages.create(model=..., max_tokens=...,
                                   tools=TOOLS, messages=messages)
    3. Look at response.stop_reason:
         - "tool_use": the model wants tools.
             a. Append the assistant's ENTIRE response content to messages:
                  {"role": "assistant", "content": response.content}
             b. For every block in response.content where block.type == "tool_use":
                  run execute_tool(block.name, block.input)
             c. Append ONE user message carrying the results:
                  {"role": "user", "content": [
                      {"type": "tool_result",
                       "tool_use_id": block.id,
                       "content": <what execute_tool returned>}, ...]}
                (Why role="user"? The API models tool results as things the
                 *world* says back to the model. Sit with that — it explains
                 the whole conversation structure.)
             d. Loop back to step 2.
         - anything else ("end_turn"): extract the text blocks and return them.
    4. Respect MAX_TURNS. If you hit it, return what you have with a warning.

    While debugging, print every tool call and its result — watching the
    loop think is the entire educational payload of this module.
    """
    client = Anthropic()
    messages = [{"role": "user", "content": user_message}]

    # YOU: implement the loop described above.
    raise NotImplementedError("This is the part you build. ~30 lines.")


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY in .env first (copy .env.example).")
    question = sys.argv[1] if len(sys.argv) > 1 else "What is (17 * 43) + 2026?"
    print(f"USER: {question}\n")
    print(f"AGENT: {run_agent(question)}")
