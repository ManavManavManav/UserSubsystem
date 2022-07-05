python3 auth.py AddUser manav iEatPotatoes >>output2.txt
python3 auth.py AddUser jason iLikeCars >>output2.txt
python3 auth.py AddUser shreya iLikeTomatoes >>output2.txt
python3 auth.py AddUser manav2 "" >>output2.txt
python3 auth.py AddUser manav "" >>output2.txt
python3 auth.py AddUser "" "" >>output2.txt
python3 auth.py Authenticate manav iEatPotatoes >>output2.txt
python3 auth.py Authenticate jason iLikeCars >>output2.txt
python3 auth.py Authenticate shreya iLikeCase >>output2.txt
python3 auth.py Authenticate carly "iLikeSomething" >>output2.txt
python3 auth.py SetDomain manav admin >>output2.txt
python3 auth.py SetDomain shreya normal >>output2.txt
python3 auth.py SetDomain raj normal >>output2.txt
python3 auth.py SetDomain shreya "" >>output2.txt
python3 auth.py SetDomain shreya admin >>output2.txt
python3 auth.py DomainInfo admin >>output2.txt
python3 auth.py DomainInfo normal >>output2.txt
python3 auth.py DomainInfo potatoLovers >>output2.txt
python3 auth.py DomainInfo "" >>output2.txt
python3 auth.py SetType hbo paid >>output2.txt
python3 auth.py SetType netflix paid >>output2.txt
python3 auth.py SetType "" "" >>output2.txt
python3 auth.py SetType youtube free >>output2.txt
python3 auth.py TypeInfo paid >>output2.txt
python3 auth.py TypeInfo free >>output2.txt
python3 auth.py TypeInfo "doesntExist" >>output2.txt
python3 auth.py TypeInfo "" >>output2.txt
python3 auth.py AddAccess watch admin paid >>output2.txt
python3 auth.py AddAccess watch normal free >>output2.txt
python3 auth.py AddAccess remove admin paid >>output2.txt
python3 auth.py AddAccess remove admin free >>output2.txt
python3 auth.py AddAccess add admin paid >>output2.txt
python3 auth.py AddAccess add admin free >>output2.txt
python3 auth.py AddAccess watch admin rentable >>output2.txt
python3 auth.py AddAccess watch normal rentable >>output2.txt
python3 auth.py AddAccess "" "" "" >>output2.txt
python3 auth.py CanAccess watch shreya hbo >>output2.txt
python3 auth.py CanAccess watch shreya netflix >>output2.txt
python3 auth.py CanAccess watch jason hbo >>output2.txt
python3 auth.py CanAccess remove manav hbo >>output2.txt
python3 auth.py CanAccess remove manav netflix >>output2.txt
python3 auth.py CanAccess remove manav youtube >>output2.txt
python3 auth.py CanAccess watch shreya youtube >>output2.txt
python3 auth.py CanAccess watch raj youtube >>output2.txt
rm types.json
rm domains.json
rm access.json
rm users.json


echo "Success
Success
Success
Success
Error: user exists
Error: username missing
Success
Success
Error: bad password
Error: no such user
Success
Success
Error no such user
Error: missing domain
Success
manav
shreya
shreya
Error: missing domain
success
success
Error: missing  object
success
hbo
netflix
youtube
Error: missing type_name
Success
Success
Success
Success
Success
Success
Success
Success
Error: missing operation
Success
Success
Error: access denied
Success
Success
Success
Success
Error: access denied" >correctOutput.txt




FILE1=correctOutput.txt
FILE2=output2.txt
if cmp --silent -- "$FILE1" "$FILE2"; then
  echo "TestPassed"
else
  echo "TestFailed"
fi

rm correctOutput.txt
rm output2.txt