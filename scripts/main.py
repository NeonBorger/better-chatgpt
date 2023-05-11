import openai
from subprocess import call
model_engine = "text-davinci-003"
api_key_path = "../../api_key.txt"
with open(api_key_path, 'r') as file:
    api_key = file.read().strip()

model_engine = "text-davinci-003"
openai.api_key = api_key
def GPT(query):
   response = openai.Completion.create(
       engine=model_engine,
       prompt=query,
       max_tokens=2048,
       temperature=0.3,
   )
   return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']
exit_words = ("q","Q","quit","QUIT","EXIT")
try:
   while True:
       print("Type q, Q, quit, QUIT or EXIT and press Enter to end the chat session")
       query = input("Prompt> ")
       if query in exit_words:
           print("ENDING CHAT")
           break
       else:
           (res, usage) = GPT(query)
           print(res)
           call(["espeak",res])
           print("="*20)
           print("You have used %s tokens on this query" % usage)
           print("="*20)
except KeyboardInterrupt:
 exitSpeech="Exiting Program."
 call(["espeak",exitSpeech])
 print("\nExited ChatGPT")
