import pandas as pd
import requests
import os


warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    a_office_df = pd.read_xml(r'../Data/A_office_data.xml')
    b_office_df = pd.read_xml(r'../Data/B_office_data.xml')
    hr_data_df = pd.read_xml(r'../Data/hr_data.xml')

    # reset indexes
    a_office_df = a_office_df.reset_index(drop=True)
    b_office_df = b_office_df.reset_index(drop=True)

    hr_data_df = hr_data_df.reset_index(drop=True).set_index('employee_id')

    # create separate_index for a/b offices
    a_office_df['employee_office_id'] = 'A' + a_office_df['employee_office_id'].astype(str)
    b_office_df['employee_office_id'] = 'B' + b_office_df['employee_office_id'].astype(str)

    # set new index
    a_office_df = a_office_df.set_index('employee_office_id')
    b_office_df = b_office_df.set_index('employee_office_id')

    print(list(a_office_df.index))
    print(list(b_office_df.index))
    print(list(hr_data_df.index))
