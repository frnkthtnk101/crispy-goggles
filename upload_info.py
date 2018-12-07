import csv
import requests
'''
0 - course
1 - username
2 - uid
3 - cid
4 - eid
5 - role
'''
def main():
    site = 'school'
    code = 'my cool code'
    csv_file = 'my cool cvsfile'
    base_url = f"https://{site}.instructure.com/api/v1/accounts/1/enrollments/:id"
    header = {'Authorization':f'Bearer {code}'}
    with open(csv_file,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter='\t')
        for row in reader:
            URL = base_url.replace(":id",row[4])
            response = requests.get(URL,headers=header)
            if response.status_code == 200:
                data = response.json()
                for k in data.keys():
                    print(f"{data[k]}\t",end='')
                print('',flush=True)


    

main()
