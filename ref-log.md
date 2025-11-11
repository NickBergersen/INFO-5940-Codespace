## What I Learned from Implementing a Multi-Agent Workflow

Implementing this multi-agent travel planner taught me the importance of clear role separation and specialized responsibilities. The Planner operates purely from its knowledge base to create comprehensive itineraries, while the Reviewer validates using real-time data through internet searches. This division of labor mirrors real-world workflows where different team members have distinct expertise and tools.

I learned that agent orchestration requires careful prompt engineering to ensure each agent produces outputs in formats the next agent can consume. The sequential pipeline demonstrated how breaking complex tasks into specialized subtasks improves overall output quality. Watching the agents collaborate—with the Planner generating creative itineraries and the Reviewer fact-checking details like museum hours and ticket prices—showed me how AI systems can complement each other's strengths and limitations.

## Challenges Faced and How I Addressed Them

The primary challenge was getting the Reviewer Agent to actually use the internet_search tool effectively. I ensured the tool was properly added to the reviewer_agent's tools list and crafted instructions that explicitly told the Reviewer when and why to search—checking opening hours, ticket prices, and current availability. Testing revealed that vague instructions led to the Reviewer skipping searches, so I made the tool usage requirements more explicit.

Another challenge was API key configuration in the Codespaces environment. The .env file approach wasn't working reliably, so I had to run my key configuration in the terminal each time along with the streamlit command.

## Creative Ideas and Design Choices

For the Planner instructions, I emphasized creating itineraries with specific times, locations, and cost breakdowns to make validation easier. I instructed the Planner to work "entirely from its own knowledge" to establish a clear baseline before fact-checking.

For the Reviewer, I designed instructions around a "Delta List" concept—requiring specific changes with concrete reasons rather than vague suggestions. This forces the Reviewer to be actionable and evidence-based, giving users transparency into changes and a ready-to-use final plan.



## GenAI assistance:

I used claude to help me with the following error:

Error code: 401 - {'error': {'message': 'Authentication Error, No api key passed in.', 'type': 'auth_error', 'param': 'None', 'code': '401'}}

Claude then was able to debug that I had to run my API_KEY and OPENAI_API_KEY in the terminal with both of them being the same key along with the run streamlit command:

OPENAI_API_KEY="YOUR_KEY_HERE" API_KEY="YOUR_KEY_HERE" streamlit run assign_2.py