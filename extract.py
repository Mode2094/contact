import csv

csv_file = 'WhatsApp_Contacts_2026-09-01.csv'
js_array = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['Saved Name'].strip()
        # Remove quotes if present
        if name.startswith('"') and name.endswith('"'):
            name = name[1:-1]
            
        phone = row['Phone Number'].strip()
        if phone.startswith('"') and phone.endswith('"'):
            phone = phone[1:-1]
            
        js_array.append(f'        {{ name: "{name}", number: "{phone}" }}')

js_content = "const contactsData = [\n" + ",\n".join(js_array) + "\n    ];"

with open('contacts.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_content)
