import requests
import csv
from collections import defaultdict
from tenable.io import TenableIO
 
# ==========================
# CONFIG
# ==========================
ACCESS_KEY = ""
SECRET_KEY = ""
BASE_URL = "https://cloud.tenable.com"
tio = TenableIO(ACCESS_KEY, SECRET_KEY)
CSV_FILE = "sample-tags.csv"
  
# ==========================
# GET NETWORK UUID MAP
# ==========================

def get_network_map():
    network_map = {} 
    for net in tio.networks.list():
        network_map[net['name']] = net['uuid']
    return network_map
# ==========================
# MAIN
# ==========================

def main():
    grouped = defaultdict(list) 
    
    # Load CSV
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        required_cols = {"Category", "Value", "IP Range", "Network"}
        if not required_cols.issubset(reader.fieldnames):
            raise Exception(f"CSV must contain columns: {required_cols}")
 
        for row in reader:
            key = (row["Category"].strip(), row["Value"].strip())
            grouped[key].append(row)
 
    # Get network mapping
    network_map = get_network_map()
 
    # Process each tag
    for (category, value), rows in grouped.items():
        print(f"\nProcessing: {category} -> {value}")
        filters = []
        network_uuid = None
 
        for row in rows:
            ip = row["IP Range"].strip()
            network_name = row["Network"].strip()
 
            if ip:
                filters.append(("ipv4", "eq", ip))
 
            if network_name:
                if network_name not in network_map:
                    raise Exception(f"Network not found: {network_name}")
                network_uuid = network_map[network_name]
 
        # Add network filter (only once)
        if network_uuid:
            filters.append(("network_id", "eq", network_uuid))
 
        # Create tag
        try:
            tio.tags.create(
                category,
                value,
                f"Dynamic tag for {value}",
                filters=filters
            )
            print("Tag created")
 
        except Exception as e:
            if "already exists" in str(e).lower():
                print("ℹ️ Tag already exists, skipping")

            else:
                print(f"Error: {e}")
 
if __name__ == "__main__":
    main()