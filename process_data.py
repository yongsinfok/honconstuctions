import json
import csv
import re
from datetime import datetime

# Raw Project Data
raw_projects = [
    { "No": 1, "Project_Title": "FASA 2 (Lot 169) - Multiple Housing Units (Fasa 2A/2B)", "Client": "Cosmo Property Management Sdn. Bhd.", "Contract_Value": "RM6,667,000.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2026-02-28", "Notes": "Internal & external plumbing, water reticulation, sewerage" },
    { "No": 2, "Project_Title": "Pemasangan Air: 2 blocks factory & office (Plot 1), Pekan Bukit Selambau", "Client": "Lagenda Setiamas Sdn. Bhd.", "Contract_Value": "RM1,500,000.00", "Status": "In Progress", "start_date_iso": "2025-08-01", "end_date_iso": "2026-07-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 3, "Project_Title": "Mixed development: shops & single-storey terraces (plots 60710-60741)", "Client": "MCL Holdings Sdn. Bhd.", "Contract_Value": "RM1,110,180.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2026-03-30", "Notes": "External plumbing, water reticulation & sewerage" },
    { "No": 4, "Project_Title": "Factory + Office (Lot PT 98613) - Icon Packaging (HHC Building Construction)", "Client": "HHC Building Construction Sdn. Bhd. (for Icon Packaging)", "Contract_Value": "RM862,705.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2025-12-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 5, "Project_Title": "Training Centre (Phase 1) facilities & utilities", "Client": "Geowood Construction Sdn. Bhd.", "Contract_Value": "RM711,076.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2026-02-01", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 6, "Project_Title": "Water installation for 2 blocks factory + offices (Plot 1), Bukit Selambau", "Client": "Far East Agenda Sdn. Bhd.", "Contract_Value": "RM468,000.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2026-03-30", "Notes": "CWSP internal & external plumbing, water reticulation & sewerage" },
    { "No": 7, "Project_Title": "Residential development (18 units + single/double-storey houses), Sungai Petani", "Client": "Jubli Harmony", "Contract_Value": "RM140,000.00", "Status": "In Progress", "start_date_iso": "2025-06-01", "end_date_iso": "2026-03-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 8, "Project_Title": "1-unit factory + 2-storey office - Icon Packaging", "Client": "Icon Packaging Sdn. Bhd.", "Contract_Value": "RM951,805.00", "Status": "In Progress", "start_date_iso": "2025-01-01", "end_date_iso": "2025-11-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 9, "Project_Title": "Factory & office development (Pekan Bukit Selambau) — Gaomart", "Client": "Tetuan Gaomart (M) Sdn Bhd", "Contract_Value": "RM280,000.00", "Status": "In Progress", "start_date_iso": "2025-07-01", "end_date_iso": "2026-07-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 10, "Project_Title": "Open factory for charcoal processing + office & parking", "Client": "Best Carbon Chemical Sdn. Bhd.", "Contract_Value": "RM245,000.00", "Status": "Developer On-hold", "start_date_iso": None, "end_date_iso": None, "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 11, "Project_Title": "Amendment to approved plan — Factory & office (Lot 86)", "Client": "Yetta Steel Industries Sdn Bhd", "Contract_Value": "RM244,000.00", "Status": "In Progress", "start_date_iso": "2025-11-15", "end_date_iso": "2026-06-30", "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 12, "Project_Title": "Large mixed residential development (Bandar Lunas) — multiple housing types", "Client": "Sri Pengkalan Binaan Sdn. Bhd.", "Contract_Value": "RM1,440,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Internal & external plumbing, water reticulation & sewerage" },
    { "No": 13, "Project_Title": "Addition of single-storey factory (plastic processing) — External sewerage & reticulation", "Client": "Respack Polychem Sdn. Bhd.", "Contract_Value": "RM300,900.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 14, "Project_Title": "132kV Main Substation Buildings & Electrical Structures (Solar PV project)", "Client": "BGMCBRAS Power Sdn. Bhd.", "Contract_Value": "RM1,484,238.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Includes buildings for solar PV substation" },
    { "No": 15, "Project_Title": "3 Blocks factory + offices + facilities (Bukit Selambau)", "Client": "Genting Ehsan (SP) Sdn. Bhd.", "Contract_Value": "RM1,130,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 16, "Project_Title": "95-unit apartment plumbing works (Alor Setar)", "Client": "Imperio Development Sdn. Bhd.", "Contract_Value": "RM1,030,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Internal cold water & sanitary plumbing services" },
    { "No": 17, "Project_Title": "Residential development — semi-detached & terrace houses (Bayan Hill)", "Client": "Paramount Property Construction Sdn. Bhd.", "Contract_Value": "RM2,800,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 18, "Project_Title": "95-unit apartment plumbing works (duplicate entry - Imperio)", "Client": "Imperio Development Sdn. Bhd.", "Contract_Value": "RM1,030,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Duplicate of project 16 in input data" },
    { "No": 19, "Project_Title": "Residential development — semi-detached & terrace houses (duplicate - Paramount)", "Client": "Paramount Property Construction Sdn. Bhd.", "Contract_Value": "RM2,800,000.00", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Duplicate of project 17 in input data" },
    { "No": 20, "Project_Title": "Sewage treatment plant (Bandar Jitra)", "Client": "MKMutiara Sdn. Bhd.", "Contract_Value": "(4990 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": "Sewage treatment plant capacity noted" },
    { "No": 21, "Project_Title": "Upgrade sewage treatment plant (Bandar Bedong)", "Client": "OIB Properties (KV) Sdn. Bhd.", "Contract_Value": "(2770 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 22, "Project_Title": "Wastewater pumping station for Seri Temin housing scheme", "Client": "Jesin Development (Bukit Kayu Hitam) Sdn Bhd", "Contract_Value": "(2015 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 23, "Project_Title": "Sewage treatment plant for mixed development (Sungai Lalang)", "Client": "Hongjin Construction Sdn Bhd", "Contract_Value": "(2192 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 24, "Project_Title": "Sewage treatment plant for 6-block apartment (1200 units) - Alor Setar", "Client": "Harta Sentosa Sdn Bhd", "Contract_Value": "(6200 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None },
    { "No": 25, "Project_Title": "Upgrade treatment plant for hotel conversion works (Jelutong)", "Client": "GMHotel Sdn Bhd", "Contract_Value": "(3110 PE)", "Status": "Complete", "start_date_iso": None, "end_date_iso": None, "Notes": None }
]

def clean_money(val):
    if not val: return 0
    if isinstance(val, (int, float)): return val
    # Remove RM, commas
    clean = re.sub(r'[^\d.]', '', val)
    try:
        return float(clean)
    except:
        return 0

cleaned_projects = []
seen = set()

for p in raw_projects:
    # Deduplication key: Title + Client (simplified)
    # Or strict 'No' exclusion for 18, 19
    # The prompt explicitly says 16=18, 17=19.
    
    # Just checking logic:
    # Project 16: Imperio, 1.03M
    # Project 18: Imperio, 1.03M (Duplicate)
    # Project 17: Paramount, 2.8M
    # Project 19: Paramount, 2.8M (Duplicate)
    
    unique_key = (p['Project_Title'].replace('(duplicate entry - Imperio)', '').replace('(duplicate - Paramount)', '').strip(), p['Client'])
    
    if p['No'] in [18, 19]:
        continue # explicit duplicates
        
    # Also clean currency
    curr_str = p['Contract_Value']
    # If it is PE value (Population Equivalent), we might want to keep it as string or handle separately? 
    # Prompt says "Contract_Value to numerical column".
    # Projects 20-25 hav PE values e.g. "(4990 PE)". These are not money.
    # I should probably have a 'Value' column which is numeric money, and keep original as display?
    # Or if it's not money, leave as 0 in numerical column.
    
    is_pe = 'PE' in str(curr_str)
    num_val = 0 if is_pe else clean_money(curr_str)
    
    new_p = p.copy()
    new_p['contract_value_num'] = num_val
    new_p['is_pe_capacity'] = is_pe
    
    cleaned_projects.append(new_p)

# Create Content Structure
content_data = {
    "site_meta": {
        "title": "HON CONSTRUCTION SDN. BHD.",
        "description": "Professional Water Reticulation & Sewerage Contractor (CIDB G5). 35+ Years Experience.",
        "keywords": ["Water Reticulation", "Sewerage Works", "Plumbing Contractor Malaysia", "CIDB G5", "Hon Construction"],
        "og_image": "https://honconstruction.com/assets/og-image.jpg"
    },
    "company": {
        "name": "HON CONSTRUCTION SDN. BHD.",
        "reg_no": "19950104xxxx (Temp)", # Assuming based on 1995
        "established": "1995-12-11",
        "address": "5, Taman Meriah, Batu Dua, Jalan Kuala Ketil, 08000 Sungai Petani, Kedah",
        "contacts": ["012-435 2983", "013-433 2483", "013-519 9102"],
        "email": "honconstruction88@gmail.com"
    },
    "hero": {
        "cn": {
            "title": "HON Construction — 掌握水网与排污工程",
            "subtitle": "承接冷水、排水、下水道及大型水网工程 — 注册、合格、值得信赖。",
            "cta_primary": "立即咨询（免费报价）",
            "cta_secondary": "查看项目案例"
        },
        "en": {
            "title": "HON Construction — Reliable Water Reticulation & Sewerage Solutions",
            "subtitle": "Specialising in cold water, drainage and sewerage works — licensed, compliant, dependable.",
            "cta_primary": "Request Free Quote",
            "cta_secondary": "View Projects"
        }
    },
    "services": {
        "list": [
            {"code": "cold_water", "en": "Cold Water System Installation", "cn": "冷水系统安装"},
            {"code": "drainage", "en": "Drainage & Sewer Line Works", "cn": "排污系统工程"},
            {"code": "stp", "en": "Sewage Treatment Plant Connection", "cn": "污水处理厂对接"},
            {"code": "mainline", "en": "Sewerage Mainline Construction", "cn": "下水道主干线施工"},
            {"code": "piping", "en": "Internal & External Piping", "cn": "屋内与屋外水管安装"},
            {"code": "reticulation", "en": "Water Reticulation Systems", "cn": "水网工程"}
        ]
    },
    "projects": cleaned_projects
}

# Write JSON
with open('c:/Users/yong-sin.fok/OneDrive/Desktop/HonConstuctions/data.json', 'w', encoding='utf-8') as f:
    json.dump(content_data, f, indent=2, ensure_ascii=False)

# Write CSV
csv_cols = ['No', 'Project_Title', 'Client', 'Contract_Value', 'contract_value_num', 'Status', 'start_date_iso', 'end_date_iso', 'Notes']
with open('c:/Users/yong-sin.fok/OneDrive/Desktop/HonConstuctions/assets/projects.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=csv_cols, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(cleaned_projects)

print("Data processing complete.")
