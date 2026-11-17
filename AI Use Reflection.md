How did you approach learning your topic? What were your initial questions, and how did your exploration develop?

I have trust issues with AI models, so my immediate action was to make sure that claude cites all of its information. After that I started at a base level of exploring how C is used in python, and the first
thing it brought up was ctypes, so I explored the documentation for that and began to write my own basic implementation. With all of my code, I felt that it would be better to write it myself and then consult claude if I got stuck,
because that would result in a better personal understanding than just telling claude to generate everything.

I also immediately asked for a list of python libraries that implement C, and when providing that list, it often brought up Cython as their C implementation instead of ctypes. This got me started on investigating Cython
and writing my own code to implement that for a library. I also thought about pygame, a library I used as a child studying python, and asked it if that used C, and it turned out that it was a wrapper for SDL which is coded in C.
I tried exploring SDL a little, but it was out of scope and also harder to find information on where specifically it came up in pygame.



What prompts did you use? Share two or three representative prompts from your conversation. Choose prompts that demonstrate how you explored your topic, asked follow-up questions, or worked through something confusing.

"what is the filepath based on when calling CDLL? provide an example that includes the filepath for the c program and python program that implements the c program"
This prompt provided a clearer example of CDLL in practice, including the compilation steps which required their own flags.
I didn't understand certain unique flags and terms that came up, so I asked followup questions like "what do the -shared and -fPIC tags do?", and "im receiving an os error from this implementation. it "cannot dynamically load position-independent executable"" when errors came up


How did you engage with AI? Describe how you used AI's responses to guide your learning. Did you ask clarifying questions, request examples, challenge an explanation, or test something yourself?

I mainly engaged with it as a starting point for research, and then worked off of more concrete documentation that I found from the links it provided or through a search engine.
Whenever I encountered a roadbump with understanding the documentation or encountered a specific error, I went back to AI to see if I could get some clarification or a better example than what the documentation provided
I tested the code it gave me, but in the context of the code I was already writing (so things like filenames weren't exact but the logic was the same)



What would you do differently? Reflect briefly on what worked well and what you might change about how you use AI to learn in the future.

AI worked well with bugfixing, as it's more difficult to dive through something like stackoverflow and get a solid or working answer. The more fluid response can work better with the more fluid nature of debugging a specific program.
Oftentimes outside of that case, it felt like a worse search engine, and the links it provided weren't always the top ones that were the most helpful. In the future there's probably something I could say to make it produce better results, but search engines also exist and are more consistent.
I also didn't have very many prolonged conversations outside of fixing a specific bug. There may be some more value I could get by asking more questions than are strictly necessary.
