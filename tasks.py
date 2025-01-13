from crewai import Task
from agents import planner, editor, writer

plan=Task(
    description=(
        "1. Prioritize the latest trends, key players, "
            "and noteworthy news on {topic}.\n"
        "2. Identify the linkedin target audience, considering "
            "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
            "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan document "
    "with an outline, audience analysis, "
    "SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
            "LinkedIn post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
		"3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "introduction with hooks, insightful body, "
            "and a CTA.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written linkedin post "
        "in text format, ready for publication,",
    agent=writer,
)

edit = Task(
    description=("Proofread the given linkedin post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written linkedin post in text format, "
                    "ready for publication, ",
    agent=editor
)