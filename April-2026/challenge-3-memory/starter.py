import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent

MODEL = "us.amazon.nova-pro-v1:0"

from strands_tools import mem0_memory

sys= """You are a helpful assistant called 'Pixie' , answer the user in short answer but simple and accurate"""
agent = Agent(model = MODEL, tools =[mem0_memory],system_prompt=sys)  # Replace this line


print("🧠 Memory Agent Ready!")
print("Try: 'Remember that my name is [your name] and I love [food]'")
print("Then: 'What's my name and what food do I like?'")
print("Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! 👋")
            break
        
        # TODO: Send user_input to the agent and print the response
        # Hint: response = agent(user_input)
        print("Agent: ")
        response = agent(user_input)

    except KeyboardInterrupt:
        print("\nBye! 👋")
        break

print("\n✅ Challenge 3 complete!")
