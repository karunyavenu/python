web_development = ["Asha", "Rahul", "Meera"]
data_science = ["Arjun", "Priya", "Vijay"]
ui_ux_design = ["Anu", "Kiran", "Neha"]
all_participants = [web_development, data_science, ui_ux_design]
web_development.append("Ravi")
data_science.insert(1, "Sneha")
ui_ux_design.pop()
copied_data_science = data_science.copy()
data_science.clear()
print("First two Web Development participants:", web_development[:2])
name_lengths = [len(name) for name in copied_data_science]
print("Name lengths:", name_lengths)
asha_present = any("Asha" in workshop for workshop in all_participants)
print("Is Asha in any workshop?", asha_present)
first_participants = (
    web_development[0],
    copied_data_science[0],
    ui_ux_design[0]
)

print("First participants tuple:", first_participants)