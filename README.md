Chat with Meta’s Llama 3 8B

Use this Studio to deploy a private version of Meta’s Llama 3 8B LLM. Llama 3 is a state-of-the-art language model that is great for coding or general Q&A.

https://www.loom.com/share/0b6771433c324a7f8ea5dbf372a04e5d?sid=95949ddc-0b47-4c7b-812d-4f8e520771f4Chat with Meta's Llama 3 8B

Try it yourself

You can run the Llama 3 7B LLM on your own private Lightning Studio. Chat with it at interactive speeds on cost friendly GPUs (T4, L4, A10G) using your 15 free credits.

No need to depend on external APIs that may go down without notice.

Click "Open in Studio" to start this Studio with Llama 3 running.

What is Llama 3?

Large language models (LLM) are great coding and writing companions. The ability to run them in a Studio without relying on third-party APIs opens up a lot of possibilities, from personal use during development, to building LLM-based systems quickly.

Llama 3 is a very capable family of large language models (LLM) initially released by Meta in April 2024. This studio contains the smallest 8 billion parameter variant.

The model family:

includes 8B (this studio) and 70B variantsis trained on a dataset of 15B tokens, spanning over 30 languagesshows very strong performance on text generation, coding, and reasoning tasks

Take a look at the announcement for more details.

License

Make sure you read, accept and understand the Meta Llama 3 License before proceeding.

Steps to run Llama 3

Follow these steps to run a private version of Llama 3.

Deploy the model API

Start the Studio by clicking "Open in Studio." Once the Studio starts, it will automatically start a server running an optimized version of Llama 3 in the background (courtesy of ollama.ai).

At that point you can start the run.ipynb notebook to chat with the model:

Chat with Meta's Llama 8B in run.ipynb Select an Image

The chatbot function returns and accepts a context variable that contains the context of the conversation. This way the replies with take the previous conversation steps into account.

You can modify the chatbot function to capture the text response in a variable and extract information from it, the above is just a starting point.

Deploy the built-in chat app

The Studio comes prepackaged with a built-in web app (in Streamlit). Use this to chat with the model.

The app will preserve the context of the conversation, will format code snippets nicely and allow you to copy them with a button click, so you can use the app as a code companion.

The main.py file contains the chat app, implemented as a Streamlit application. It's about 50 lines of Python and it's easy follow and hack on. You can run it in a studio through the Streamlit plugin.

Click on the plugin:

select the Streamlit icon Select an Image

Then create a new app by clicking on the "New App" button on the top right (or clicking on "select a Studio file"):

Create a new Streamlit app Select an Image

Now select the main.py, which contains the Streamlit application, and click on "Run":

Run the Streamlit app Select an Image

And off you go! You can start interacting with Llama 3, notice how nicely code and mathematical formulas are displayed. And by the way, you can copy paste the code directly in your studio by clicking on the copy button that appears in each code block.

Using the built-in chat app Select an Image

Should you need to reset the context of the conversation, just click on the "Reset ↺".

You can also open the app in a separate window by clicking on "Open", so you can go back to your code. Or share the app with a friend by copying the "Public link" (don't post it on social though :-) ).

Compute requirements

This studio will start on a single L4 by default. Llama 3 8B will run fast at interactive speeds on the L4.

If you need to run on something cheaper to save on your credits you can switch to a single T4 machine. The model will run at a fewer tokens per second on a T4, but will still be usable.

At this time you won't be able to run Llama 3 or other LLMs on CPU Studios.

Performance and cost

Here's a breakdown on how Llama 3 performs on L4 and T4 studios:

Add row aboveAdd row belowDelete rowAdd column to leftAdd column to rightDelete columnMachineCost per hourSpeed (tok/s)L41.0847.06T40.6841.65

Conclusion

In this guide you deployed a private instance of the Llama 3 8B. Feel free to connect this model's API to any of your products.
