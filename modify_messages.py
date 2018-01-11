"""Modify an existing Message's Labels.
"""

from apiclient import errors
import list_messages


def ModifyMessage(service, user_id, msg_id, msg_labels):
  """Modify the Labels on the given Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The id of the message required.
    msg_labels: The change in labels.

  Returns:
    Modified message, containing updated labelIds, id and threadId.
  """
  try:
    message = service.users().messages().modify(userId=user_id, id=msg_id,
                                                body=msg_labels).execute()

    label_ids = message['labelIds']

    print( 'Message ID: {} - With Label IDs {}'.format(msg_id, label_ids))
    return message
  except errors.HttpError as error:
    print( 'An error occurred: {}' .format(error))


def CreateMsgLabels():
  """Create object to update labels.

  Returns:
    A label update object.
  """
  return {'removeLabelIds': ['UNREAD'], 'addLabelIds': ['INBOX']}

if __name__ == "__main__":
    msg_ids = list_messages.get_unread_messages()
    service = list_messages.quickstart.main()[1]
    user_id = "me"
    msg_labels = CreateMsgLabels()
    for msg_id in msg_ids:
      ModifyMessage(service, user_id, msg_id, msg_labels)
    print("Good work Prof. Lemmah, all your messages are now marked as read.")
