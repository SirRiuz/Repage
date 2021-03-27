
# Rest_framework
#from rest_framework.authtoken import Token
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Django
from django.contrib.auth.hashers import check_password



class AuthSerailizer(serializers.Serializer):

    nickName = serializers.CharField(required=True,max_length=100)
    password = serializers.CharField(required=True,max_length=50)


    def auth(self,nickName,password,model) -> (dict):
        nickName = nickName
        password = password
        data = ({})

        user = model.objects.filter(nickName=nickName)
        if len(user) > 0:
            user = user[0]
            if check_password(password,user.password):
                userToken = Token.objects.get_or_create(user=user)
                token = userToken[0].key
                data = ({
                    'status':'ok',
                    'data':{
                        'id':user.id,
                        'email':user.email,
                        'nickName':user.nickName,
                        'token':token
                    }
                })

            else:
                data = ({
                    'status':'error',
                    'type-error':'password-error',
                    'messege':'The password not is correct .'
                })

        else:
            data = ({
                'status':'error',
                'type-error':'user-not-found',
                'messege':'The user not exits'
            })


            

        return data


