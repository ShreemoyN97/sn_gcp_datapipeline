import pandas as pd
from google.cloud import storage

def process_and_save_data(request):
    """Cloud Function to process data and save it to Google Cloud Storage."""
    try:
        # Set the GCS file paths
        input_path = 'gs://sn_data_landing_zone/DataCoSupplyChainDataset.csv'
        base_output_path = 'gs://sn_data_processing_zone/'
        project_id = 'supply-chain-001'  # Your Google Cloud project ID

        # Load data from GCS
        client = storage.Client(project=project_id)
        bucket = client.get_bucket(input_path.split('/')[2])
        blob = bucket.blob(input_path.split('/', 3)[-1])  # Remove 'gs://bucket-name/' prefix
        data = pd.read_csv(blob.download_as_string())

        # Data transformation sections
        customer_columns = ['Customer Id', 'Customer Email', 'Customer Fname', 'Customer Lname',
                            'Customer Password', 'Customer Segment', 'Customer Street',
                            'Customer City', 'Customer State', 'Customer Country', 'Customer Zipcode']
        order_columns = ['Order Id', 'Customer Id', 'Order Status', 'Sales per customer', 'Order Profit Per Order', 'Shipping Mode']
        order_item_columns = ['Order Item Id', 'Order Id', 'Order Item Product Price', 'Order Item Quantity', 'Order Item Discount Rate']
        product_columns = ['Product Card Id', 'Product Name', 'Product Price', 'Product Category Id']
        product_category_columns = ['Category Id', 'Category Name']
        department_columns = ['Department Id', 'Department Name']

        # Create DataFrames for each data category
        customers_df = data[customer_columns].drop_duplicates().reset_index(drop=True)
        orders_df = data[order_columns].drop_duplicates().reset_index(drop=True)
        order_items_df = data[order_item_columns].drop_duplicates().reset_index(drop=True)
        products_df = data[product_columns].drop_duplicates().reset_index(drop=True)
        product_categories_df = data[product_category_columns].drop_duplicates().reset_index(drop=True)
        departments_df = data[department_columns].drop_duplicates().reset_index(drop=True)

        # Save the transformed data to new GCS paths
        datasets = {'Customers.csv': customers_df, 'Orders.csv': orders_df, 'Order_Items.csv': order_items_df,
                    'Products.csv': products_df, 'Product_Categories.csv': product_categories_df, 'Departments.csv': departments_df}
        for filename, df in datasets.items():
            blob = bucket.blob(base_output_path + filename)
            blob.upload_from_string(df.to_csv(index=False), content_type='text/csv')

        return 'Data processing complete. Files saved to GCS.'

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return f"An error occurred: {str(e)}", 500
