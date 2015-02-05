# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.conversation import Conversation
from nose.tools import eq_
from nose.tools import raises


@raises(ValueError)
def test_find_no_thread_id():
    Conversation.find(email='xxx@example.com')


def test_properties():
    conversation = Conversation()
    conversation.thread_id = 12345
    conversation.read = False
    conversation.body = 'ABCDE'

    eq_(conversation.thread_id, 12345)
    eq_(conversation.read, False)

    try:
        conversation.body
    except AttributeError:
        pass
