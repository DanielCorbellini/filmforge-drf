from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.api.serializers import WatchListSerializer, StreamPlataformSerializer
from watchlist_app.models import WatchList, StreamPlataform


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlataformAV(APIView):
    def get(self, request):
        plataforms = StreamPlataform.objects.all()
        serializer = StreamPlataformSerializer(plataforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlataformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlataformDetailAV(APIView):
    def get(self, request, pk):
        try:
            streamplataform = StreamPlataform.objects.get(pk=pk)
        except StreamPlataform.DoesNotExist:
            return Response({'Error': 'Plataform not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlataformSerializer(streamplataform)
        return Response(serializer.data)

    def put(self, request, pk):
        streamplataform = StreamPlataform.objects.get(pk=pk)
        serializer = StreamPlataformSerializer(
            streamplataform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        streamplataform = StreamPlataform.objects.get(pk=pk)
        streamplataform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
