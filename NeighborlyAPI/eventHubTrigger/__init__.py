import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):
    body = event.get_body().decode()
    logging.info('Function triggered to process a message: ', {body})
    logging.info('  EnqueuedTimeUtc =', event.enqueued_time)
    logging.info('  SequenceNumber =', event.sequence_number)
    logging.info('  Offset =', event.offset)

    result = json.loads(body)
    logging.info('Python EventGrid trigger processed an event: %s', result)
