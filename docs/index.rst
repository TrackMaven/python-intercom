===============
python-intercom
===============

.. toctree::
    installation
    api/modules
    changelog
    development

Installation
============

Stable releases of python-intercom can be installed with 
`pip <http://pip.openplans.org>`_ or you may download a `.tgz` source 
archive from `pypi <http://pypi.python.org/pypi/python-intercom#downloads>`_.
See the :doc:`installation` page for more detailed instructions.

If you want to use the latest code, you can grab it from our 
`Git repository <http://github.com/jkeyes/python-intercom>`_, or `fork it <http://github.com/jkeyes/python-intercom>`_.

Usage
===================================

Authentication
---------------

Intercom documentation: `Authorization
<http://doc.intercom.io/api/#authorization>`_.

::

    from intercom import Intercom
    Intercom.app_id = 'dummy-app-id'
    Intercom.api_key = 'dummy-api-key'

Users
-----

Get All Users
+++++++++++++++++

Intercom documentation: `List Users
<http://doc.intercom.io/api/#list-users>`_.

::

    from intercom import User
    for user in User.all():
        print user.email

View a User
++++++++++++++

Intercom documentation: `View a User
<http://doc.intercom.io/api/#view-a-user>`_.

::

    user = User.find(email="ben@intercom.io")

Create a User
+++++++++++++

Intercom documentation: `Create or Update User
<http://doc.intercom.io/api/#create-or-update-user>`_.

::

    user = User.create(email="ben@intercom.io",
            user_id=7902,
            name="Ben McRedmond",
            created_at=datetime.now(),
            custom_data={"plan": "pro"},
            last_seen_ip="1.2.3.4",
            last_seen_user_agent="ie6")

Updating a User
+++++++++++++++

Intercom documentation: `Create or Update User
<http://doc.intercom.io/api/#create-or-update-user>`_.

::

    user = User.find(email="ben@intercom.io")
    user.name = "Benjamin McRedmond"
    user.save()

Delete a User
+++++++++++++++

Intercom documentation: `Delete a user
<http://doc.intercom.io/api/#delete-a-user>`_.

::

    deleted_user = User.delete(email="ben@intercom.io")

Notes
-----

Create a Note
+++++++++++++++

Intercom documentation: `Create a Note
<http://doc.intercom.io/api/#create-a-note>`_.

::

    from intercom import Note
    note = Note.create(email="ben@intercom.io", 
            body="These are a few of my favourite things.")


Tagging
-------

List Tags
+++++++++++++

Intercom documentation: `List Tags
<http://doc.intercom.io/api/#list-tags-for-an-app>`_.

::

    from intercom import Tag
    tag = Tag.find_by_name("Free Trial")

Creating a new Tag
++++++++++++++++++

Intercom documentation: `Creating and Update Tags
<http://doc.intercom.io/api/#create-and-update-tags>`_.

::

    from intercom import Tag
    tag = Tag.create("Free Trial")

Updating an already existing Tag
++++++++++++++++++++++++++++++++

Intercom documentation: `Create and Update Tags
<http://doc.intercom.io/api/#create-and-update-tags>`_.

::

    from intercom import Tag
    tag = Tag.update("Free Trial", "tag",
        user_ids=["abc123", "def456"])

Conversations
---------------

List Conversations
+++++++++++++++++++++++

Intercom documentation:  `List Conversations
<http://doc.intercom.io/api/#list-conversations>`_.

::

    from intercom import MessageThread

    # all message threads
    message_threads = MessageThread.find_all(email="ben@intercom.io")

    # a specific thread
    message_threads = MessageThread.find_all(email="ben@intercom.io",
            thread_id=123)

Get a Single Conversation
+++++++++++++++++++++++++

Intercom documentation:  `Get a Single Conversation
<http://doc.intercom.io/api/#get-a-single-conversation>`_.


Admin Initiated Conversation
+++++++++++++++++++++++++

Intercom documentation:  `Admin Initiated Conversation
<http://doc.intercom.io/api/#admin-initiated-conversation>`_.

::

    message_thread = MessageThread.create(email="ben@intercom.io", 
            body="Hey Intercom, What is up?")

User Initiated Conversation
+++++++++++++++++++++++++

Intercom documentation:  `User Initiated Conversation
<http://doc.intercom.io/api/#user-initiated-conversation>`_.

::

    message_thread = MessageThread.create(email="ben@intercom.io", 
            body="Hey Intercom, What is up?")


Replying to a Conversation
++++++++++++++++++++++++++++

Intercom documentation:  `Replying to a Conversation
<http://doc.intercom.io/api/#replying-to-a-conversation>`_.

::

    message_thread = MessageThread.create(email="ben@intercom.io",
            thread_id=123,
            body="Not much either :(")

Events
-----------

Submitting Events
+++++++++++++++++

Intercom documentation: `Submitting Events
<http://doc.intercom.io/api/#submitting-events>`_.

::

    from intercom import Event
    impression = Event.create(event_name="sent-invite", 
            user_id="314159")

Development
===========

Our :doc:`development` page has detailed instructions on how to run our
tests, and to produce coverage and pylint reports.

Changelog
=========

The :doc:`changelog` keeps track of changes per release.

pydoc
=====

View the extensive `pydoc <api/modules.html>`_ which has liberal helpings of
`doctests` to display usage.

