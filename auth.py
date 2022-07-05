import json
import sys
import os.path


# file io
def userMaker(uF):
    if os.path.exists(uF):
        if os.path.getsize(uF) == 0:
            with open(uF, 'w+') as fp:
                dict = {}
                json.dump(dict, fp)
            return 1
        else:
            pass
            return 1
    else:
        with open(uF, 'w+') as fp:
            dict = {}
            json.dump(dict, fp)
        return 0

def domainMaker(dF):
    if os.path.exists(dF):
        if os.path.getsize(dF) == 0:
            with open(dF, 'w+') as fp:
                lists = {}
                json.dump(lists, fp)
            return 1
        else:
            pass
            return 1
    else:
        with open(dF, 'w+') as fp:
            lists = {}
            json.dump(lists, fp)
        return 0

def typeMaker(tF):
    if os.path.exists(tF):
        if os.path.getsize(tF) == 0:
            with open(tF, 'w+') as fp:
                lists = {}
                json.dump(lists, fp)
            return 1
        else:
            pass
            return 1
    else:
        with open(tF, 'w+') as fp:
            lists ={}
            json.dump(lists, fp)
        return 0

def accessMaker(aF):
    if os.path.exists(aF):
        if os.path.getsize(aF) == 0:
            with open(aF, 'w+') as fp:
                lists = {}
                json.dump(lists, fp)
            return 1
        else:
            pass
            return 1
    else:
        with open(aF, 'w+') as fp:
            lists ={}
            json.dump(lists, fp)
        return 0

# functionality
def addUser(name, password):
    userMaker('users.json')

    f = open('users.json')
    dict = json.load(f)

    if name in dict:
        return 'Error: user exists'
    else:
        dict.update({name: password})
        with open('users.json', 'w+') as fp:
            json.dump(dict, fp)
        return 'Success'

def authenticate(name, password):

    if not os.path.exists('users.json'):
        return 'Error: no such user'

    f = open('users.json')
    dict = json.load(f)

    if name in dict:
        if(dict[name] == password):
            return 'Success'
        else:
            return 'Error: bad password'
    else:
        return 'Error: no such user'

def setDomain(name, domain):
    domainMaker('domains.json')

    fu = open('users.json')
    dict = json.load(fu)

    if not name in dict:
        return 'Error no such user'


    with open('domains.json') as fp:
        lists = json.load(fp)


    if domain in lists:
        if name in lists[domain]:
            return 'Success'
        else:
            lists[domain].append(name)
    else:
        lists[domain]=[name]





    with open('domains.json', 'w+') as fp:
        json.dump(lists, fp)

    return 'Success'

def domainInfo(domain):
    with open('domains.json') as fp:
        lists = json.load(fp)

    if not domain in lists:
        return None


    for name in lists[domain]:
        print(str(name))

def setType(object, typeName):
    typeMaker('types.json')

    with open('types.json') as fp:
        lists=json.load(fp)
    

    if(typeName) in lists:
        if object in lists[typeName]:
            print('already present')
            pass
        else:
            lists[typeName].append(object)
            with open('types.json', 'w+') as fp:
                json.dump(lists, fp)
    else:
        lists.update({typeName:[object]})
        with open('types.json', 'w+') as fp:
            json.dump(lists, fp)


    return 'success'

def typeInfo(typeName):

    with open('types.json') as fp:
        lists = json.load(fp)

    if not typeName in lists:
        pass
    else:
        for name in lists[typeName]:
            print(str(name))

def addAccess(operation, domain, typeName):
    domainMaker('domains.json')
    with open('domains.json') as fp:
        lists = json.load(fp)
    if domain in lists:
        pass;
    else:
        lists[domain]=[]
    with open('domains.json', 'w+') as fp:
        json.dump(lists, fp)



    typeMaker('types.json')
    with open('types.json') as fp:
        lists=json.load(fp)
    if(typeName) in lists:
        pass
    else:
        lists.update({typeName:[]})
    with open('types.json', 'w+') as fp:
        json.dump(lists, fp)




    accessMaker('access.json')
    with open('access.json') as fp:
        lists=json.load(fp)

    if operation in lists:
        if domain in lists[operation]:
            if typeName in lists[operation][domain]:
                return 'Success'
            else:
                lists[operation][domain].append(typeName)
        else:
            lists[operation][domain]=[typeName]
    else:
        lists[operation]={domain:[typeName]}
        

    with open('access.json','w+') as fp:
        json.dump(lists,fp)
    return 'Success'

