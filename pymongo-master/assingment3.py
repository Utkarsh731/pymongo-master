mongoimport C:\Users\UTKARSH\Downloads\boxoffice.json -d boxoffice -c records --drop --jsonArray
 db.records.find({"meta.rating":{$gt:9.2},"meta.runtime":{"$lt":100}}).pretty()
 db.records.find({$or:[{"genre":"drama","genre":"action"}]}).pretty()
  db.records.find({$expr:{"$gt":["$visitors","$expectedVisitors"]}}).pretty()
