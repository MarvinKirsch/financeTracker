# main.py
from modules import pdf_reader, data_extractor, data_analyzer, visualizer, data_storage


def main():
    # Path to the folder containing your bank statements
    folder_path = "path_to_your_folder"

    # Read the PDFs
    bank_statements = pdf_reader.read_pdfs(folder_path)

    # Extract income and expenses data
    income_expenses = data_extractor.extract_data(bank_statements)

    # Analyze the data
    analysis = data_analyzer.analyze_data(income_expenses)

    # Create visualizations
    visualizer.create_visualizations(analysis)

    # Store the data
    data_storage.store_data(income_expenses)


if __name__ == "__main__":
    main()

