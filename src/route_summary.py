def generate_route_summary(path, distance):

    summary = "\n===== ROUTE SUMMARY =====\n"

    summary += f"\nRoute: {' -> '.join(path)}"

    summary += f"\nTotal Distance: {distance}"

    summary += "\nStatus: Route Successfully Found"

    return summary


def save_report(summary):

    with open("outputs/route_report.txt", "w") as file:
        file.write(summary)

    print("\nReport Saved Successfully!")