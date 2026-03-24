import os

def main() -> None:

    keywords=["ERROR", "WARNING", "INFO"]
    analyze_result={}
    log_file_name = "sample.log"
    analyze_result_file_name = "analyze_result.txt"

    try:
        current_dir = os.path.dirname(__file__)
        sample_log_path = os.path.join(current_dir, log_file_name)
        analyze_result_path = os.path.join(current_dir, analyze_result_file_name)
        print("\nLog Summary")
        print("-" * 20)

        with open(sample_log_path, "r", encoding = 'utf-8') as log_file:
            lines = log_file.readlines()
            for word in keywords:
                counter = 0
                for row in lines:
                    if word in row.upper():
                        counter +=1
                
                analyze_result[word] = counter
                print(f"{word}: {counter}")

            total = sum(analyze_result.values())
            print(f"Total entries matched: {total}")

    except PermissionError:
        print(f"Error: You do not have permission to read {log_file_name}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        with open(analyze_result_path, "a", encoding = 'utf-8') as result_file:
            for key, value in analyze_result.items():
                result_file.write(f"{key} message has found {value} times in the {log_file_name} file.\n")

    except PermissionError:
        print(f"Error: You do not have permission to read {analyze_result_file_name}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()