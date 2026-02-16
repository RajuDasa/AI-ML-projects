## Engineering Team:
- Team of agents (engieers) building the Application.
- Team includes: Lead, Backend, Frontend and Tester.
- Is part of exercise: update the crewAI project with dynamic addition of tasks based on Lead engineer plan.
- Use structured-output, callback and sub-crew (nested crew).
- Original solution - https://github.com/ed-donner/agents/tree/main/3_crew/community_contributions/software-engineering-crew

**Note:** 
- Requires Docker running in local system.
- Use strong models for quality output.
  
**Execution:**
- > crewai run
- check generated files in /output folder.
- > uv add gradio
- > output> uv run app.py

**Test:**
- > uv add pytest
- > output> uv run python -m pytest
  
