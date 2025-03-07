import argparse
from radon.visitors import ComplexityVisitor

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        visitor = ComplexityVisitor.from_code(code)
        results = []
        for block in visitor.functions + visitor.classes:
            results.append({
                "function": block.name,
                "complexity": block.complexity,
                "lineno": block.lineno
            })
        print(f" Function: {block.name}, \n Complexity: {block.complexity}, \n Line: {block.lineno}")


        return results

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Code Complexity Checker")
    parser.add_argument("--file", type=str, required=True, help="Path to the Python file")
    args = parser.parse_args()

    file_path = args.file
    analyze_file(file_path)

        
if __name__ == "__main__":
    main()