def canAccess(operation, user, object):
    if not os.path.exists('access.json') or os.path.getsize('access.json')==0:
        print('Error: access denied')
        exit()
    if not os.path.exists('types.json') or os.path.getsize('types.json')==0:
        print('Error: access denied')
        exit()
    if not os.path.exists('domains.json') or os.path.getsize('domains.json')==0:
        print('Error: access denied')
        exit()
        
    with open('access.json') as fp:
        acs=json.load(fp)
    if operation not in acs:
        return 'Error: access denied'
    
    with open('domains.json') as fup:
        dom=json.load(fup)
    with open('types.json') as fip:
        typ=json.load(fip)

   
    

    #for each domain in domains.json file
    for d in dom:
        #for each user in that domain
        for usr in range(len(dom[d])):
            #if that user matches the one passed in canAccess function
            if dom[d][usr]==user:
                #for each category type of object
                for t in typ:
                    #for each object in that type
                    for obj in range(len(typ[t])):
                        #if that object matches the one passed in canAccess
                        if typ[t][obj]==object:
                            for op in acs:
                                #look for operation matching the param
                                if op==operation:
                                    for key in acs[op]:
                                        if key==d:
                                            if t in acs[op][key]:
                                                
                                                return 'Success'

                                
                    
    return 'Error: access denied'


try:
    action=sys.argv[1]
except:
    print('Error: missing arguments')
    exit()


if action=='AddUser':
    if(len(sys.argv)<4):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>4):
        print('Error: too many arguments for AddUser')
        exit()

    if sys.argv[2]=='':
        print('Error: username missing')
        exit()

    
    print(addUser(sys.argv[2],sys.argv[3]))
elif action=='Authenticate':

    if(len(sys.argv)<4):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>4):
        print('Error: too many arguments for Authenticate')
        exit()
    if sys.argv[2]=='':
        print('Error: username missing')
        exit()


    print(authenticate(sys.argv[2],sys.argv[3]))
elif action=='SetDomain':
    if(len(sys.argv)<4):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>4):
        print('Error: too many arguments for SetDomain')
        exit()

    if sys.argv[3]=='':
        print('Error: missing domain')
        exit()
    
    print(setDomain(sys.argv[2],sys.argv[3]))
elif action=='DomainInfo':
    if(len(sys.argv)<3):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>3):
        print('Error: too many arguments for DomainInfo')
        exit()

    if sys.argv[2]=='':
        print('Error: missing domain')
        exit()


    domainInfo(sys.argv[2])

elif action=='SetType':
    
    if(len(sys.argv)<4):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>4):
        print('Error: too many arguments for SetType')
        exit()

    if sys.argv[2]=='':
        print('Error: missing  object')
        exit()
    elif sys.argv[3]=='':
        print('Error: missing type_name')
        exit()

    print(setType(sys.argv[2],sys.argv[3]))




elif action=='TypeInfo':

    if(len(sys.argv)<3):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>3):
        print('Error: too many arguments for TypeInfo')
        exit()

    if sys.argv[2]=='':
        print('Error: missing type_name')
        exit()


    typeInfo(sys.argv[2])
elif action=='AddAccess':
    if(len(sys.argv)<5):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>5):
        print('Error: too many arguments for AddAccess')
        exit()

    if sys.argv[2]=='':
        print('Error: missing operation')
        exit()
    elif sys.argv[3]=='':
        print('Error: missing domain')
        exit()
    elif sys.argv[4]=='':
        print('Error: missing type')
        exit()


    print(addAccess(sys.argv[2],sys.argv[3],sys.argv[4]))

elif action=='CanAccess':
    
    if(len(sys.argv)<5):
        print('missing arguments')
        exit()
    elif(len(sys.argv)>5):
        print('Error: too many arguments for CanAccess')
        exit()

    if sys.argv[2]=='':
        print('Error: missing operation')
        exit()
    elif sys.argv[3]=='':
        print('Error: missing user')
        exit()
    elif sys.argv[4]=='':
        print('Error: missing object')
        exit()
    
    print(canAccess(sys.argv[2],sys.argv[3],sys.argv[4]))

else:
    print('Error: invalid command '+ sys.argv[1])
    exit()

