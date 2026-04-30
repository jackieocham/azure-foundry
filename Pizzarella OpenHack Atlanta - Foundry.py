# Pizzarella OpenHack Atlanta - Foundry

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

# Format: "https://resource_name.ai.azure.com/api/projects/project_name"
PROJECT_ENDPOINT = "https://pizzarella-openhack-atlanta.services.ai.azure.com/api/projects/proj-default"
AGENT_NAME = "Pizzarella"

# Create project client to call Foundry API
project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

# Create an agent with a model and instructions
agent = project.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model="gpt-4o",  # supports all Foundry direct models"
        instructions="You are a pizza assistant that places pizza orders.",
    ),
)
print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")