from django.http import JsonResponse

from kafka_integration.service.kafka_service import KafkaService


def produce_view(request):
    kafka_service = KafkaService()
    kafka_service.produce_message('test-topic', {'key': 'value'})
    return JsonResponse({'status': 'Message sent to Kafka'})
