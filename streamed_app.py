import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner,set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI
import rich
load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#=============================================
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"

)
agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free", openai_client=client),
    name="Fzk agent",
    instructions="you are a helpful assistant",
)
#===============================================
async def main():
    jawab = Runner.run_streamed(starting_agent=agent, input="write a 10 lines of eassy on cat?") # Agentic loop
    async for event in jawab.stream_events():
      
      rich.print(event)

if __name__ == "__main__":
   asyncio.run(main())



