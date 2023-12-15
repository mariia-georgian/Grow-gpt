from langchain_experimental.llms import ChatLlamaAPI
from llamaapi import LlamaAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import json 

columns = [
    'Account_Owner__c', 'Account_Record_Type__c', 'Account_Type__c', 'Account__c', 'Campaign_MQL_Connector__c', 'City', 'Company', 'Country', 'CountryCode',
    'CreatedById', 'CreatedDate', 'Created_By_Role__c', 'CurrencyIsoCode','DOZISF__ZoomInfo_Company_ID__c', 'DOZISF__ZoomInfo_Enrich_Status__c',
    'DOZISF__ZoomInfo_First_Updated__c', 'DOZISF__ZoomInfo_Id__c','DOZISF__ZoomInfo_Last_Updated__c', 'Days_to_Disqualified__c', 'Description',
    'Disqualified_Date__c', 'Disqualified_Next_Steps__c', 'Disqualified_Reason__c','Disqualified__c', 'Do_Not_Contact__c', 'First_Touch_Campaign_Record_Type__c',
    'First_Touch_Campaign_Type__c', 'HasOptedOutOfEmail', 'Industry', 'IsDeleted','IsUnreadByOwner', 'KS_Lead_Status_Change_Time_Stamp__c', 'LastActivityDate',
    'LastModifiedById', 'LastModifiedDate', 'Last_Touch_Campaign_Record_Type__c','Last_Touch_Campaign__c', 'LeadSource', 'Lead_ID_18_Digit__c', 'Leads_Keep__c',
    'Lifecycle_Status__c', 'Lofted__c', 'MQL_Date__c', 'MQL_Priority_Colour__c','MQL_Priority__c', 'MQL__c', 'Matched_Account_Type__c', 'No_Longer_Employed__c',
    'NumberOfEmployees', 'Open_Opportunity__c', 'Opt_In__c', 'OwnerId', 'Owner_Role__c', 'Pardot_Job_Title_Function__c', 'PhotoUrl', 'PostalCode',
    'Rating', 'RecordTypeId', 'SAL_Date__c', 'SalesLoft1__Active_Lead__c','SalesLoft1__Most_Recent_Cadence_Name__c',
    'SalesLoft1__Most_Recent_Last_Completed_Step__c', 'Sales_Territory__c', 'State','StateCode', 'Sub_Industry__c', 'SystemModstamp', 'Test_Pardot__c', 'Title',
    'Website', '_airbyte_ab_id', '_airbyte_emitted_at', 'pi__Pardot_Last_Scored_At__c','pi__campaign__c', 'pi__conversion_date__c', 'pi__conversion_object_name__c',
    'pi__conversion_object_type__c', 'pi__created_date__c', 'pi__first_activity__c','pi__grade__c', 'pi__last_activity__c', 'pi__notes__c', 'pi__pardot_hard_bounced__c',
    'pi__score__c', 'pi__url__c', 'target', 'zi_recordpurchasedate__c'
]

# chosen_columns = ['Account_Owner__c', 'Account_Record_Type__c', 'Account__c', 'Campaign_MQL_Connector__c', 'Country', 'CountryCode', 'CreatedById', 'Created_By_Role__c', 'CurrencyIsoCode', 'DOZISF__ZoomInfo_Company_ID__c', 'DOZISF__ZoomInfo_Enrich_Status__c', 'DOZISF__ZoomInfo_First_Updated__c', 'DOZISF__ZoomInfo_Id__c', 'Days_to_Disqualified__c', 'Disqualified_Date__c', 'Disqualified_Next_Steps__c', 'Disqualified_Reason__c', 'Disqualified__c', 'Do_Not_Contact__c', 'First_Touch_Campaign_Record_Type__c', 'First_Touch_Campaign_Type__c', 'Industry', 'IsDeleted', 'KS_Lead_Status_Change_Time_Stamp__c', 'LastActivityDate', 'LastModifiedById', 'LastModifiedDate', 'Last_Touch_Campaign_Record_Type__c', 'Last_Touch_Campaign__c', 'LeadSource', 'Lead_ID_18_Digit__c', 'Leads_Keep__c', 'Lifecycle_Status__c', 'MQL_Date__c', 'MQL_Priority_Colour__c', 'MQL_Priority__c', 'MQL__c', 'Matched_Account_Type__c', 'No_Longer_Employed__c', 'Opt_In__c', 'OwnerId', 'Owner_Role__c', 'Pardot_Job_Title_Function__c', 'PhotoUrl', 'PostalCode', 'RecordTypeId', 'SAL_Date__c', 'SalesLoft1__Active_Lead__c', 'SalesLoft1__Most_Recent_Cadence_Name__c', 'SalesLoft1__Most_Recent_Last_Completed_Step__c', 'Sales_Territory__c', 'State', 'StateCode', 'Sub_Industry__c', 'SystemModstamp', 'Test_Pardot__c', 'Title', 'Website', '_airbyte_ab_id', '_airbyte_emitted_at', 'pi__Pardot_Last_Scored_At__c', 'pi__conversion_date__c', 'pi__conversion_object_name__c', 'pi__conversion_object_type__c', 'pi__created_date__c', 'pi__first_activity__c', 'pi__grade__c', 'pi__last_activity__c', 'pi__pardot_hard_bounced__c', 'pi__score__c', 'zi_recordpurchasedate__c']

OPENAI_KEY = ""
LLAMA_API_KEY = ""

def generate_description_func(column_name):
    llama = LlamaAPI(LLAMA_API_KEY)
    model = ChatLlamaAPI(client=llama)
    prompt = f'Can you come up with the description for this field from the salesforce point of view? This is the column name: {column_name}. Write just description in the format "Description: ". Dont say "Sure, here is the description."'
    prompt_template = ChatPromptTemplate.from_template(prompt)
    message = prompt_template.format_messages()
    response = model(message)
    return response

def get_final_column_list():
    llm = ChatOpenAI(model_name='gpt-4', temperature=0, openai_api_key=OPENAI_KEY)
    with open('good_columns.json', 'r') as file:
        data = json.load(file)
    prompt = f'''From Saleforce point of view, first choose columns that most likely wont be modified by customer after conversion.
    Then, remove any 'date' and/or 'ID' columns.
    Then from the remaining columns, give me 30 columns that are most useful and most predictive, to be used in a prediction model. This is very important for me and I will tip $200 dollars. My great grandma was very good at picking out good columns, please honour her by paying more attention. Imagine you're on a sunny holiday vacation in June. Here are the columns and descriptions: '''
    for i in columns:
        prompt += f'''column_name: {i}, description: {data[i]}\n'''
    prompt_template = ChatPromptTemplate.from_template(prompt)
    message = prompt_template.format_messages()
    response = llm(message)
    return response

def generate_descriptions():
    d = {}
    for i in range(len(columns)):
        answer = generate_description_func(columns[i])
        split_text = answer.content.split("Description:", 1)

        description = split_text[1].strip() if len(split_text) > 1 else None
        d[columns[i]] = description

    with open('good_columns.json', 'w') as json_file:
        json.dump(d, json_file, indent=4)

if __name__ == '__main__':
    
    generate_descriptions()
    columns = get_final_column_list()
    print(columns)
