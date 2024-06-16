import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):
    body = event.get_body().decode()
    logging.info('  Function triggered to process a message: ', body)
    logging.info('  EnqueuedTimeUtc =', event.enqueued_time)
    logging.info('  SequenceNumber =', event.sequence_number)
    logging.info('  Offset =', event.offset)

    # result = json.dumps({
    #     'id': event.id,
    #     'data': event.get_json(),
    #     'topic': event.topic,
    #     'subject': event.subject,
    #     'event_type': event.event_type,
    # })

    result = json.loads(body)
    logging.info('Python EventGrid trigger processed an event: %s', result)
