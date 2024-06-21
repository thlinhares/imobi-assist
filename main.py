import os
from pathlib import Path
from scripts.download import Download
from scripts.extract import Extractor
#from scripts.transform import Transformer
#from scripts.load import Loader


def main():
    data_dir = "data/"

    # Create the output directory if it doesn't exist
    Path(data_dir).mkdir(parents=True, exist_ok=True)

    # Initialize download in the 'data/' directory
    download = Download(data_dir)
    itbi_report_dict = download.get_itbi_report()

    # Initialize the Extractor and load data from the 'data/' directory
    extractor = Extractor(itbi_report_dict[202404]['path'])
    itbi_data = extractor.load_itbi_report()
    print(itbi_data)

    # Initialize the Transformer with the loaded data
#    transformer = Transformer(taxi_data, payment_data, vendor_data)

    # Process the loaded data to transform it
#    transformed_data = transformer.process_data()

    # Initialize the Loader to save the transformed data to 'output/etl_output.csv'
#    loader = Loader(output_dir)

    # Save the transformed data to a CSV file
#    loader.save_data(transformed_data, filename='etl_output.csv')


if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()
