import requests
import pymongo
response=requests.get("https://api.github.com/repos/pallets/flask/issues")
data= response.json()
client= pymongo.MongoClient("mongodb://root:s123@mongo_compose:27017/")
db=client["mi-db"]
coll=db["issues"]
bulk=[]
a=['id', 'url', 'repository_url', 'labels_url', 'comments_url', 'events_url', 'html_url', 'node_id', 'number', 'title', 'user' , 'labels', 'state', 'locked', 'assignee', 'assignees', 'milestone', 'comments', 'created_at', 'updated_at', 'closed_at', 'author_association', 'active_lock_reason','draft','pull_request', 'body', 'reactions','timeline_url', 'performed_via_github_app', 'state_reason'] 
b=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
for i in range (0, len (data),1):
    insert_data={}
    for j in range (0,len(a),1):
        if j==0:
            insert_data['_id']=b[i]

            insert_data['issues_id']=data[i][a[j]]
        elif len(data[i])==28:
            if j==23:
               insert_data['draft']= ("null")
            elif j==24:
                insert_data['pull_request']= ("null")
            else:   
               insert_data[a[j]]=data[i][a[j]]
        else:
            insert_data[a[j]]=data[i][a[j]]
    bulk.append(insert_data)
result = coll.insert_many(bulk)
print(f"¡Se ha terminado la inserción de datos!: {result.inserted_ids}")

