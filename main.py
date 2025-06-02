import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import chainlit as cl
#=============================================================
#=======================  Setup  =============================
load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY= os.getenv('OPENROUTER_API_KEY')

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set")

#=======================================================================
history = []

#======================================================================

client =AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client),
    name="fzk_agent",
    instructions="your are a helpful assistant",

)

#====================================================================
@cl.on_message
async def main(message: cl.Message):
   ui_question = message.content
   history.append({"role": "user", "content": ui_question})

   jawab = Runner.run_sync(agent, history)
   history.append({"role": "assistant", "content": jawab.final_output})

   await cl.Message(content=jawab.final_output).send()



