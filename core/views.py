import asyncio
from django.http import JsonResponse

async def contador_view(request):
    for i in range(5):
        print(f"Contando: {i + 1}")
        await asyncio.sleep(1)
    return JsonResponse({"mensagem": "Contador assíncrono finalizado!"})
