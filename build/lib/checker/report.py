import json

def generate_report(results, output_file):
    try:
        if not results:
            print("No complexity results to generate report.")
            return

        # Writing the results to a JSON file
        with open(output_file, "w") as file:
            json.dump(results, file, indent=4)

        print(f"Report generated successfully: {output_file}")

    except Exception as e:
        print(f"Error generating report: {e}")
