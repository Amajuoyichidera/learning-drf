from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view,APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):

    if request.method == 'POST':
        data = request.data

        response = {'message':'Hello World', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)
  
    response = {'message':'Hello World'}
    return Response(data=response, status=status.HTTP_200_OK)



# class PostListCreateView(APIView):
#     # view for creating and listing posts

#     serializer_class = PostSerializer

#     def get(self,request:Request,*args,**kwargs):
#         posts = Post.objects.all()

#         serializer = self.serializer_class(instance=posts, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

    
#     def post(self,request:Request,*args,**kwargs):
#         data=request.data

#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response={
#                 'message':'post created',
#                 'data':serializer.data
#             }

#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PostRetrieveUpdateDeleteView(APIView):
#     serializer_class = PostSerializer


#     def get(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)

#         serializer = self.serializer_class(instance=post)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


#     def put(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)

#         data=request.data

#         serializer = self.serializer_class(instance=post, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response ={
#                 'message': 'post updated',
#                 'data':serializer.data
#             }
#             return Response(data=response, status=status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)

#         post.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
    


class PostListCreateView(generics.GenericAPIView,
    mixins.ListModelMixin,mixins.CreateModelMixin
):
    serializer_class = PostSerializer
    permission_classes=[IsAuthenticated]
    queryset = Post.objects.all()

    def get(self, request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

    def post(self, request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        

class PostRetrieveUpdateDeleteView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self,request:Request, *args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    

    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request:Request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
