from django.shortcuts import render
from rest_framework.response import Response
from API_APP.models import Profile
from API_APP.serializer import ProfileSerializersAPI
from rest_framework.views import APIView
from rest_framework import status

class ProfileView(APIView):
    def get(self,request, pk=None,format=None):
        id = pk
        if id is not None:
            candidates = Profile.objects.get(id=id)
            serializer = ProfileSerializersAPI(candidates)
            return Response(serializer.data)

        candidates = Profile.objects.all()
        serializer = ProfileSerializersAPI(candidates, many=True)
        return Response(
            {
                'status':'success',
                'candidates': serializer.data
            },
            status=status.HTTP_200_OK
            )
     
    def post(self,request,format=None):
        serializer = ProfileSerializersAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                'msg':'Resume Upload Successfully',
                'status':'success',
                'cadidate': serializer.data
                },
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id= pk
        candidate = Profile.objects.get(pk=id)
        serializer = ProfileSerializersAPI( candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'msg':'Resume Updated to successfully'
                }
            )
        return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )
    def patch(self,request,pk,format=None):
        id= pk
        candidate = Profile.objects.get(pk=id)
        serializer = ProfileSerializersAPI( candidate, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                        'msg':'Resume Updated Partial to successfully'
                         })
        return Response(serializer.errors,)
    def delete(self,request,pk,format=None):
        id= pk
        candidate = Profile.objects.get(pk=id)
        candidate.delete()
        return Response({
            'msg': 'Resume Deleted Successfully'
        })