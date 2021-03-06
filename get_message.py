"""Get Message with given ID.
"""

import base64
import email
import quickstart
from apiclient import errors
from googleapiclient.discovery import build

def get_message(service, user_id, msg_id):
  """Get a Message with given ID.
  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.
  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print('Message snippet: {}'.format(message['snippet']))

    return message
  except errors.HttpError as error:
    print('An error occurred: {}'.format(error))

def get_mime_message(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.
  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.
  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    print('Message snippet: {}'.format(message['snippet']))

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except errors.HttpError as error:
    print('An error occurred: {}'.format(error))

def build_service(credentials):
    """Build a Gmail Service Object
    Args:
        credentials: OAuth 2.0 Credentials
    Returns:
        Gmail service object
    """
    http = httplib2.Http()
    http = credentials.authorize(http)
    return build('gmail', 'v1', http=http)

get_message(quickstart.main()[1], 'me', '160e3c6cf92364ba')
