from pydantic import Field
from dataclasses_avroschema.pydantic import AvroBaseModel

id_description: str = "Used to identify the account"


class UpdateToken(AvroBaseModel):
    id: str = Field(description='Used to identify the account')
    old_token: str = Field(description='Encrypted old refresh token')
    new_token: str = Field(description='Encrypted new refresh token')

