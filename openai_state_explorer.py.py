import openai
import json
import xlsxwriter

country_code_list = [  "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CS", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "EU", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NT", "NU", "NZ", "OM", "OR", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "UN", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW" ]
openai.api_key = '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'
openai.default_headers = {"x-foo": "true"}

#client = OpenAI()
for current_country in country_code_list:
    print("===========================================")
    print(current_country)
    query_1 = "Consider that the United Kingdom has such states/provinces/areas which includes Armagh,Angus/Forfarshire, Antrim, Ayrshire, Bedfordshire, Banffshire, Berkshire, Brecknockshire and others"
    query_2 = "I need you to consider this and give me the equivalent states/provinces for the following country with the next country code"
    query_3 = "Note, Give me the response in array format, with each item in double quotes, no need for any other text, no need for any newline character as well, just the items in quotes. Give me such result for the NEXT country code: "
    query_4 = current_country

    final_query = query_1 + query_2 + query_3 + query_4


    completion = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": final_query
        }
      ]
    )

    result = completion.choices[0].message


    #print()
    
    array_result = result.content
    array = []
    try:
        array = json.loads(array_result)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        array = []
        
    # Loop through the array
    for element in array:
        print(element)
        
# done obtaining the list of states in the country, next is to store it in excel

    worksheet_name = '' + current_country + '.xlsx'
    workbook = xlsxwriter.Workbook( worksheet_name )
    
    worksheet = workbook.add_worksheet()

    
    country_code = []
    for i in array:
        country_code.append(current_country)

    excel_output = [  country_code, array ]

    row = 0

    for col, data in enumerate(excel_output):
        worksheet.write_column(row, col, data)
    workbook.close()
