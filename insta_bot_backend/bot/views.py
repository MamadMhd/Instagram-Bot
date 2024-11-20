from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BotConfig, BotLog
from .utils import run_bot

class BotConfigView(APIView):
    def get(self, request):
        configs = BotConfig.objects.all().values()
        return Response(configs, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        config = BotConfig.objects.create(
            username=data['username'],
            password=data['password'],
            target_hashtags=data['target_hashtags']
        )
        return Response({"id": config.id}, status=status.HTTP_201_CREATED)

class BotRunView(APIView):
    def post(self, request, pk):
        try:
            config = BotConfig.objects.get(pk=pk)
            result = run_bot(config.username, config.password, config.target_hashtags)
            BotLog.objects.create(bot=config, action="run", status=result)
            return Response({"result": result}, status=status.HTTP_200_OK)
        except BotConfig.DoesNotExist:
            return Response({"error": "Bot config not found"}, status=status.HTTP_404_NOT_FOUND)
