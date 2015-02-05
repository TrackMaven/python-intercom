# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" conversation module.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'
>>> from intercom import Conversation

"""

from . import Intercom
from . import from_timestamp_property


class Conversation(dict):
    """ An Intercom conversation between an admin and a User. """

    @classmethod
    def find(cls, user_id=None, email=None, thread_id=None):
        """ Finds a particular conversation for a particular user.

        >>> conversation = Conversation.find(email="somebody@example.com")
        Traceback (most recent call last):
            ...
        ValueError: No thread_id specified
        >>> conversation = Conversation.find(email="somebody@example.com",
        ... thread_id=5591)
        >>> len(conversation.messages)
        3
        >>> message = conversation.messages[0]
        >>> type(message)
        <class 'intercom.conversation.Message'>

        """
        if thread_id is None:
            raise ValueError("No thread_id specified")
        resp = Intercom.get_conversations(
            user_id=user_id, email=email, thread_id=thread_id)
        return Conversation(resp)

    @classmethod
    def find_all(cls, user_id=None, email=None):
        """ Finds all Messages for a particular user.

        >>> conversations = Conversation.find_all(
        ... email="somebody@example.com")
        >>> len(conversations)
        1

        """
        resp = Intercom.get_conversations(user_id=user_id, email=email)
        return [Conversation(mt) for mt in resp]

    @classmethod
    def create(cls, user_id=None, email=None, body=None):
        """ Creates a new converstion.

        >>> email = "somebody@example.com"
        >>> body = "Hi everybody, I'm Doctor Nick"
        >>> conversation = Conversation.create(email=email, body=body)
        >>> conversation.thread_id
        5591
        >>> len(conversation.messages)
        3

        """
        resp = Intercom.create_conversation(
            user_id=user_id, email=email, body=body)
        return Conversation(resp)

    @classmethod
    def reply(
            cls, user_id=None, email=None, thread_id=None, body=None,
            read=None):
        """ Reply to an existing conversation.

        >>> email = "somebody@example.com"
        >>> thread_id = 5591
        >>> body = "Are you talking to me?"
        >>> conversation = Conversation.reply(email=email,
        ... thread_id=thread_id, body=body)
        >>> len(conversation.messages)
        3
        >>> conversation.messages[0].html
        u'<p>Hey Intercom, What is up?</p>\n\n<p></p>'
        >>> conversation.messages[1].html
        u'<p>Not much, you?\n</p>'
        >>> conversation.messages[2].html
        u'<p>Not much either :(</p>\n\n<p></p>'

        """
        resp = Intercom.reply_conversation(
            user_id=user_id, email=email, thread_id=thread_id,
            read=read, body=body)
        return Conversation(resp)

    @property
    @from_timestamp_property
    def updated_at(self):
        """ Returns a datetime of when the last update occurred. """
        return dict.get(self, 'updated_at', None)

    @property
    @from_timestamp_property
    def created_at(self):
        """ Sets a timestamp of when the last update occurred. """
        return dict.get(self, 'created_at', None)

    def set_body(self, value):
        """ Set the body of a reply. """
        self['body'] = value
    body = property(None, set_body, None)

    @property
    def thread_id(self):
        """ Returns the thread_id of this Conversation. """
        return dict.get(self, 'thread_id', None)

    @thread_id.setter
    def thread_id(self, value):
        """ Sets the thread_id of this Conversation. """
        self['thread_id'] = value

    @property
    def read(self):
        """ Returns whether this thread has been read or not. """
        return dict.get(self, 'read', None)

    @read.setter
    def read(self, value):
        """ Sets whether this thread has been read or not. """
        self['read'] = value

    @property
    def messages(self):
        """ Returns a list of Messages in this Conversation. """
        messages = dict.get(self, 'messages', None)
        if messages:
            return [Message(m) for m in messages]


class Message(dict):
    """ Object representing a Message in a Conversation.

    >>> conversation = Conversation.find(email="somebody@example.com",
    ... thread_id=5591)
    >>> message = conversation.messages[0]
    >>> type(message.author)
    <class 'intercom.conversation.Conversation'>
    >>> message.html
    u'<p>Hey Intercom, What is up?</p>\n\n<p></p>'
    >>> type(message.created_at)
    <type 'datetime.datetime'>

    """

    @property
    def author(self):
        """ Returns who authored the message. """
        _from = self.get('from', None)
        if _from:
            return Conversation(_from)

    @property
    def html(self):
        """ Returns the HTML body of the Message. """
        return dict.get(self, 'html', None)

    @property
    @from_timestamp_property
    def created_at(self):
        """ Returns a datetime for when this Message was created. """
        return dict.get(self, 'created_at', None)


class ConversationAuthor(dict):
    """ Object represting the author of a Conversatoin.

    >>> conversation = Conversation.find(email="somebody@example.com",
    ... thread_id=5591)
    >>> author = conversation.messages[0].author
    >>> author.admin
    False
    >>> author.email
    u'bob@example.com'
    >>> author.user_id
    u'456'
    >>> author.avatar_path_50

    >>> author.name
    u'Bob'

    """

    @property
    def admin(self):
        """ Returns whether the author is an admin. """
        return dict.get(self, 'is_admin', None)

    @property
    def email(self):
        """ Returns the email address of the author. """
        return dict.get(self, 'email', None)

    @property
    def user_id(self):
        """ Returns the user_id of the author. """
        return dict.get(self, 'user_id', None)

    @property
    def avatar_path_50(self):
        """ Returns a URL to a 50x50 avatar of the author. """
        return dict.get(self, 'avatar_path_50', None)

    @property
    def name(self):
        """ Returns the author's name. """
        return dict.get(self, 'name', None)
