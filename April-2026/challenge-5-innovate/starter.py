"""
Challenge 5 (Innovate): Build Your Own MCP-Powered Agent

YOUR TASK:
  Build an innovative agent from scratch that connects to any MCP server.
  The most creative and useful agent gets a special shoutout! 🏆

RULES:
  - Must use Strands Agents SDK
  - Must use at least one MCP server
  - Must use Amazon Nova Pro (or any Bedrock model)
  - Must have an interactive chat loop
  - Must be YOUR OWN idea — be creative!

EXAMPLE MCP SERVERS:
  pip install awslabs.aws-documentation-mcp-server   # AWS Docs
  uvx awslabs.cdk-mcp-server@latest                  # AWS CDK
  uvx awslabs.cost-analysis-mcp-server@latest        # AWS Pricing

BROWSE MORE: https://github.com/modelcontextprotocol/servers

RESOURCES:
  - Strands MCP docs: https://strandsagents.com/latest/user-guide/concepts/tools/mcp-tools/
  - AWS MCP servers: https://github.com/awslabs/mcp

Build something that makes us go "whoa!" 🚀
"""

# Your code here — build the entire agent from scratch!
import os
import asyncio
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

MODEL = "us.amazon.nova-pro-v1:0"

async def main():
    # Connect to the AWS Documentation MCP server
    server_params = StdioServerParameters(
        command="uvx",
        args=["awslabs.aws-documentation-mcp-server@latest"],
        env={"FASTMCP_LOG_LEVEL": "ERROR"}
    )

    async with stdio_client(server_params) as (read, write):
        async with MCPClient(read, write) as mcp_client:
            tools = await mcp_client.list_tools()

            agent = Agent(
                model=MODEL,
                tools=tools,
                system_prompt="""You are an AWS documentation expert! 📚
You have access to the official AWS documentation via MCP tools.
Help users understand AWS services, find docs, and answer technical questions.
Always cite which AWS service or doc you're referencing."""
            )

            print("📚 AWS Docs Chatbot — powered by MCP")
            print("Ask me anything about AWS! Type 'quit' to exit.\n")

            while True:
                user_input = input("You: ").strip()
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("Goodbye! 👋")
                    break
                if not user_input:
                    continue
                response = agent(user_input)
                print(f"Agent: {response}\n")

asyncio.run(main())

print("\n✅ Challenge 5 complete!")
