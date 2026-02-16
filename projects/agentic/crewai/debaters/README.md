## Debating Agents using CrewAI

**Description:**
Two debating agents present arguments for and against a given motion.
A third judge agent evaluates their arguments and determines the winner.

**Note:**
Install crewai tool on PC at global level from command-prompt using admin privilages:
- >uv tool install crewai
- >uv tool update-shell

Check official doc for installation - https://docs.crewai.com/en/installation

**Commands per project:**
- >crewai --help
- >crewai create crew <your_project_name>
- >cd <to_proj_folder>
- >crewai install  #insatll dependent pkgs
- >uv add crewai litellm   #litellm for openrouter

(pip install 'litellm[proxy]' not worked)

**Execute:**
- >crewai run  #or
- >uv run crewai run  
