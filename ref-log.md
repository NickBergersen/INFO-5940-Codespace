## What I Learned from Implementing a Multi-Agent Workflow

Implementing this multi-agent travel planner revealed how task specialization significantly improves output quality. The Planner's focus on creative itinerary generation produced comprehensive plans quickly, while the Reviewer's dedicated validation with internet access caught critical errors like attraction closures and incorrect pricing. I learned that successful multi-agent systems need compatible output formats and clear handoff points—the Planner had to generate structured itineraries the Reviewer could systematically validate. Most importantly, explicitly defining what each agent should NOT do proved as crucial as defining what they should do. The orchestration showed me that agent collaboration creates emergent quality—the final validated itinerary consistently exceeded what either agent could produce alone. Through iterative testing, I discovered that providing concrete examples in prompts (like "9:00 AM - Visit Louvre Museum") was more effective than abstract instructions.

## Challenges Faced and How I Addressed Them

My biggest challenge was getting the Reviewer to consistently use the internet_search tool. Initially, passive instructions ("you may use internet_search") resulted in generic feedback without verification. I solved this by making tool usage mandatory: listing specific categories to fact-check (opening hours, prices, closures) and using directive language like "Use the internet_search tool to fact-check..." This dramatically improved validation quality.

API configuration presented another obstacle—the .env file failed repeatedly. I developed a workaround by setting environment variables directly in the terminal before launching Streamlit. This  approach allowed me to focus on the core multi-agent functionality rather than environment debugging.

What could be improved: The system lacks feedback loops—if the Reviewer identifies major issues, the Planner can't revise. A true iterative workflow would enable replanning rather than having the Reviewer fix everything.

## Creative Ideas and Design Choices

I focused on transparency and actionability. The "Delta List" concept was my most important choice—requiring an explicit change log (what changed, why, and supporting evidence) rather than burying corrections in text. This creates accountability and educational value.

I framed the Reviewer as a "validator" rather than "critic" to encourage constructive feedback. Early tests showed "error-finding" language produced overly negative outputs, while "validation" language yielded balanced assessments acknowledging what worked alongside necessary corrections. I also emphasized specific, itemized costs in the Planner instructions to facilitate easier verification.


## GenAI assistance:

I used claude to help me with the following error:

Error code: 401 - {'error': {'message': 'Authentication Error, No api key passed in.', 'type': 'auth_error', 'param': 'None', 'code': '401'}}


Claude then was able to debug that I had to run my API_KEY and OPENAI_API_KEY in the terminal with both of them being the same key along with the run streamlit command:

OPENAI_API_KEY="YOUR_KEY_HERE" API_KEY="YOUR_KEY_HERE" streamlit run assign_2.py