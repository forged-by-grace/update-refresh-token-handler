from core.model.update_model import UpdateFieldAvro, UpdateAvro
from core.model.token_models import UpdateToken

from core.event.produce_event import produce_event

from core.utils.settings import settings
from core.utils.init_log import logger

from datetime import datetime


async def update_refresh_token(data: UpdateToken) -> None:
   
    # Create database field objs
    token_field = UpdateFieldAvro(action='$set', value={'tokens.$': data.new_token})
    last_update_field = UpdateFieldAvro(action='$set', value={'last_update': datetime.utcnow().isoformat()})
    
    # Create update list
    account_updates = UpdateAvro(
        db_metadata={'provider': 'mongoDB', 
                     'database': 'account_db', 
                     'collection': 'accounts'},
        db_filter={
            '_id': data.id,
            'tokens': data.old_token
        },
        updates=[
            token_field,
            last_update_field,
        ]
    )

    await emit_update_event(account_updates=account_updates)

   
async def emit_update_event(account_updates: UpdateAvro) -> None:
    # Serialize    
    account_updates_event = account_updates.serialize()

    # Emit event
    logger.info('Emitting update account event')
    await produce_event(topic=settings.api_update_account, value=account_updates_event)

