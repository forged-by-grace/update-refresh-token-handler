from core.helper.consumer_helper import consume_event
from core.utils.settings import settings
from core.utils.init_log import logger
from core.helper.token_helper import update_refresh_token
from core.model.token_models import UpdateToken

# Processing event msg
event_processing_msg = "Processing event"

async def consume_update_token_event():
    # consume event
    consumer = await consume_event(topic=settings.api_update_token, group_id=settings.api_update_token)
    
    try:
        # Consume messages
        async for msg in consumer: 
            logger.info('Received update refresh token event.') 
            
            # Deserialize event
            update_token_data = UpdateToken.deserialize(data=msg.value)
            
            # update token
            logger.info(event_processing_msg)
            await update_refresh_token(data=update_token_data)
    except Exception as err:
        logger.error(f'Failed to process event due to error: {str(err)}')
    finally:
        await consumer.stop()

