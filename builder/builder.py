import os
import json

# Path to the JSON file containing the projects array

# Read the projects array from the JSON file
with open("builder/content/projects.json", 'r') as json_file:
    projects = json.load(json_file)

with open("builder/content/main.json", 'r') as json_file:
    main = json.load(json_file)

# Update the main README.md file
main_readme_path = "README.md"
main_readme_content = f"""
# {main["title"]}
## {main["description"]}
## Projects list
"""

# Generate the project list in the main README.md
for project in projects:
    project_name = project['name']
    project_directory = os.path.join(
        "projects", project_name.replace(" ", "_"))
    project_readme_path = os.path.join(project_directory, "README.md")
    main_readme_content += f"- [{project_name}]({project_readme_path})\n"
    first_project_image = project['images'][0]
    main_readme_content += f"![{first_project_image['desc']}]({project['name']}/assets/{first_project_image['path']})\n"

# Write the project list to the main README.md file
with open(main_readme_path, 'w') as main_readme_file:
    main_readme_file.write(main_readme_content)

# Create/update the README.md file for each project
for project in projects:
    project_name = project['name']
    project_directory = os.path.join(
        "projects", project_name.replace(" ", "_"))
    readme_path = os.path.join(project_directory, "README.md")

    # Generate the README content
    readme_content = f"# {project_name}\n\n"
    readme_content += f"**Used Technology:** {', '.join(project['technologies'])}\n\n"
    readme_content += f"**Project Link:** [{project_name}]({project['link']})\n\n"
    readme_content += f"**Project Website:** [{project_name} Website]({project['website']})\n\n"
    readme_content += "## Screenshots\n\n"

    for image in project['images']:
        readme_content += f"![{image['desc']}](assets/{image['path']})\n"
        readme_content += f"**Description:** {image['desc']}\n\n"
    print(readme_path)
    # Write the README content to the file
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)

print("README.md files updated successfully.")
