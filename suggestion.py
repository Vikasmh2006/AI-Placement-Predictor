def suggest(cgpa,internship,project,technical,communication):

    suggestions=[]

    if cgpa<7:
        suggestions.append("Improve CGPA by focusing on academics")

    if internship==0:
        suggestions.append("Do at least 1 Internship")

    if project==0:
        suggestions.append("Build Innovative Projects")

    if technical==0:
        suggestions.append("Complete Technical Courses (Python, ML etc)")

    if communication<5:
        suggestions.append("Improve Communication Skills")

    return suggestions